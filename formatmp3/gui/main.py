#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Fenêtre principale de l'application
@author: Julien
'''



from ActionGui import *
from formatmp3.actions.Action import *
from wx.lib.pubsub import pub as Publisher
import os.path
import pickle
import threading
import wx



# Liste des actions de l'application
actions = [CaseChange, ReplaceString, Cut, InsertString]



class Model(object):
    '''
    Modèle
    Contient les fichiers à modifier et les action à effectuer
    @author: Julien
    '''
    
    
    # Messages émis à l'interface graphique
    ERROR = "ERROR"
    FILESAVE_CHANGED = "FILESAVE_CHANGED"
    FILELIST_CHANGED = "FILELIST_CHANGED"
    ACTIONLIST_CHANGED = "ACTIONLIST_CHANGED"
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        self._stop = False
        self.filesave = None
        self.filelist = []
        self.actionlist = []
    
    # Ajout/Suppression de fichiers/répertoire
    
    def _addFile(self, path):
        '''
        Ajouter un fichier
        @param path: path
        @author: Julien
        '''
        if path not in self.filelist:
            self.filelist.append(path)
    
    
    def addFile(self, path):
        '''
        Ajouter un fichier
        @param path: Path
        @author: Julien
        '''
        oldCount = len(self.filelist)
        self._addFile(path)
        newCount = len(self.filelist)
        if oldCount < newCount:
            self.filelist.sort()
            Publisher.sendMessage(Model.FILELIST_CHANGED)
    
    
    def addFiles(self, pathlist=[]):
        '''
        Ajouter des fichiers
        @param pathlist: Liste des path
        @author: Julien
        '''
        oldCount = len(self.filelist)
        for path in pathlist:
            self._addFile(path)
        newCount = len(self.filelist)
        if oldCount < newCount:
            self.filelist.sort()
            Publisher.sendMessage(Model.FILELIST_CHANGED)
    
    
    def _addFolder(self, strDirname):
        '''
        Ajout de chacun des fichiers contenus dans le répertoire de manière récursive
        @param strDirname: Path du répertoire
        @author: Julien
        '''
        for basename in os.listdir(strDirname):
            strPath = os.path.join(strDirname, basename)
            if os.path.isdir(strPath):
                self._addFolder(strPath)
            elif os.path.isfile(strPath):
                path = Path(strPath)
                self._addFile(path)
    
    
    def addFolder(self, path):
        '''
        Ajouter un répertoire
        @param path: Path du répertoire
        @author: Julien
        '''
        oldCount = len(self.filelist)
        self._addFolder(path)
        newCount = len(self.filelist)
        if oldCount < newCount:
            self.filelist.sort()
            Publisher.sendMessage(Model.FILELIST_CHANGED)
    
    
    def removeFiles(self, pathlist=[]):
        '''
        Retirer des fichiers
        @param pathlist: Liste des chemins des fichiers
        @author: Julien
        '''
        filesDeleted = False
        for path in pathlist:
            if path in self.filelist:
                self.filelist.remove(path)
                filesDeleted = True
        if filesDeleted:
            Publisher.sendMessage(Model.FILELIST_CHANGED)
    
    
    def removeAllFiles(self):
        '''
        Retirer tous les fichiers
        @author: Julien
        '''
        if self.filelist:
            self.filelist = []
            Publisher.sendMessage(Model.FILELIST_CHANGED)
    
    
    def AddAction(self, action):
        '''
        Ajouter une action
        @param action: Action
        @author: Julien
        '''
        self.actionlist.append(action)
        Publisher.sendMessage(Model.ACTIONLIST_CHANGED)
    
    
    def getOverviewFilelist(self):
        '''
        Obtenir la liste des fichiers avec l'aperçu des modifications
        @return: Liste des fichiers
        @author: Julien
        '''
        overviews = []
        for path in self.filelist:
            for action in self.actionlist:
                path = action.getOverview(path)
            overviews.append(path)
        return overviews
    
    
    def SwapActions(self, i1, i2):
        '''
        Echanger 2 actions
        @param i1: Indice 1
        @param i2: Indice 2
        @author: Julien
        '''
        self.actionlist[i1], self.actionlist[i2] = self.actionlist[i2], self.actionlist[i1]
        Publisher.sendMessage(Model.ACTIONLIST_CHANGED)
    
    
    def removeAction(self, action):
        '''
        Retirer des fichiers
        @param action: Action
        @author: Julien
        '''
        if action in self.actionlist:
            self.actionlist.remove(action)
            Publisher.sendMessage(Model.ACTIONLIST_CHANGED)
    
    
    def removeAllActions(self):
        '''
        Retirer toutes les actions
        @author: Julien
        '''
        if self.actionlist:
            self.actionlist = []
            Publisher.sendMessage(Model.ACTIONLIST_CHANGED)
    
    # Exécution
    
    def stop(self):
        '''
        Arrêter l'exécution
        @author: Julien
        '''
        self._stop = True
    
    
    def Execute(self):
        '''
        Exécuter les actions sur les fichiers
        @author: Julien
        '''
        for path in self.filelist:
            try:
                for action in self.actionlist:
                    if self._stop:
                        Publisher.sendMessage(Model.FILELIST_CHANGED)
                        return
                    action.execute(path)
            except BaseException, err:
                Publisher.sendMessage(Model.ERROR, error=err)
        Publisher.sendMessage(Model.FILELIST_CHANGED)
        self._stop = True
    
    # Chargement et sauvegarde
    
    def open(self, path):
        '''
        Charger les actions du fichier
        @param path: Fichier d'entrée
        @author: Julien
        '''
        fichier = open(path.get(), 'r')
        self.actionlist = pickle.load(fichier)
        self.filesave = path.get()
        Publisher.sendMessage(Model.ACTIONLIST_CHANGED)
    
    
    def save(self, path):
        '''
        Enregistrer les actions dans un fichier
        @param path: Fichier de sortie
        @author: Julien
        '''
        fichier = open(path.get(), 'w')
        pickle.dump(self.actionlist, fichier)
        fichier.close()
        self.filesave = path



class View(wx.Frame):
    '''
    Vue
    @author: Julien
    '''
    
    
    iconMenuSize = wx.Size(16,16)
    iconMaintoolbarSize = iconMenuSize
    iconToolbarSize = iconMenuSize
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        # Fenêtre
        minSize = (675,700)
        wx.Frame.__init__(self, None, title="FormatMP3 - Formatez vos fichiers MP3 en un clic !", size=minSize)
        #self.SetMinSize(minSize)
        self.CenterOnScreen()
        
        # Barre de menus
        menubar = wx.MenuBar(0)
        self.SetMenuBar(menubar)
        #     Fichier
        menubar_fichier = wx.Menu()
        menubar.Append(menubar_fichier, "&Fichier")
        #         Ouvrir
        self.menubar_fichier_ouvrir = wx.MenuItem(menubar_fichier, wx.ID_ANY, "&Ouvrir\tCtrl+O")
        menubar_fichier_ouvrir_image = wx.Image("icons/open.png")
        menubar_fichier_ouvrir_image.Rescale(View.iconMenuSize.width, View.iconMenuSize.height)
        menubar_fichier_ouvrir_bitmap = wx.BitmapFromImage(menubar_fichier_ouvrir_image)
        self.menubar_fichier_ouvrir.SetBitmap(menubar_fichier_ouvrir_bitmap)
        menubar_fichier.AppendItem(self.menubar_fichier_ouvrir)
        #     .
        menubar_fichier.AppendSeparator()
        #         Enregistrer
        self.menubar_fichier_enregistrer = wx.MenuItem(menubar_fichier, wx.ID_ANY, "&Enregistrer\tCtrl+S")
        menubar_fichier_enregistrer_image = wx.Image("icons/save.png")
        menubar_fichier_enregistrer_image.Rescale(View.iconMenuSize.width, View.iconMenuSize.height)
        menubar_fichier_enregistrer_bitmap = wx.BitmapFromImage(menubar_fichier_enregistrer_image)
        self.menubar_fichier_enregistrer.SetBitmap(menubar_fichier_enregistrer_bitmap)
        menubar_fichier.AppendItem(self.menubar_fichier_enregistrer)
        #         Enregistrer sous
        self.menubar_fichier_enregistrerSous = wx.MenuItem(menubar_fichier, wx.ID_ANY, "Enregistrer &sous...\tCtrl-Shift+S")
        menubar_fichier_enregistrerSous_image = wx.Image("icons/save.png")
        menubar_fichier_enregistrerSous_image.Rescale(View.iconMenuSize.width, View.iconMenuSize.height)
        menubar_fichier_enregistrerSous_bitmap = wx.BitmapFromImage(menubar_fichier_enregistrerSous_image)
        self.menubar_fichier_enregistrerSous.SetBitmap(menubar_fichier_enregistrerSous_bitmap)
        menubar_fichier.AppendItem(self.menubar_fichier_enregistrerSous)
        #     .
        menubar_fichier.AppendSeparator()
        #         Quitter
        self.menubar_fichier_quitter = wx.MenuItem(menubar_fichier, wx.ID_ANY, "&Quitter\tAlt+F4")
        menubar_fichier_quitter_image = wx.Image("icons/exit.png")
        menubar_fichier_quitter_image.Rescale(View.iconMenuSize.width, View.iconMenuSize.height)
        menubar_fichier_quitter_bitmap = wx.BitmapFromImage(menubar_fichier_quitter_image)
        self.menubar_fichier_quitter.SetBitmap(menubar_fichier_quitter_bitmap)
        menubar_fichier.AppendItem(self.menubar_fichier_quitter)
        #     Aide
        menubar_aide = wx.Menu()
        menubar.Append(menubar_aide, "&?")
        #         A propos
        self.menubar_aide_aPropos = wx.MenuItem(menubar_aide, wx.ID_ANY, "A &propos de FormatMP3")
        menubar_aide.AppendItem(self.menubar_aide_aPropos)
        
        # Barre d'outils
        toolBar = self.CreateToolBar()
        #     Quitter
        exit_image = wx.Image("icons/exit.png")
        exit_image.Rescale(View.iconMaintoolbarSize.width, View.iconMaintoolbarSize.height)
        exit_bitmap = wx.BitmapFromImage(exit_image)
        self.exit_tool = toolBar.AddLabelTool(wx.ID_ANY, "Quitter", exit_bitmap)
        # .
        toolBar.Realize()
        
        # Barre de statut
        statusBar = self.CreateStatusBar()
        
        # Sizer
        frame_boxSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(frame_boxSizer)
        #     Splitter
        main_splitterWindow = wx.SplitterWindow(self, style=wx.SP_3D|wx.SP_NO_XP_THEME)
        frame_boxSizer.Add(main_splitterWindow, 1, wx.ALL|wx.EXPAND)
        #         Fichiers à modifier
        files_panel = wx.Panel(main_splitterWindow)
        files_boxSizer = wx.BoxSizer(wx.VERTICAL)
        files_panel.SetSizer(files_boxSizer)
        #             Titre
        title_files_staticText = wx.StaticText(files_panel, label="Fichiers à modifier")
        title_files_font = wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_files_staticText.SetFont(title_files_font)
        files_boxSizer.Add(title_files_staticText, flag=wx.ALL, border=5)
        #             Barre d'outils
        files_toolbar = wx.ToolBar(files_panel, style=wx.TB_FLAT|wx.TB_TEXT)
        files_boxSizer.Add(files_toolbar, flag=wx.EXPAND)
        #                 Ajouter un fichier
        addFile_image = wx.Image("icons/add_file.png")
        addFile_image.Rescale(View.iconToolbarSize.width, View.iconToolbarSize.height)
        addFile_bitmap = wx.BitmapFromImage(addFile_image)
        self.addFile_tool = files_toolbar.AddLabelTool(wx.ID_ANY, label="Ajouter fichier", bitmap=addFile_bitmap, shortHelp="Ajouter un fichier dans la liste")
        #                 Ajouter un répertoire
        addFolder_image = wx.Image("icons/add_folder.png")
        addFolder_image.Rescale(View.iconToolbarSize.width, View.iconToolbarSize.height)
        addFolder_bitmap = wx.BitmapFromImage(addFolder_image)
        self.addFolder_tool = files_toolbar.AddLabelTool(wx.ID_ANY, label="Ajouter répertoire", bitmap=addFolder_bitmap, shortHelp="Ajouter un répertoire dans la liste")
        #             .
        files_toolbar.AddSeparator()
        #                 Supprimer la sélection
        removeSelectedListFiles_image = wx.Image("icons/remove_selected.png")
        removeSelectedListFiles_image.Rescale(View.iconToolbarSize.width, View.iconToolbarSize.height)
        removeSelectedListFiles_bitmap = wx.BitmapFromImage(removeSelectedListFiles_image)
        self.removeSelectedListFiles_tool = files_toolbar.AddLabelTool(wx.ID_ANY, label="Supp. sélection", bitmap=removeSelectedListFiles_bitmap, shortHelp="Supprimer les fichiers sélectionnés de la liste")
        #                 Supprimer tout
        removeAllListFiles_image = wx.Image("icons/remove_all.png")
        removeAllListFiles_image.Rescale(View.iconToolbarSize.width, View.iconToolbarSize.height)
        removeAllListFiles_bitmap = wx.BitmapFromImage(removeAllListFiles_image)
        self.removeAllListFiles_tool = files_toolbar.AddLabelTool(wx.ID_ANY, label="Supp. tout", bitmap=removeAllListFiles_bitmap, shortHelp="Supprimer tous les fichiers de la liste")
        #             .
        files_toolbar.Realize()
        #             Liste
        self.listFiles_listCtrl = wx.ListCtrl(files_panel, style=wx.LC_REPORT)
        self.listFiles_listCtrl.InsertColumn(0, "Dossier", width=300)
        self.listFiles_listCtrl.InsertColumn(1, "Nom d'origine", width=150)
        self.listFiles_listCtrl.InsertColumn(2, "Nouveau nom", width=150)
        files_boxSizer.Add(self.listFiles_listCtrl, 1, wx.ALL|wx.EXPAND, 5)
        #         Actions
        actions_panel = wx.Panel(main_splitterWindow)
        self.actions_boxSizer = wx.BoxSizer(wx.VERTICAL)
        actions_panel.SetSizer(self.actions_boxSizer)
        #             Titre
        title_actions_staticText = wx.StaticText(actions_panel, label="Actions à réaliser")
        title_actions_font = wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_actions_staticText.SetFont(title_actions_font)
        self.actions_boxSizer.Add(title_actions_staticText, flag=wx.ALL, border=5)
        #             Barre d'outils
        actions_toolbar = wx.ToolBar(actions_panel, style=wx.TB_FLAT|wx.TB_TEXT)
        self.actions_boxSizer.Add(actions_toolbar, flag=wx.EXPAND)
        #                 Ajouter
        addAction_image = wx.Image("icons/add.png")
        addAction_image.Rescale(View.iconToolbarSize.width, View.iconToolbarSize.height)
        addAction_bitmap = wx.BitmapFromImage(addAction_image)
        self.addAction_tool = actions_toolbar.AddLabelTool(wx.ID_ANY, label="Ajouter", bitmap=addAction_bitmap, shortHelp="Ajouter une action à la liste")
        #             .
        actions_toolbar.AddSeparator()
        #                 Supprimer la sélection
        removeSelectedAction_image = wx.Image("icons/remove_selected.png")
        removeSelectedAction_image.Rescale(View.iconToolbarSize.width, View.iconToolbarSize.height)
        removeSelectedAction_bitmap = wx.BitmapFromImage(removeSelectedAction_image)
        self.removeSelectedAction_tool = actions_toolbar.AddLabelTool(wx.ID_ANY, label="Supp. sélection", bitmap=removeSelectedAction_bitmap, shortHelp="Supprimer l'action sélectionné de la liste")
        #                 Supprimer tout
        removeAllActions_image = wx.Image("icons/remove_all.png")
        removeAllActions_image.Rescale(View.iconToolbarSize.width, View.iconToolbarSize.height)
        removeAllActions_bitmap = wx.BitmapFromImage(removeAllActions_image)
        self.removeAllActions_tool = actions_toolbar.AddLabelTool(wx.ID_ANY, label="Supp. tout", bitmap=removeAllActions_bitmap, shortHelp="Supprimer toutes les actions de la liste")
        #             .
        actions_toolbar.AddSeparator()
        #                 Monter l'action
        upSelectedAction_image = wx.Image("icons/up.png")
        upSelectedAction_image.Rescale(View.iconToolbarSize.width, View.iconToolbarSize.height)
        upSelectedAction_bitmap = wx.BitmapFromImage(upSelectedAction_image)
        self.upSelectedAction_tool = actions_toolbar.AddLabelTool(wx.ID_ANY, label="Monter", bitmap=upSelectedAction_bitmap, shortHelp="Monter l'action sélectionnée dans la liste")
        #                 Descendre l'action
        downSelectedAction_image = wx.Image("icons/down.png")
        downSelectedAction_image.Rescale(View.iconToolbarSize.width, View.iconToolbarSize.height)
        downSelectedAction_bitmap = wx.BitmapFromImage(downSelectedAction_image)
        self.downSelectedAction_tool = actions_toolbar.AddLabelTool(wx.ID_ANY, label="Descendre", bitmap=downSelectedAction_bitmap, shortHelp="Descendre l'action sélectionnée dans la liste")
        #             .
        actions_toolbar.AddSeparator()
        #                 Exécuter
        executeActions_image = wx.Image("icons/execute.png")
        executeActions_image.Rescale(View.iconToolbarSize.width, View.iconToolbarSize.height)
        executeActions_bitmap = wx.BitmapFromImage(executeActions_image)
        self.executeActions_tool = actions_toolbar.AddLabelTool(wx.ID_ANY, label="Exécuter", bitmap=executeActions_bitmap, shortHelp="Exécuter les actions sur les fichiers")
        #                 Stoper
        stopActions_image = wx.Image("icons/stop.png")
        stopActions_image.Rescale(View.iconToolbarSize.width, View.iconToolbarSize.height)
        stopActions_bitmap = wx.BitmapFromImage(stopActions_image)
        self.stopActions_tool = actions_toolbar.AddLabelTool(wx.ID_ANY, label="Stop", bitmap=stopActions_bitmap, shortHelp="Arrêter l'exécution")
        #             .
        actions_toolbar.Realize()
        #             Splitter
        self.actions_splitter = wx.SplitterWindow(actions_panel, style=wx.SP_3D|wx.SP_NO_XP_THEME)
        self.actions_boxSizer.Add(self.actions_splitter, 1, wx.ALL|wx.EXPAND)
        #                 Liste des actions
        listActions_panel = wx.Panel(self.actions_splitter)
        listActions_boxSizer = wx.BoxSizer(wx.VERTICAL)
        listActions_panel.SetSizer(listActions_boxSizer)
        #                     Liste
        self.listActionsToDo_listBox = wx.ListBox(listActions_panel)
        listActions_boxSizer.Add(self.listActionsToDo_listBox, 1, wx.ALL|wx.EXPAND, 5)
        #                 Action sélectionnée
        self.selectedAction_panel = wx.Panel(self.actions_splitter)
        #             .
        self.actions_splitter.SplitVertically(listActions_panel, self.selectedAction_panel, 250)
        #     .
        main_splitterWindow.SplitHorizontally(files_panel, actions_panel, 200)
    
    
    def setSelectedActionPanel(self, newPanel):
        '''
        Spéficier le panel de l'action sélectionnée
        @param newPanel: Panel
        @author: Julien
        '''
        oldPanel = self.selectedAction_panel
        self.actions_splitter.ReplaceWindow(oldPanel, newPanel)
        self.selectedAction_panel = newPanel
        oldPanel.Destroy()



class Controller(object):
    '''
    Controlleur
    @author: Julien
    '''
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        self.execute_thread = None
        
        self.model = Model()
        self.view = View()
        
        # Binding de la vue
        self.view.Bind(event=wx.EVT_CLOSE, handler=self.OnClose)
        # Binding des éléments de la vue
        #     Menu
        self.view.Bind(wx.EVT_MENU, self.OnOpen, self.view.menubar_fichier_ouvrir)
        self.view.Bind(wx.EVT_MENU, self.OnSave, self.view.menubar_fichier_enregistrer)
        self.view.Bind(wx.EVT_MENU,
                       lambda event:
                           self._saveAs(),
                       self.view.menubar_fichier_enregistrerSous)
        self.view.Bind(wx.EVT_MENU,
                       lambda event:
                           self.view.Close(),
                       self.view.menubar_fichier_quitter)
        #     Barre d'outils principale
        #self.view.Bind(wx.EVT_TOOL,
        #               lambda event:
        #                   self.view.Close(),
        #               self.view.exit_tool)
        self.view.Bind(wx.EVT_TOOL, self.test, self.view.exit_tool)
        #     Barre d'outils de la liste des fichiers
        self.view.Bind(wx.EVT_TOOL, self.OnAddFiles, self.view.addFile_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnAddFolder, self.view.addFolder_tool)
        self.view.Bind(wx.EVT_TOOL,
                       lambda event:
                           self.removeSelectedListFiles(),
                       self.view.removeSelectedListFiles_tool)
        self.view.Bind(wx.EVT_TOOL,
                       lambda event:
                           self.model.removeAllFiles(),
                       self.view.removeAllListFiles_tool)
        #     Barre d'outils de la liste des actions
        self.view.Bind(wx.EVT_LISTBOX,
                       lambda event:
                           self._refreshSelectedActionGui(),
                       self.view.listActionsToDo_listBox)
        self.view.Bind(wx.EVT_TOOL, self.OnAddAction, self.view.addAction_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnRemoveSelectedAction, self.view.removeSelectedAction_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnRemoveAllActions, self.view.removeAllActions_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnUpSelectedAction, self.view.upSelectedAction_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnDownSelectedAction, self.view.downSelectedAction_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnExecuteActions, self.view.executeActions_tool)
        self.view.Bind(wx.EVT_TOOL,
                       lambda event:
                           self.model.stop(),
                       self.view.stopActions_tool)
        # Événements du modèle
        Publisher.subscribe(self.Error, Model.ERROR)
        Publisher.subscribe(self.RefreshFilelist, Model.FILELIST_CHANGED)
        Publisher.subscribe(self.RefreshActionlist, Model.ACTIONLIST_CHANGED)
        Publisher.subscribe(self.RefreshFilelist, ActionGui.ACTION_CHANGED)
        
        self.view.Show()
        
        # DEBUG
        self.model.AddAction(CaseChange())
        self.model.AddAction(ReplaceString())
        self.model.AddAction(Cut())
        self.model.AddAction(InsertString())
    
    
    def test(self, event):
        self.model.save(Path("C:\\Users\\Julien\\Desktop\\toto.xml"))
    
    # Erreur
    
    def Error(self, err):
        '''
        Erreur dans l'application
        @param err: Erreur
        @author: Julien
        '''
        print err
    
    # Ouvrir ou Enregistrer les actions
    
    def OnOpen(self, event):
        '''
        Clic sur le bouton "Ouvrir" du menu
        @param event: Événement
        @todo: Implémenter
        @author: Julien
        '''
        fDialog = wx.FileDialog(self.view, "Enregistrer sous", wildcard="Fichiers XML (*.xml)|*.xml|Fichiers texte (*.txt)|*.txt|Tous les fichiers (*.*)|*.*", style=wx.FD_OPEN)
        if fDialog.ShowModal() != wx.ID_OK:
            return
        strPath = fDialog.GetPath()
        path = Path(strPath)
        self.model.open(path)
    
    
    def _saveAs(self):
        '''
        "Enregistrer sous..."
        Ouvrir la fenêtre d'exploration
        @author: Julien
        '''
        if self.model.filesave is None:
            filename = ""
        else:
            filename = self.model.filesave.filename
        fDialog = wx.FileDialog(self.view, "Enregistrer sous", defaultFile=filename, wildcard="Fichiers XML (*.xml)|*.xml|Fichiers texte (*.txt)|*.txt|Tous les fichiers (*.*)|*.*", style=wx.FD_SAVE)
        if fDialog.ShowModal() != wx.ID_OK:
            return
        strPath = fDialog.GetPath()
        if os.path.isfile(strPath):
            mDialog = wx.MessageDialog(self.view, strPath+"existe déjà.\nVoulez-vous le remplacer ?", "Confirmer l'enregistrement", wx.YES_NO|wx.NO_DEFAULT|wx.ICON_EXCLAMATION)
            if mDialog.ShowModal() != wx.YES:
                return
        path = Path(strPath)
        self.model.save(path)
    
    
    def OnSave(self, event):
        '''
        Clic sur le bouton "Enregistrer" du menu
        @param event: Événement
        @todo: Implémenter
        @author: Julien
        '''
        if self.model.filesave is None:
            self._saveAs()
        else:
            path = self.model.filesave
            self.model.save(path)
    
    # Manipulation des fichiers
    
    def OnAddFiles(self, event):
        '''
        Clic sur le bouton "Ajouter des fichiers"
        @param event: Événement
        @author: Julien
        '''
        fDialog = wx.FileDialog(self.view, "Sélectionnez les fichiers", style=wx.FD_MULTIPLE)
        if fDialog.ShowModal() != wx.ID_OK:
            return
        pathlist = []
        for strPath in fDialog.GetPaths():
            path = Path(strPath)
            pathlist.append(path)
        self.model.addFiles(pathlist)
    
    
    def OnAddFolder(self, event):
        '''
        Clic sur le bouton "Ajouter un répertoire"
        @param event: Événement
        @author: Julien
        '''
        dDialog = wx.DirDialog(self.view, "Répertoire source", style=wx.DD_DEFAULT_STYLE|wx.DD_DIR_MUST_EXIST)
        if dDialog.ShowModal() != wx.ID_OK:
            return
        path = dDialog.GetPath()
        self.model.addFolder(path)
    
    
    def removeSelectedListFiles(self):
        '''
        Clic sur le bouton "Supprimer les fichiers sélectionnés"
        @todo: Utiliser les index de ligne plutôt que de faire os.path.join(direname, basename)
        @author: Julien
        '''
        pathlist = []
        index = self.view.listFiles_listCtrl.GetFirstSelected()
        while index != -1:
            direname = self.view.listFiles_listCtrl.GetItem(index, 0).GetText()
            basename = self.view.listFiles_listCtrl.GetItem(index, 1).GetText()
            strPath = os.path.join(direname, basename)
            path = Path(strPath)
            pathlist.append(path)
            index = self.view.listFiles_listCtrl.GetNextSelected(index)
        self.model.removeFiles(pathlist)
    
    
    # Manipulation des actions
    
    def _onAddAction(self, event, action):
        '''
        Clic sur un sous-menu du bouton "Ajouter une action"
        @param event: Événement
        @param action: Action
        @author: Julien
        '''
        lastIndex = self.view.listActionsToDo_listBox.Count
        self.model.AddAction(action)
        self.view.listActionsToDo_listBox.Selection = lastIndex
        self._refreshSelectedActionGui()
    
    
    def OnAddAction(self, event):
        '''
        Clic sur le bouton "Ajouter une action"
        @param event: Événement
        @author: Julien
        '''
        menu = wx.Menu()
        for actionClass in actions:
            menuItem = wx.MenuItem(menu, wx.NewId(), actionClass.getTitle())
            self.view.Bind(wx.EVT_MENU,
                           lambda event, actionClass=actionClass:
                               self._onAddAction(event, actionClass()),
                           menuItem)
            menu.AppendItem(menuItem)
        self.view.PopupMenu(menu)
    
    
    def OnRemoveSelectedAction(self, event):
        '''
        Clic sur le bouton "Supprimer l'action sélectionnée"
        @param event: Événement
        @author: Julien
        '''
        index = self.view.listActionsToDo_listBox.GetSelection()
        if index == -1:
            return
        action = self.model.actionlist[index]
        self.model.removeAction(action)
        # Sélectionner le précédent
        if self.view.listActionsToDo_listBox.Count != 0:
            self.view.listActionsToDo_listBox.Selection = max(0, index-1)
        self._refreshSelectedActionGui()
    
    
    def OnRemoveAllActions(self, event):
        '''
        Clic sur le bouton "Supprimer toutes les actions"
        @param event: Événement
        @author: Julien
        '''
        self.model.removeAllActions()
        self._refreshSelectedActionGui()
    
    
    def OnUpSelectedAction(self, event):
        '''
        Clic sur le bouton "Monter l'action sélectionnée"
        @param event: Événement
        @author: Julien
        '''
        index = self.view.listActionsToDo_listBox.GetSelection()
        if index == -1:
            return
        if index != 0:
            self.model.SwapActions(index, index-1)
            self.view.listActionsToDo_listBox.Selection = index-1
        
    
    
    def OnDownSelectedAction(self, event):
        '''
        Clic sur le bouton "Descendre l'action sélectionnée"
        @param event: Événement
        @author: Julien
        '''
        index = self.view.listActionsToDo_listBox.GetSelection()
        if index == -1:
            return
        if index != self.view.listActionsToDo_listBox.Count-1:
            self.model.SwapActions(index, index+1)
            self.view.listActionsToDo_listBox.Selection = index+1
    
    # Exécution
    
    def _onExecuteActions(self):
        '''
        Thread d'exécution
        @author: Julien
        '''
        try:
            self.model.Execute()
        except:
            pass
        finally:
            self.execute_thread = None
    
    
    def OnExecuteActions(self, event):
        '''
        Exécuter les actions sur les fichiers
        @param event: Événement
        @author: Julien
        '''
        if self.execute_thread is not None:
            return
        self.execute_thread = threading.Thread(target=self._onExecuteActions, name="Exécution")
        self.execute_thread.run()
    
    
    # Affichage des éléments
    
    def RefreshFilelist(self):
        '''
        Rafraichir la liste des fichiers
        @param event: Événement
        @author: Julien
        '''
        self.view.listFiles_listCtrl.DeleteAllItems()
        files = self.model.filelist
        overviews = self.model.getOverviewFilelist()
        for i in xrange(0, len(files)):
            index = self.view.listFiles_listCtrl.GetItemCount()
            self.view.listFiles_listCtrl.InsertStringItem(index, label=files[i].dirname)
            self.view.listFiles_listCtrl.SetStringItem(index, 1, files[i].basename)
            self.view.listFiles_listCtrl.SetStringItem(index, 2, overviews[i].basename)
    
    
    def RefreshActionlist(self):
        '''
        Rafraichir la liste des actions
        @author: Julien
        '''
        # Liste des actions
        while self.view.listActionsToDo_listBox.Count != 0:
            self.view.listActionsToDo_listBox.Delete(0)
        for action in self.model.actionlist:
            index = self.view.listActionsToDo_listBox.Count
            self.view.listActionsToDo_listBox.Insert(action.__class__.getTitle(), index)
        # Liste des fichiers
        self.RefreshFilelist()
    
    
    def _refreshSelectedActionGui(self):
        '''
        Afficher l'action
        @param index: Index
        @author: Julien
        '''
        index = self.view.listActionsToDo_listBox.Selection
        if index == -1:
            newActionGui = wx.Panel(self.view.actions_splitter)
        else:
            action = self.model.actionlist[index]
            newActionGui = createGui(self.view.actions_splitter, action)
        self.view.setSelectedActionPanel(newActionGui)
    
    # Événements de la vue
    
    def OnClose(self, event):
        '''
        Quitter
        @param event: Événement
        @author: Julien
        '''
        if self.execute_thread is not None:
            return
        event.Skip()



if __name__ == '__main__':
    app = wx.App(False)
    controller = Controller()
    app.MainLoop()
