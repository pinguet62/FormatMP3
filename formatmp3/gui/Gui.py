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
from formatmp3.action.Action import *
from formatmp3.gui.ActionGui import *


FILELIST_CHANGED = "FILELIST_CHANGED"
ACTIONLIST_CHANGED = "ACTIONLIST_CHANGED"

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
    
    
    #def AddFile(self, path):
    #    '''
    #    Ajouter un fichier
    #    @param path: Chemin du fichier
    #    @author: Julien
    #    '''
    #    if path not in self.filelist:
    #        self.filelist.append(path)
    #        self.filelist.sort()
    #        Publisher.sendMessage(FILELIST_CHANGED)
    
    
    def AddFiles(self, pathlist=[]):
        '''
        Ajouter des fichiers
        @param pathlist: Liste des chemins des fichiers
        @author: Julien
        '''
        filesAdded = False
        for path in pathlist:
            if path not in self.filelist:
                self.filelist.append(path)
                filesAdded = True
        if filesAdded:
            self.filelist.sort()
            Publisher.sendMessage(FILELIST_CHANGED)
    
    
    def _addFolder(self, dirname):
        '''
        Ajout de chacun des fichiers contenus dans le répertoire de manière récursive
        @param dirname: Chemin du répertoire
        @author: Julien
        '''
        for basename in os.listdir(dirname):
            path = os.path.join(dirname, basename)
            if os.path.isdir(path):
                self._addFolder(path)
            elif os.path.isfile(path):
                if path not in self.filelist:
                    self.filelist.append(path)
    
    
    def AddFolder(self, path):
        '''
        Ajouter un répertoire
        @param path: Chemin du répertoire
        @author: Julien
        '''
        oldCount = len(self.filelist)
        self._addFolder(path)
        newCount = len(self.filelist)
        if oldCount < newCount:
            self.filelist.sort()
            Publisher.sendMessage(FILELIST_CHANGED)
    
    
    #def RemoveFile(self, path):
    #    '''
    #    Retirer un fichier
    #    @param path: Chemin du fichier
    #    @author: Julien
    #    '''
    #    if path in self.filelist:
    #        self.filelist.remove(path)
    #        Publisher.sendMessage(FILELIST_CHANGED)
    
    
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
        if self.filelist != []:
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
        minSize = (600,600)
        wx.Frame.__init__(self, None, title="FormatMP3 - Formatez vos fichiers MP3 en un clic !", size=minSize)
        self.SetMinSize(minSize)
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
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(mainSizer)
        #     Splitter
        splitter = wx.SplitterWindow(self, style=wx.SP_3D|wx.SP_NO_XP_THEME)
        mainSizer.Add(splitter, 1, wx.ALL|wx.EXPAND)
        #         Fichiers à modifier
        listFiles_panel = wx.Panel(splitter)
        listFiles_boxSizer = wx.BoxSizer(wx.VERTICAL)
        listFiles_panel.SetSizer(listFiles_boxSizer)
        #             Titre
        listFiles_title_staticText = wx.StaticText(listFiles_panel, label="Fichiers à modifier")
        listFiles_title_font = wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString)
        listFiles_title_staticText.SetFont(listFiles_title_font)
        listFiles_boxSizer.Add(listFiles_title_staticText, flag=wx.ALL, border=5)
        #             Barre d'outils
        listFiles_toolbar = wx.ToolBar(listFiles_panel, style=wx.TB_FLAT|wx.TB_TEXT)
        listFiles_boxSizer.Add(listFiles_toolbar, flag=wx.EXPAND)
        #                 Ajouter un fichier
        addFile_image = wx.Image("icons/add_file.png")
        addFile_image.Rescale(16,16)
        addFile_bitmap = wx.BitmapFromImage(addFile_image)
        self.addFile_tool = listFiles_toolbar.AddLabelTool(wx.ID_ANY, label="Ajouter fichier", bitmap=addFile_bitmap, shortHelp="Ajouter un fichier dans la liste")
        #                 Ajouter un répertoire
        addFolder_image = wx.Image("icons/add_folder.png")
        addFolder_image.Rescale(16,16)
        addFolder_bitmap = wx.BitmapFromImage(addFolder_image)
        self.addFolder_tool = listFiles_toolbar.AddLabelTool(wx.ID_ANY, label="Ajouter répertoire", bitmap=addFolder_bitmap, shortHelp="Ajouter un répertoire dans la liste")
        #             .
        listFiles_toolbar.AddSeparator()
        #                 Supprimer la sélection
        removeSelectedListFiles_image = wx.Image("icons/remove_selected.png")
        removeSelectedListFiles_image.Rescale(16,16)
        removeSelectedListFiles_bitmap = wx.BitmapFromImage(removeSelectedListFiles_image)
        self.removeSelectedListFiles_tool = listFiles_toolbar.AddLabelTool(wx.ID_ANY, label="Supp. sélection", bitmap=removeSelectedListFiles_bitmap, shortHelp="Supprimer les fichiers sélectionnés de la liste")
        #                 Supprimer tout
        removeAllListFiles_image = wx.Image("icons/remove_all.png")
        removeAllListFiles_image.Rescale(16,16)
        removeAllListFiles_bitmap = wx.BitmapFromImage(removeAllListFiles_image)
        self.removeAllListFiles_tool = listFiles_toolbar.AddLabelTool(wx.ID_ANY, label="Supp. tout", bitmap=removeAllListFiles_bitmap, shortHelp="Supprimer tous les fichiers de la liste")
        #             .
        listFiles_toolbar.Realize()
        #             Liste
        self.listFiles_listCtrl = wx.ListCtrl(listFiles_panel, style=wx.LC_REPORT)
        self.listFiles_listCtrl.InsertColumn(0, "Dossier", width=200)
        self.listFiles_listCtrl.InsertColumn(1, "Nom d'origine", width=125)
        self.listFiles_listCtrl.InsertColumn(2, "Nouveau nom", width=125)
        listFiles_boxSizer.Add(self.listFiles_listCtrl, 1, wx.ALL|wx.EXPAND, 5)
        #         Liste des actions
        self.listActions_panel = wx.Panel(splitter)
        self.listActions_boxSizer = wx.BoxSizer(wx.VERTICAL)
        self.listActions_panel.SetSizer(self.listActions_boxSizer)
        #             Titre
        listActions_title_staticText = wx.StaticText(self.listActions_panel, label="Actions à réaliser")
        listActions_title_font = wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString)
        listActions_title_staticText.SetFont(listActions_title_font)
        self.listActions_boxSizer.Add(listActions_title_staticText, flag=wx.ALL, border=5)
        #             Barre d'outils
        listActions_toolbar = wx.ToolBar(self.listActions_panel, style=wx.TB_FLAT|wx.TB_TEXT)
        self.listActions_boxSizer.Add(listActions_toolbar, flag=wx.EXPAND)
        #                 Ajouter
        addAction_image = wx.Image("icons/add.png")
        addAction_image.Rescale(16,16)
        addAction_bitmap = wx.BitmapFromImage(addAction_image)
        self.addAction_tool = listActions_toolbar.AddLabelTool(wx.ID_ANY, label="Ajouter", bitmap=addAction_bitmap, shortHelp="Ajouter une action à la liste")
        #             .
        listActions_toolbar.AddSeparator()
        #                 Supprimer la sélection
        removeSelectedAction_image = wx.Image("icons/remove_selected.png")
        removeSelectedAction_image.Rescale(16,16)
        removeSelectedAction_bitmap = wx.BitmapFromImage(removeSelectedAction_image)
        self.removeSelectedAction_tool = listActions_toolbar.AddLabelTool(wx.ID_ANY, label="Supp. sélection", bitmap=removeSelectedAction_bitmap, shortHelp="Supprimer l'action sélectionné de la liste")
        #                 Supprimer tout
        removeAllActions_image = wx.Image("icons/remove_all.png")
        removeAllActions_image.Rescale(16,16)
        removeAllActions_bitmap = wx.BitmapFromImage(removeAllActions_image)
        self.removeAllActions_tool = listActions_toolbar.AddLabelTool(wx.ID_ANY, label="Supp. tout", bitmap=removeAllActions_bitmap, shortHelp="Supprimer toutes les actions de la liste")
        #             .
        listActions_toolbar.AddSeparator()
        #                 Monter l'action
        upSelectedAction_image = wx.Image("icons/up.png")
        upSelectedAction_image.Rescale(16,16)
        upSelectedAction_bitmap = wx.BitmapFromImage(upSelectedAction_image)
        self.upSelectedAction_tool = listActions_toolbar.AddLabelTool(wx.ID_ANY, label="Monter", bitmap=upSelectedAction_bitmap, shortHelp="Monter l'action sélectionnée dans la liste")
        #                 Descendre l'action
        downSelectedAction_image = wx.Image("icons/down.png")
        downSelectedAction_image.Rescale(16,16)
        downSelectedAction_bitmap = wx.BitmapFromImage(downSelectedAction_image)
        self.downSelectedAction_tool = listActions_toolbar.AddLabelTool(wx.ID_ANY, label="Descendre", bitmap=downSelectedAction_bitmap, shortHelp="Descendre l'action sélectionnée dans la liste")
        #             .
        listActions_toolbar.Realize()
        #             Liste
        self.listActionsToDo_listBox = wx.ListBox(self.listActions_panel)
        self.listActions_boxSizer.Add(self.listActionsToDo_listBox, 1, wx.ALL|wx.EXPAND, 5)
        #             Paramètres
        self.selectedAction_panel = wx.Panel(self.listActions_panel, size=wx.Size(-1,50), style=wx.TAB_TRAVERSAL)
        self.listActions_boxSizer.Add(self.selectedAction_panel, flag=wx.ALL|wx.EXPAND, border=5)
        #     .
        splitter.SplitHorizontally(listFiles_panel, self.listActions_panel, 150) # TODO: Proportion initiale



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
        # Événements du modèle
        Publisher.subscribe(self._filelistChanged, FILELIST_CHANGED)
        Publisher.subscribe(self._actionlistChanged, ACTIONLIST_CHANGED)
        
        self.view.Show()
        
        self.model.AddAction(CaseChange())
        self.model.AddAction(ReplaceString())
        self.model.AddAction(Cut())
        self.model.AddAction(InsertString())
    
    
    def OnAddFiles(self, event):
        '''
        Clic sur le bouton "Ajouter des fichiers"
        @param event: Événement
        @author: Julien
        @todo: Répertoire par défaut
        '''
        print "OnAddFiles"
        fDialog = wx.FileDialog(self.view, "Sélectionnez les fichiers", style=wx.FD_MULTIPLE)
        if fDialog.ShowModal() != wx.ID_OK :
            return
        pathlist = []
        direname = fDialog.GetDirectory()
        for basename in fDialog.GetFilenames():
            path = os.path.join(direname, basename)
            pathlist.append(path)
        self.model.AddFiles(pathlist)
        event.Skip()
    
    
    def OnAddFolder(self, event):
        '''
        Clic sur le bouton "Ajouter un répertoire"
        @param event: Événement
        @author: Julien
        '''
        print "OnAddFolder"
        dDialog = wx.DirDialog(self.view, "Répertoire source", style=wx.DD_DEFAULT_STYLE|wx.DD_DIR_MUST_EXIST)
        if dDialog.ShowModal() != wx.ID_OK :
            return
        path = dDialog.GetPath()
        self.model.AddFolder(path)
        event.Skip()
    
    
    def OnRemoveSelectedListFiles(self, event):
        '''
        Clic sur le bouton "Supprimer les fichiers sélectionnés"
        @param event: Événement
        @author: Julien
        '''
        print "OnRemoveSelectedListFiles"
        pathlist = []
        index = self.view.listFiles_listCtrl.GetFirstSelected()
        while index != -1:
            direname = self.view.listFiles_listCtrl.GetItem(index, 0).GetText()
            basename = self.view.listFiles_listCtrl.GetItem(index, 1).GetText()
            path = os.path.join(direname, basename)
            pathlist.append(path)
            index = self.view.listFiles_listCtrl.GetNextSelected(index)
        self.model.RemoveFiles(pathlist)
        event.Skip()
    
    
    def OnRemoveAllListFiles(self, event):
        '''
        Clic sur le bouton "Supprimer tous les fichiers"
        @param event: Événement
        @author: Julien
        '''
        print "OnRemoveAllListFiles"
        self.model.RemoveAllFiles()
        event.Skip()
        
    
    def _filelistChanged(self):
        '''
        Rafraichir la liste des fichiers
        @param event: Événement
        @author: Julien
        '''
        print "_filelistChanged"
        self.view.listFiles_listCtrl.DeleteAllItems()
        for path in self.model.filelist:
            (head, tail) = os.path.split(path)
            index = self.view.listFiles_listCtrl.GetItemCount()
            self.view.listFiles_listCtrl.InsertStringItem(index, label=head)
            self.view.listFiles_listCtrl.SetStringItem(index, 1, tail)
            self.view.listFiles_listCtrl.SetStringItem(index, 2, "TODO")
    
    
    def OnSelectedAction(self, event):
        '''
        Sélection d'une action dans la liste
        @param event: Événement
        @author: Julien
        '''
        print "OnSelectedAction"
        index = self.view.listActionsToDo_listBox.Selection
        self._showAction(index)
    
    
    def _onAddAction(self, event, action):
        '''
        Clic sur un sous-menu du bouton "Ajouter une action"
        @param event: Événement
        @param action: Action
        @author: Julien
        @todo: Implémenter
        '''
        print "_onAddAction"
        lastIndex = self.view.listActionsToDo_listBox.Count
        self.model.AddAction(action)
        self.view.listActionsToDo_listBox.Selection = lastIndex
        self._showAction(lastIndex)
    
    
    def OnAddAction(self, event):
        '''
        Clic sur le bouton "Ajouter une action"
        @param event: Événement
        @author: Julien
        @todo: Implémenter
        '''
        print "OnAddAction"
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
        @todo: Implémenter
        '''
        print "OnRemoveSelectedAction"
    
    
    def OnRemoveAllActions(self, event):
        '''
        Clic sur le bouton "Supprimer toutes les actions"
        @param event: Événement
        @author: Julien
        @todo: Implémenter
        '''
        print "OnRemoveAllActions"
    
    
    def OnUpSelectedAction(self, event):
        '''
        Clic sur le bouton "Monter l'action sélectionnée"
        @param event: Événement
        @author: Julien
        @todo: Implémenter
        '''
        print "OnUpSelectedAction"
    
    
    def OnDownSelectedAction(self, event):
        '''
        Clic sur le bouton "Descendre l'action sélectionnée"
        @param event: Événement
        @author: Julien
        @todo: Implémenter
        '''
        print "OnDownSelectedAction"
    
    
    def _actionlistChanged(self):
        '''
        Rafraichir la liste des actions
        @author: Julien
        '''
        print "_actionlistChanged"
        while self.view.listActionsToDo_listBox.Count != 0:
            self.view.listActionsToDo_listBox.Delete(0)
        for action in self.model.actionlist:
            index = self.view.listActionsToDo_listBox.Count
            self.view.listActionsToDo_listBox.Insert(action.__class__.getTitle(), index)
    
    
    def _showAction(self, index):
        '''
        Afficher l'action
        @param index: Index
        @author: Julien
        '''
        print "_showAction"
        action = self.model.actionlist[index]
        newActionGui = createGui(self.view.listActions_panel, action)
        oldActionGui = self.view.selectedAction_panel
        self.view.listActions_boxSizer.Replace(oldActionGui, newActionGui)
        self.view.selectedAction_panel = newActionGui
        oldActionGui.Destroy()
        self.view.listActions_boxSizer.Layout()
    
    
    def OnTest(self, event):
        print "OnTest"
        
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