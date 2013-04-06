#!/usr/bin/python
# -*- coding: utf-8 -*-



import os.path
import wx



'''
Interface graphique de l'application
@author: Julien
'''



class MainFrame(wx.Frame):
    '''
    Fenêtre principale
    @author: Julien
    '''
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        # Fenêtre
        minSize = (500,500)
        wx.Frame.__init__ (self, parent=None, title="FormatMP3 - Formatez vos fichiers MP3 en un clic !", size=minSize)
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
        quitter_tool = toolBar.AddLabelTool(wx.ID_ANY, "Quitter", wx.Bitmap('icons/exit.png'))
        self.Bind(wx.EVT_TOOL, self.OnTest, quitter_tool)
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
        listFiles_header_title_staticText = wx.StaticText(listFiles_panel, label="Fichiers à modifier")
        listFiles_header_title_font = wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString)
        listFiles_header_title_staticText.SetFont(listFiles_header_title_font)
        listFiles_boxSizer.Add(listFiles_header_title_staticText, flag=wx.ALL, border=5)
        #             Barre d'outils
        listFiles_header_toolbar = wx.ToolBar(listFiles_panel, style=wx.TB_FLAT|wx.TB_HORZ_TEXT)
        listFiles_boxSizer.Add(listFiles_header_toolbar, flag=wx.EXPAND)
        #                 Ajouter un fichier
        addFile_tool = listFiles_header_toolbar.AddLabelTool(wx.ID_ANY, label="Ajouter un fichier", bitmap=wx.Bitmap(name="icons/add_file.png", type=wx.BITMAP_TYPE_PNG), shortHelp="Ajouter un fichier dans la liste")
        self.Bind(wx.EVT_TOOL, self.OnAddFile, addFile_tool)
        #                 Ajouter un répertoire
        addFolder_tool = listFiles_header_toolbar.AddLabelTool(wx.ID_ANY, label="Ajouter un répertoire", bitmap=wx.Bitmap(name="icons/add_folder.png", type=wx.BITMAP_TYPE_PNG), shortHelp="Ajouter un répertoire dans la liste")
        self.Bind(wx.EVT_TOOL, self.OnAddFolder, addFolder_tool)
        #                 Supprimer la sélection
        removeSelectedListFiles_tool = listFiles_header_toolbar.AddLabelTool(wx.ID_ANY, label="Supprimer la sélection", bitmap=wx.Bitmap(name="icons/delete.png", type=wx.BITMAP_TYPE_PNG), shortHelp="Supprimer les fichiers sélectionnés de la liste")
        self.Bind(wx.EVT_TOOL, self.OnRemoveSelectedListFiles, removeSelectedListFiles_tool)
        #             .
        listFiles_header_toolbar.Realize()
        #             Liste
        self.listFiles_listCtrl = wx.ListCtrl(listFiles_panel, style=wx.LC_REPORT)
        listFiles_boxSizer.Add(self.listFiles_listCtrl, 1, wx.ALL|wx.EXPAND, 5)
        self.listFiles_listCtrl.InsertColumn(0, "Dossier", width=200)
        self.listFiles_listCtrl.InsertColumn(1, "Nom d'origine", width=125)
        self.listFiles_listCtrl.InsertColumn(2, "Nouveau nom", width=125)
        #         Liste des actions
        listActions_panel = wx.Panel(splitter)
        listActions_boxSizer = wx.BoxSizer(wx.VERTICAL)
        listActions_panel.SetSizer(listActions_boxSizer)
        #             Titre
        listActions_title_staticText = wx.StaticText(listActions_panel, label="Actions à réaliser")
        listActions_title_font = wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString)
        listActions_title_staticText.SetFont(listActions_title_font)
        listActions_boxSizer.Add(listActions_title_staticText, flag=wx.ALL, border=5)
        #             Liste
        self.listActionsToDo_listBox = wx.ListBox(listActions_panel)
        listActions_boxSizer.Add(self.listActionsToDo_listBox, 1, wx.ALL|wx.EXPAND, 5)
        #             Nouvelle action ou action sélectionnée
        listActions_action_sizer = wx.BoxSizer()
        listActions_boxSizer.Add(listActions_action_sizer, flag=wx.ALL|wx.EXPAND)
        #                 Options
        listActions_options_sizer = wx.BoxSizer(wx.VERTICAL)
        listActions_action_sizer.Add(listActions_options_sizer, flag=wx.ALL)
        #                     Liste des actions disponibles
        self.listAvailableActions_choice = wx.Choice(listActions_panel)
        listActions_options_sizer.Add(self.listAvailableActions_choice, flag=wx.ALL, border=5)
        #                     Ajouter l'action choisie
        self.addChosenAction_button = wx.Button(listActions_panel, label="Ajouter")
        listActions_options_sizer.Add(self.addChosenAction_button, flag=wx.ALL, border=5)
        #                     Supprimer l'action sélectionnée
        self.deleteSelectedAction_button = wx.Button(listActions_panel, label="Supprimer")
        listActions_options_sizer.Add(self.deleteSelectedAction_button, flag=wx.ALL, border=5)
        #                 Paramètres
        self.selectedAction_panel = wx.Panel(listActions_panel, style=wx.TAB_TRAVERSAL)
        listActions_action_sizer.Add(self.selectedAction_panel, flag=wx.EXPAND |wx.ALL, border=5)
        #     .
        splitter.SplitHorizontally(listFiles_panel, listActions_panel, 150) # TODO: Proportion initiale
    
    
    
    def AddPath(self, path):
        '''
        Ajouter un fichier ou un répertoire
        @param path: Chemin
        @author: Julien
        '''
        (head, tail) = os.path.split(path)
        index = self.listFiles_listCtrl.InsertStringItem(0, label=head)
        self.listFiles_listCtrl.SetStringItem(index, 1, tail)
        self.listFiles_listCtrl.SetStringItem(index, 2, "TODO")
    
    
    
    def OnAddFile(self, event):
        '''
        Ajout d'un fichier
        @param event: Événement
        @author: Julien
        @todo: Impélmenter
        '''
        print "OnAddFile"
        event.Skip()
    
    
    def OnAddFolder(self, event):
        '''
        Ajout d'un répertoire
        @param event: Événement
        @author: Julien
        @todo: Impélmenter
        '''
        print "OnAddFolder"
        event.Skip()
    
    
    def OnRemoveSelectedListFiles(self, event):
        '''
        Supprimer la liste des fichiers ou répertoires sélectionnés de la liste
        @param event: Événement
        @author: Julien
        @todo: Impélmenter
        '''
        print "OnRemoveSelectedListFiles"
        event.Skip()
    
    
    def UpdateSurvey(self):
        '''
        Mettre à jour l'aperçu des noms de fichier après modification
        @author: Julien
        @todo: Implémenter
        '''
        print "UpdateSurvey"
    
    
    def OnTest(self, event):
        print "OnTest"
        self.AddPath("C:\\toto\\app\\fdv.mp3")
        event.Skip()
        




if __name__ == '__main__':
    ex = wx.App(redirect=False)
    fen = MainFrame()
    fen.Show(True)
    ex.MainLoop()
    pass