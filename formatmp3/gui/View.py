#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Vues du pattern MVC
@author: Julien
'''



import wx



class View(wx.Frame):
    '''
    Vue de l'interface principale
    @author: Julien
    '''
    
    
    def __init__(self):
        '''
        Constructeur
        @param parent: Fenêtre parent
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
        menubar_fichier_ouvrir_image.Rescale(16,16)
        menubar_fichier_ouvrir_bitmap = wx.BitmapFromImage(menubar_fichier_ouvrir_image)
        self.menubar_fichier_ouvrir.SetBitmap(menubar_fichier_ouvrir_bitmap)
        menubar_fichier.AppendItem(self.menubar_fichier_ouvrir)
        #     .
        menubar_fichier.AppendSeparator()
        #         Enregistrer
        self.menubar_fichier_enregistrer = wx.MenuItem(menubar_fichier, wx.ID_ANY, "&Enregistrer\tCtrl+S")
        menubar_fichier_enregistrer_image = wx.Image("icons/save.png")
        menubar_fichier_enregistrer_image.Rescale(16,16)
        menubar_fichier_enregistrer_bitmap = wx.BitmapFromImage(menubar_fichier_enregistrer_image)
        self.menubar_fichier_enregistrer.SetBitmap(menubar_fichier_enregistrer_bitmap)
        menubar_fichier.AppendItem(self.menubar_fichier_enregistrer)
        #         Enregistrer sous
        self.menubar_fichier_enregistrerSous = wx.MenuItem(menubar_fichier, wx.ID_ANY, "Enregistrer &sous...\tCtrl-Shift+S")
        menubar_fichier_enregistrerSous_image = wx.Image("icons/save.png")
        menubar_fichier_enregistrerSous_image.Rescale(16,16)
        menubar_fichier_enregistrerSous_bitmap = wx.BitmapFromImage(menubar_fichier_enregistrerSous_image)
        self.menubar_fichier_enregistrerSous.SetBitmap(menubar_fichier_enregistrerSous_bitmap)
        menubar_fichier.AppendItem(self.menubar_fichier_enregistrerSous)
        #     .
        menubar_fichier.AppendSeparator()
        #         Quitter
        self.menubar_fichier_quitter = wx.MenuItem(menubar_fichier, wx.ID_ANY, "&Quitter\tAlt+F4")
        menubar_fichier_quitter_image = wx.Image("icons/exit.png")
        menubar_fichier_quitter_image.Rescale(16,16)
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
        exit_image.Rescale(16,16)
        exit_bitmap = wx.BitmapFromImage(exit_image)
        self.exit_tool = toolBar.AddLabelTool(wx.ID_ANY, "Quitter", exit_bitmap)
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
        #                 Stoper
        stopActions_image = wx.Image("icons/stop.png")
        stopActions_image.Rescale(16,16)
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



if __name__ == '__main__':
    pass