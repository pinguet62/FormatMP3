#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Controlleurs du pattern MVC
@author: Julien
'''



from Model import *
from View import *
from formatmp3.actions.Action import *
from formatmp3.gui.ActionGui import *
from wx.lib.pubsub import pub as Publisher
import os.path
import threading
import wx



class Controller(object):
    '''
    Controlleur de l'interface principale
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
        self.view.Bind(wx.EVT_MENU, self.OnSaveAs, self.view.menubar_fichier_enregistrerSous)
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
        self.view.Bind(wx.EVT_LISTBOX, self.OnSelectedAction, self.view.listActionsToDo_listBox)
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
        Publisher.subscribe(self.RefreshFilelist, ACTION_CHANGED)
        
        self.view.Show()
        
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
        fDialog = wx.FileDialog(self.view, "Enregistrer sous", wildcard="XML files (*.xml)|*.xml", style=wx.FD_OPEN)
        if fDialog.ShowModal() != wx.ID_OK:
            return
        strPath = os.path.join(fDialog.GetDirectory(), fDialog.GetFilename())
        path = Path(strPath)
        self.model.open(path)
    
    
    def OnSave(self, event):
        '''
        Clic sur le bouton "Enregistrer" du menu
        @param event: Événement
        @todo: Implémenter
        @author: Julien
        '''
        if self.model.filesave is None:
            fDialog = wx.FileDialog(self.view, "Enregistrer sous", wildcard="XML files (*.xml)|*.xml", style=wx.FD_SAVE)
            if fDialog.ShowModal() != wx.ID_OK:
                return
            strPath = os.path.join(fDialog.GetDirectory(), fDialog.GetFilename())
            path = Path(strPath)
        else:
            path = self.model.filesave
        self.model.save(path)
    
    
    def OnSaveAs(self, event):
        '''
        Clic sur le bouton "Enregistrer sous..." du menu
        @param event: Événement
        @author: Julien
        '''
        
        if self.model.filesave is None:
            filename = ""
        else:
            filename = self.model.filesave.filename
        fDialog = wx.FileDialog(self.view, "Enregistrer sous", defaultFile=filename, wildcard="XML files (*.xml)|*.xml", style=wx.FD_SAVE)
        if fDialog.ShowModal() != wx.ID_OK:
            return
        strPath = os.path.join(fDialog.GetDirectory(), fDialog.GetFilename())
        path = Path(strPath)
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
        direname = fDialog.GetDirectory()
        for basename in fDialog.GetFilenames():
            strPath = os.path.join(direname, basename)
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
        self.model.removeAction(action)
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
        self.model.removeAllActions()
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
    
    # Exécution
    
    def _onExecuteActions(self):
        '''
        Thread d'exécution
        @author: Julien
        '''
        try:
            self.model.Execute()
        except Exception, err:
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
    
    
    def _showActionGui(self, index):
        '''
        Afficher l'action
        @param index: Index
        @author: Julien
        '''
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