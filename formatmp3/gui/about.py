#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Fenètre "À propos"
@author: Julien
'''



import wx



class View(wx.Frame):
    '''
    Vue
    @author: Julien
    '''
    
    
    def __init__(self, parent=None):
        '''
        Constructeur
        @param parent: Fenêtre parent
        @author: Julien
        '''
        # Fenêtre
        wx.Frame.__init__(self, parent, title="À propos de FormatMP3", style=wx.CAPTION|wx.SYSTEM_MENU|wx.CLOSE_BOX|wx.FRAME_NO_TASKBAR)#wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER)
        self.CenterOnScreen()
        # Icone
        icon = wx.Icon("icons/about.png", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)
        
        frame_boxSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(frame_boxSizer)
        # Frame
        main_panel = wx.Panel(self)
        frame_boxSizer.Add(main_panel, 1, wx.ALL|wx.EXPAND)
        main_boxSizer = wx.BoxSizer(wx.VERTICAL)
        main_panel.SetSizer(main_boxSizer)
        #     Titre
        title_staticText = wx.StaticText(main_panel, label="FormatMP3")
        title_files_font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_staticText.SetFont(title_files_font)
        main_boxSizer.Add(title_staticText, flag=wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, border=5)
        #     gridSizer
        gridSizer = wx.GridSizer(0, 2)
        main_boxSizer.Add(gridSizer, flag=wx.ALL|wx.ALIGN_CENTER_HORIZONTAL)
        #         Version
        #             Titre
        title_version_staticText = wx.StaticText(main_panel, label="Version :")
        title_version_font = wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_version_staticText.SetFont(title_version_font)
        gridSizer.Add(title_version_staticText, flag=wx.ALL|wx.ALIGN_RIGHT, border=5)
        #             Valeur
        value_version_staticText = wx.StaticText(main_panel, label="1.0")
        gridSizer.Add(value_version_staticText, flag=wx.ALL, border=5)
        #         Sources
        #             Titre
        title_sources_staticText = wx.StaticText(main_panel, label="Sources :")
        title_sources_font = wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_sources_staticText.SetFont(title_sources_font)
        gridSizer.Add(title_sources_staticText, flag=wx.ALL|wx.ALIGN_RIGHT, border=5)
        #             Valeur
        value_sources_staticText = wx.HyperlinkCtrl(main_panel, label="GitHub",  url="https://github.com/pinguet62/FormatMP3")
        gridSizer.Add(value_sources_staticText, flag=wx.ALL, border=5)
        #         Sources
        #             Titre
        title_licence_staticText = wx.StaticText(main_panel, label="Licence :")
        title_licence_font = wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_licence_staticText.SetFont(title_licence_font)
        gridSizer.Add(title_licence_staticText, flag=wx.ALL|wx.ALIGN_RIGHT, border=5)
        #             Valeur
        value_licence_staticText = wx.HyperlinkCtrl(main_panel, label="Beerware",  url="http://fr.wikipedia.org/wiki/Beerware")
        gridSizer.Add(value_licence_staticText, flag=wx.ALL, border=5)
        #         Développé par
        #             Titre
        title_developpePar_staticText = wx.StaticText(main_panel, label="Développé par :")
        title_developpePar_font = wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_developpePar_staticText.SetFont(title_developpePar_font)
        gridSizer.Add(title_developpePar_staticText, flag=wx.ALL|wx.ALIGN_RIGHT, border=5)
        #             Valeur
        value_developpePar_staticText = wx.StaticText(main_panel, label="Julien PINGUET")
        gridSizer.Add(value_developpePar_staticText, flag=wx.ALL, border=5)
        #         Sources
        #             Titre
        title_contact_staticText = wx.StaticText(main_panel, label="Contact :")
        title_contact_font = wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_contact_staticText.SetFont(title_contact_font)
        gridSizer.Add(title_contact_staticText, flag=wx.ALL|wx.ALIGN_RIGHT, border=5)
        #             Valeur
        value_contact_staticText = wx.HyperlinkCtrl(main_panel, label="Email",  url="mailto:pinguet62@gmail.com?subject=FormatMP3")
        gridSizer.Add(value_contact_staticText, flag=wx.ALL, border=5)



class Controller(object):
    '''
    Controlleur
    @author: Julien
    '''
    
    
    def __init__(self, app):
        '''
        Constructeur
        @param app: Application
        @author: Julien
        '''
        self.app = app
        self.view = View(app.TopWindow)
        
        # Binding de la vue
        self.view.Bind(event=wx.EVT_CLOSE, handler=self.OnClose)
        
        # Afficher
        if self.view.GetParent() is not None:
            self.view.GetParent().Enable(False)
        self.view.Show()
    
    # Événements de la vue
    
    def OnClose(self, event):
        '''
        Quitter
        @param event: Événement
        @author: Julien
        '''
        if self.view.GetParent() is not None:
            self.view.GetParent().Enable(True)
        event.Skip()



if __name__ == '__main__':
    app = wx.App(False)
    controller = Controller(app)
    app.MainLoop()