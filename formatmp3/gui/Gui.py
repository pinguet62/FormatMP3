#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Interface graphique de l'application
@author: Julien
@todo: Log
@todo: Hauteur max des paramètres, ou scrollbar
'''



import os.path
import wx
from wx.lib.pubsub import pub as Publisher
from formatmp3.actions.Action import *
from formatmp3.gui.ActionGui import *



# Messages de l'interface graphique
FILELIST_CHANGED = "FILELIST_CHANGED"
ACTIONLIST_CHANGED = "ACTIONLIST_CHANGED"



# Liste des actions de l'application
actions = [CaseChange, ReplaceString, Cut, InsertString]



class Model(object):
    '''
    Données de l'application
    Contient les fichiers à modifier ainsi que les actions à effectuer
    @author: Julien
    '''
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        self.filelist = []
        self.actionlist = []
    
    
    def _addFile(self, path):
        '''
        Ajouter un fichier
        @param path: path
        @author: Julien
        '''
        if path not in self.filelist:
            self.filelist.append(path)
    
    
    def AddFile(self, path):
        '''
        Ajouter un fichier
        @param path: path
        @author: Julien
        '''
        oldCount = len(self.filelist)
        self._addFile(path)
        newCount = len(self.filelist)
        if oldCount < newCount:
            self.filelist.sort()
            Publisher.sendMessage(FILELIST_CHANGED)
    
    
    def AddFiles(self, pathlist=[]):
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
            Publisher.sendMessage(FILELIST_CHANGED)
    
    
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
    
    
    def AddFolder(self, path):
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
            Publisher.sendMessage(FILELIST_CHANGED)
    
    
    def RemoveFiles(self, pathlist=[]):
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
            Publisher.sendMessage(FILELIST_CHANGED)
    
    
    def RemoveAllFiles(self):
        '''
        Retirer tous les fichiers
        @author: Julien
        '''
        if self.filelist:
            self.filelist = []
            Publisher.sendMessage(FILELIST_CHANGED)
    
    
    def AddAction(self, action):
        '''
        Ajouter une action
        @param action: Action
        @author: Julien
        '''
        self.actionlist.append(action)
        Publisher.sendMessage(ACTIONLIST_CHANGED)
    
    
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
        @param i1: Indice
        @param i2: Indice
        @author: Julien
        '''
        self.actionlist[i1], self.actionlist[i2] = self.actionlist[i2], self.actionlist[i1]
        Publisher.sendMessage(ACTIONLIST_CHANGED)
    
    
    def RemoveAction(self, action):
        '''
        Retirer des fichiers
        @param action: Action
        @author: Julien
        '''
        if action in self.actionlist:
            self.actionlist.remove(action)
            Publisher.sendMessage(ACTIONLIST_CHANGED)
    
    
    def RemoveAllActions(self):
        '''
        Retirer toutes les actions
        @author: Julien
        '''
        if self.actionlist:
            self.actionlist = []
            Publisher.sendMessage(ACTIONLIST_CHANGED)
    
    
    def Execute(self):
        '''
        Exécuter les actions sur les fichiers
        @author: Julien
        '''
        for path in self.filelist:
            try:
                for action in self.actionlist:
                    action.execute(path)
            except BaseException, err:
                print err
        Publisher.sendMessage(FILELIST_CHANGED)



class View(wx.Frame):
    '''
    Fenêtre principale
    @author: Julien
    '''
    
    
    def __init__(self):
        '''
        Constructeur
        @param parent: Fenêtre parent
        @author: Julien
        '''
        # Fenêtre
        minSize = (600,700)
        wx.Frame.__init__(self, None, title="FormatMP3 - Formatez vos fichiers MP3 en un clic !", size=minSize)
        #self.SetMinSize(minSize)
        self.CenterOnScreen()
        
        # Barre de menus
        menubar = wx.MenuBar(0)
        self.SetMenuBar(menubar)
        #     Fichier
        menubar_fichier = wx.Menu()
        menubar.Append(menubar_fichier, "&Fichier")
        #         Quitter
        menubar_fichier_quitter = wx.MenuItem(menubar_fichier, wx.ID_ANY, "&Quitter\tAlt-F4")
        menubar_fichier.AppendItem(menubar_fichier_quitter)
        #     Aide
        menubar_aide = wx.Menu()
        menubar.Append(menubar_aide, "&?")
        #         A propos
        menubar_aide_aPropos = wx.MenuItem(menubar_aide, wx.ID_ANY, "A &propos de FormatMP3")
        menubar_aide.AppendItem(menubar_aide_aPropos)
        
        # Barre d'outils
        toolBar = self.CreateToolBar()
        #     Quitter
        self.quitter_tool = toolBar.AddLabelTool(wx.ID_ANY, "Quitter", wx.Bitmap('icons/exit.png'))
        # .
        toolBar.Realize()
        
        # Barre de statut
        statusBar = self.CreateStatusBar()
        
        # Sizer
        main_boxSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(main_boxSizer)
        #     Splitter
        main_splitterWindow = wx.SplitterWindow(self, style=wx.SP_3D|wx.SP_NO_XP_THEME)
        main_boxSizer.Add(main_splitterWindow, 1, wx.ALL|wx.EXPAND)
        #         Fichiers à modifier
        files_panel = wx.Panel(main_splitterWindow)
        files_boxSizer = wx.BoxSizer(wx.VERTICAL)
        files_panel.SetSizer(files_boxSizer)
        #             Titre
        title_files_staticText = wx.StaticText(files_panel, label="Fichiers à modifier")
        title_files_font = wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString)
        title_files_staticText.SetFont(title_files_font)
        files_boxSizer.Add(title_files_staticText, flag=wx.ALL, border=5)
        #             Barre d'outils
        files_toolbar = wx.ToolBar(files_panel, style=wx.TB_FLAT|wx.TB_TEXT)
        files_boxSizer.Add(files_toolbar, flag=wx.EXPAND)
        #                 Ajouter un fichier
        addFile_image = wx.Image("icons/add_file.png")
        addFile_image.Rescale(16,16)
        addFile_bitmap = wx.BitmapFromImage(addFile_image)
        self.addFile_tool = files_toolbar.AddLabelTool(wx.ID_ANY, label="Ajouter fichier", bitmap=addFile_bitmap, shortHelp="Ajouter un fichier dans la liste")
        #                 Ajouter un répertoire
        addFolder_image = wx.Image("icons/add_folder.png")
        addFolder_image.Rescale(16,16)
        addFolder_bitmap = wx.BitmapFromImage(addFolder_image)
        self.addFolder_tool = files_toolbar.AddLabelTool(wx.ID_ANY, label="Ajouter répertoire", bitmap=addFolder_bitmap, shortHelp="Ajouter un répertoire dans la liste")
        #             .
        files_toolbar.AddSeparator()
        #                 Supprimer la sélection
        removeSelectedListFiles_image = wx.Image("icons/remove_selected.png")
        removeSelectedListFiles_image.Rescale(16,16)
        removeSelectedListFiles_bitmap = wx.BitmapFromImage(removeSelectedListFiles_image)
        self.removeSelectedListFiles_tool = files_toolbar.AddLabelTool(wx.ID_ANY, label="Supp. sélection", bitmap=removeSelectedListFiles_bitmap, shortHelp="Supprimer les fichiers sélectionnés de la liste")
        #                 Supprimer tout
        removeAllListFiles_image = wx.Image("icons/remove_all.png")
        removeAllListFiles_image.Rescale(16,16)
        removeAllListFiles_bitmap = wx.BitmapFromImage(removeAllListFiles_image)
        self.removeAllListFiles_tool = files_toolbar.AddLabelTool(wx.ID_ANY, label="Supp. tout", bitmap=removeAllListFiles_bitmap, shortHelp="Supprimer tous les fichiers de la liste")
        #             .
        files_toolbar.Realize()
        #             Liste
        self.listFiles_listCtrl = wx.ListCtrl(files_panel, style=wx.LC_REPORT)
        self.listFiles_listCtrl.InsertColumn(0, "Dossier", width=200)
        self.listFiles_listCtrl.InsertColumn(1, "Nom d'origine", width=125)
        self.listFiles_listCtrl.InsertColumn(2, "Nouveau nom", width=125)
        files_boxSizer.Add(self.listFiles_listCtrl, 1, wx.ALL|wx.EXPAND, 5)
        #         Actions
        actions_panel = wx.Panel(main_splitterWindow)
        self.actions_boxSizer = wx.BoxSizer(wx.VERTICAL)
        actions_panel.SetSizer(self.actions_boxSizer)
        #             Titre
        title_actions_staticText = wx.StaticText(actions_panel, label="Actions à réaliser")
        title_actions_font = wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString)
        title_actions_staticText.SetFont(title_actions_font)
        self.actions_boxSizer.Add(title_actions_staticText, flag=wx.ALL, border=5)
        #             Barre d'outils
        actions_toolbar = wx.ToolBar(actions_panel, style=wx.TB_FLAT|wx.TB_TEXT)
        self.actions_boxSizer.Add(actions_toolbar, flag=wx.EXPAND)
        #                 Ajouter
        addAction_image = wx.Image("icons/add.png")
        addAction_image.Rescale(16,16)
        addAction_bitmap = wx.BitmapFromImage(addAction_image)
        self.addAction_tool = actions_toolbar.AddLabelTool(wx.ID_ANY, label="Ajouter", bitmap=addAction_bitmap, shortHelp="Ajouter une action à la liste")
        #             .
        actions_toolbar.AddSeparator()
        #                 Supprimer la sélection
        removeSelectedAction_image = wx.Image("icons/remove_selected.png")
        removeSelectedAction_image.Rescale(16,16)
        removeSelectedAction_bitmap = wx.BitmapFromImage(removeSelectedAction_image)
        self.removeSelectedAction_tool = actions_toolbar.AddLabelTool(wx.ID_ANY, label="Supp. sélection", bitmap=removeSelectedAction_bitmap, shortHelp="Supprimer l'action sélectionné de la liste")
        #                 Supprimer tout
        removeAllActions_image = wx.Image("icons/remove_all.png")
        removeAllActions_image.Rescale(16,16)
        removeAllActions_bitmap = wx.BitmapFromImage(removeAllActions_image)
        self.removeAllActions_tool = actions_toolbar.AddLabelTool(wx.ID_ANY, label="Supp. tout", bitmap=removeAllActions_bitmap, shortHelp="Supprimer toutes les actions de la liste")
        #             .
        actions_toolbar.AddSeparator()
        #                 Monter l'action
        upSelectedAction_image = wx.Image("icons/up.png")
        upSelectedAction_image.Rescale(16,16)
        upSelectedAction_bitmap = wx.BitmapFromImage(upSelectedAction_image)
        self.upSelectedAction_tool = actions_toolbar.AddLabelTool(wx.ID_ANY, label="Monter", bitmap=upSelectedAction_bitmap, shortHelp="Monter l'action sélectionnée dans la liste")
        #                 Descendre l'action
        downSelectedAction_image = wx.Image("icons/down.png")
        downSelectedAction_image.Rescale(16,16)
        downSelectedAction_bitmap = wx.BitmapFromImage(downSelectedAction_image)
        self.downSelectedAction_tool = actions_toolbar.AddLabelTool(wx.ID_ANY, label="Descendre", bitmap=downSelectedAction_bitmap, shortHelp="Descendre l'action sélectionnée dans la liste")
        #             .
        actions_toolbar.AddSeparator()
        #                 Exécuter
        executeActions_image = wx.Image("icons/execute.png")
        executeActions_image.Rescale(16,16)
        executeActions_bitmap = wx.BitmapFromImage(executeActions_image)
        self.executeActions_tool = actions_toolbar.AddLabelTool(wx.ID_ANY, label="Exécuter", bitmap=executeActions_bitmap, shortHelp="Exécuter les actions sur les fichiers")
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
    
    
    def hideSelectedAction(self):
        '''
        Effacer le panel de l'action sélectionnée
        @author: Julien
        '''
        self.setSelectedActionPanel(wx.Panel(self.actions_splitter))



class Controller(object):
    '''
    Controlleur de l'application
    @author: Julien
    '''
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        self.model = Model()
        
        self.view = View()
        # Bindings
        #     Barre d'outils principale
        self.view.Bind(wx.EVT_TOOL, self.OnTest, self.view.quitter_tool)
        #     Barre d'outils de la liste des fichiers
        self.view.Bind(wx.EVT_TOOL, self.OnAddFiles, self.view.addFile_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnAddFolder, self.view.addFolder_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnRemoveSelectedListFiles, self.view.removeSelectedListFiles_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnRemoveAllListFiles, self.view.removeAllListFiles_tool)
        #     Barre d'outils de la liste des actions
        self.view.Bind(wx.EVT_LISTBOX, self.OnSelectedAction, self.view.listActionsToDo_listBox)
        self.view.Bind(wx.EVT_TOOL, self.OnAddAction, self.view.addAction_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnRemoveSelectedAction, self.view.removeSelectedAction_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnRemoveAllActions, self.view.removeAllActions_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnUpSelectedAction, self.view.upSelectedAction_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnDownSelectedAction, self.view.downSelectedAction_tool)
        self.view.Bind(wx.EVT_TOOL, self.OnExecuteActions, self.view.executeActions_tool)
        # Événements
        Publisher.subscribe(self.RefreshFilelist, FILELIST_CHANGED)
        Publisher.subscribe(self.RefreshActionlist, ACTIONLIST_CHANGED)
        Publisher.subscribe(self.RefreshFilelist, ACTION_CHANGED)
        
        self.view.Show()
        
        self.model.AddAction(CaseChange())
        self.model.AddAction(ReplaceString())
        self.model.AddAction(Cut())
        self.model.AddAction(InsertString())
    
    # Manipulation des fichiers
    
    def OnAddFiles(self, event):
        '''
        Clic sur le bouton "Ajouter des fichiers"
        @param event: Événement
        @author: Julien
        @todo: Répertoire par défaut
        '''
        fDialog = wx.FileDialog(self.view, "Sélectionnez les fichiers", style=wx.FD_MULTIPLE)
        if fDialog.ShowModal() != wx.ID_OK:
            return
        pathlist = []
        direname = fDialog.GetDirectory()
        for basename in fDialog.GetFilenames():
            strPath = os.path.join(direname, basename)
            path = Path(strPath)
            pathlist.append(path)
        self.model.AddFiles(pathlist)
    
    
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
        self.model.AddFolder(path)
    
    
    def OnRemoveSelectedListFiles(self, event):
        '''
        Clic sur le bouton "Supprimer les fichiers sélectionnés"
        @param event: Événement
        @author: Julien
        '''
        pathlist = []
        index = self.view.listFiles_listCtrl.GetFirstSelected()
        while index != -1:
            direname = self.view.listFiles_listCtrl.GetItem(index, 0).GetText()
            basename = self.view.listFiles_listCtrl.GetItem(index, 1).GetText()
            path = os.path.join(direname, basename)
            pathlist.append(path)
            index = self.view.listFiles_listCtrl.GetNextSelected(index)
        self.model.RemoveFiles(pathlist)
    
    
    def OnRemoveAllListFiles(self, event):
        '''
        Clic sur le bouton "Supprimer tous les fichiers"
        @param event: Événement
        @author: Julien
        '''
        self.model.RemoveAllFiles()
    
    # Manipulation des actions
    
    def OnSelectedAction(self, event):
        '''
        Sélection d'une action dans la liste
        @param event: Événement
        @author: Julien
        '''
        index = self.view.listActionsToDo_listBox.Selection
        self._showActionGui(index)
        # Toolbar : monter/descendre action
        if index == 0:
            pass
        elif index == self.view.listActionsToDo_listBox.Count-1:
            pass
    
    
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
        self._showActionGui(lastIndex)
    
    
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
        self.model.RemoveAction(action)
        # Sélectionner le précédent
        if self.view.listActionsToDo_listBox.Count == 0:
            self.view.hideSelectedAction()
        else:
            if index == 0:
                self.view.listActionsToDo_listBox.Selection = 0
                self._showActionGui(0)
            else:
                self.view.listActionsToDo_listBox.Selection = index-1
                self._showActionGui(index-1)
    
    
    def OnRemoveAllActions(self, event):
        '''
        Clic sur le bouton "Supprimer toutes les actions"
        @param event: Événement
        @author: Julien
        '''
        self.model.RemoveAllActions()
        self.view.hideSelectedAction()
    
    
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
    
    
    def OnExecuteActions(self, event):
        '''
        Exécuter les actions sur les fichiers
        @param event: Événement
        @author: Julien
        '''
        self.model.Execute()
    
    
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
    
    
    def _showActionGui(self, index):
        '''
        Afficher l'action
        @param index: Index
        @author: Julien
        '''
        action = self.model.actionlist[index]
        newActionGui = createGui(self.view.actions_splitter, action)
        self.view.setSelectedActionPanel(newActionGui)
    
    
    def OnTest(self, event):
        list = [CaseChange]
        self.i = (self.i+1)%len(list)
        action = list[self.i]
        classAction = action.__name__
        classActionGui = classAction + "Gui"
        classActionGuiObj = eval(classActionGui)(self)
        print classActionGuiObj
        toto = InsertString
        



if __name__ == '__main__':
    app = wx.App(False)
    controller = Controller()
    app.MainLoop()