# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FormatMP3 - Formatez vos fichiers MP3 en un clic !", pos = wx.DefaultPosition, size = wx.Size( 634,771 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.menubar = wx.MenuBar( 0 )
		self.menu_fichier = wx.Menu()
		self.menu_fichier_ouvrir = wx.MenuItem( self.menu_fichier, wx.ID_ANY, u"Ouvrir", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_fichier.AppendItem( self.menu_fichier_ouvrir )
		
		self.menu_fichier_enregistrer = wx.MenuItem( self.menu_fichier, wx.ID_ANY, u"Enregistrer", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_fichier.AppendItem( self.menu_fichier_enregistrer )
		
		self.menu_fichier_enregistrerSous = wx.MenuItem( self.menu_fichier, wx.ID_ANY, u"Enregistrer sous", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_fichier.AppendItem( self.menu_fichier_enregistrerSous )
		
		self.menu_fichier.AppendSeparator()
		
		self.menu_fichier_quitter = wx.MenuItem( self.menu_fichier, wx.ID_ANY, u"Quitter", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_fichier.AppendItem( self.menu_fichier_quitter )
		
		self.menubar.Append( self.menu_fichier, u"Fichier" ) 
		
		self.SetMenuBar( self.menubar )
		
		self.toolBar = self.CreateToolBar( 0, wx.ID_ANY ) 
		self.toolBar.AddLabelTool( wx.ID_ANY, u"Supprimer les lignes", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.toolBar.Realize() 
		
		main_boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.main_splitterWindow = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_NO_XP_THEME )
		self.main_splitterWindow.Bind( wx.EVT_IDLE, self.main_splitterWindowOnIdle )
		
		self.files_panel = wx.Panel( self.main_splitterWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		files_boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title_files_staticText = wx.StaticText( self.files_panel, wx.ID_ANY, u"Fichiers", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title_files_staticText.Wrap( -1 )
		self.title_files_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		files_boxSizer.Add( self.title_files_staticText, 0, wx.ALL, 5 )
		
		self.files_toolbar = wx.ToolBar( self.files_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT|wx.TB_TEXT ) 
		self.files_toolbar.Realize() 
		
		files_boxSizer.Add( self.files_toolbar, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.listFiles_listCtrl = wx.ListCtrl( self.files_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		files_boxSizer.Add( self.listFiles_listCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.files_panel.SetSizer( files_boxSizer )
		self.files_panel.Layout()
		files_boxSizer.Fit( self.files_panel )
		self.actions_panel = wx.Panel( self.main_splitterWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		actions_boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title_actions_staticText = wx.StaticText( self.actions_panel, wx.ID_ANY, u"Actions à réaliser", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title_actions_staticText.Wrap( -1 )
		self.title_actions_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		actions_boxSizer.Add( self.title_actions_staticText, 0, wx.ALL, 5 )
		
		self.actions_toolBar = wx.ToolBar( self.actions_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL )
		self.actions_toolBar.SetToolBitmapSize( wx.Size( 16,16 ) )
		self.actions_toolBar.Realize() 
		
		actions_boxSizer.Add( self.actions_toolBar, 0, wx.EXPAND, 5 )
		
		self.actions_splitter = wx.SplitterWindow( self.actions_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.actions_splitter.Bind( wx.EVT_IDLE, self.actions_splitterOnIdle )
		
		self.listActions_panel = wx.Panel( self.actions_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		listActions_boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		listActionsToDo_listBoxChoices = []
		self.listActionsToDo_listBox = wx.ListBox( self.listActions_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listActionsToDo_listBoxChoices, 0 )
		listActions_boxSizer.Add( self.listActionsToDo_listBox, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.listActions_panel.SetSizer( listActions_boxSizer )
		self.listActions_panel.Layout()
		listActions_boxSizer.Fit( self.listActions_panel )
		self.selectedAction_scrolledWindow = wx.ScrolledWindow( self.actions_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.selectedAction_scrolledWindow.SetScrollRate( 5, 5 )
		boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self.selectedAction_scrolledWindow, wx.ID_ANY, u"Couper le nom du fichier", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		boxSizer.Add( self.title, 0, wx.ALL, 5 )
		
		self.description = wx.StaticText( self.selectedAction_scrolledWindow, wx.ID_ANY, u"todo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.description.Wrap( -1 )
		self.description.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		boxSizer.Add( self.description, 0, wx.ALL, 5 )
		
		options_gridSizer = wx.StaticBoxSizer( wx.StaticBox( self.selectedAction_scrolledWindow, wx.ID_ANY, u"Options" ), wx.VERTICAL )
		
		gridSizer = wx.GridSizer( 3, 2, 0, 0 )
		
		self.nomber_staticText = wx.StaticText( self.selectedAction_scrolledWindow, wx.ID_ANY, u"Nombre de caractères à supprimer : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nomber_staticText.Wrap( -1 )
		gridSizer.Add( self.nomber_staticText, 0, wx.ALL, 5 )
		
		self.number_spinCtrl = wx.SpinCtrl( self.selectedAction_scrolledWindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, 0, 999, 0 )
		gridSizer.Add( self.number_spinCtrl, 0, wx.ALL, 5 )
		
		self.position_staticText = wx.StaticText( self.selectedAction_scrolledWindow, wx.ID_ANY, u"A partir de la position : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.position_staticText.Wrap( -1 )
		gridSizer.Add( self.position_staticText, 0, wx.ALL, 5 )
		
		self.position_spinCtrl = wx.SpinCtrl( self.selectedAction_scrolledWindow, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gridSizer.Add( self.position_spinCtrl, 0, wx.ALL, 5 )
		
		self.sens_staticText = wx.StaticText( self.selectedAction_scrolledWindow, wx.ID_ANY, u"En partant : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sens_staticText.Wrap( -1 )
		gridSizer.Add( self.sens_staticText, 0, wx.ALL, 5 )
		
		sens_boxSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.beginSens_radioButton = wx.RadioButton( self.selectedAction_scrolledWindow, wx.ID_ANY, u"du début", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.beginSens_radioButton.SetValue( True ) 
		sens_boxSizer.Add( self.beginSens_radioButton, 0, wx.ALL, 5 )
		
		self.endSens_radioButton = wx.RadioButton( self.selectedAction_scrolledWindow, wx.ID_ANY, u"de la fin", wx.DefaultPosition, wx.DefaultSize, 0 )
		sens_boxSizer.Add( self.endSens_radioButton, 0, wx.ALL, 5 )
		
		
		gridSizer.Add( sens_boxSizer, 0, wx.ALL, 0 )
		
		
		options_gridSizer.Add( gridSizer, 0, wx.ALL, 0 )
		
		
		boxSizer.Add( options_gridSizer, 0, wx.ALL, 5 )
		
		appliquerA_staticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.selectedAction_scrolledWindow, wx.ID_ANY, u"Appliquer à" ), wx.VERTICAL )
		
		self.filename_radioButton = wx.RadioButton( self.selectedAction_scrolledWindow, wx.ID_ANY, u"Nom du fichier", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.filename_radioButton.SetValue( True ) 
		appliquerA_staticBoxSizer.Add( self.filename_radioButton, 0, wx.ALL, 5 )
		
		self.extension_radioButton = wx.RadioButton( self.selectedAction_scrolledWindow, wx.ID_ANY, u"Extension", wx.DefaultPosition, wx.DefaultSize, 0 )
		appliquerA_staticBoxSizer.Add( self.extension_radioButton, 0, wx.ALL, 5 )
		
		
		boxSizer.Add( appliquerA_staticBoxSizer, 0, wx.ALL, 5 )
		
		
		self.selectedAction_scrolledWindow.SetSizer( boxSizer )
		self.selectedAction_scrolledWindow.Layout()
		boxSizer.Fit( self.selectedAction_scrolledWindow )
		self.actions_splitter.SplitVertically( self.listActions_panel, self.selectedAction_scrolledWindow, 50 )
		actions_boxSizer.Add( self.actions_splitter, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.actions_panel.SetSizer( actions_boxSizer )
		self.actions_panel.Layout()
		actions_boxSizer.Fit( self.actions_panel )
		self.main_splitterWindow.SplitHorizontally( self.files_panel, self.actions_panel, 301 )
		main_boxSizer.Add( self.main_splitterWindow, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( main_boxSizer )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
	def main_splitterWindowOnIdle( self, event ):
		self.main_splitterWindow.SetSashPosition( 301 )
		self.main_splitterWindow.Unbind( wx.EVT_IDLE )
	
	def actions_splitterOnIdle( self, event ):
		self.actions_splitter.SetSashPosition( 50 )
		self.actions_splitter.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class CaseChangeGui_panel
###########################################################################

class CaseChangeGui_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self, wx.ID_ANY, u"Changement de case", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		boxSizer.Add( self.title, 0, wx.ALL, 5 )
		
		self.description = wx.StaticText( self, wx.ID_ANY, u"1ère lettre en majuscule, le reste en minuscule", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.description.Wrap( -1 )
		self.description.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		boxSizer.Add( self.description, 0, wx.ALL, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Options" ), wx.VERTICAL )
		
		self.lower_radioButton = wx.RadioButton( self, wx.ID_ANY, u"Tout en minuscule", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		sbSizer3.Add( self.lower_radioButton, 0, wx.ALL, 5 )
		
		self.firstMaj_radioButton = wx.RadioButton( self, wx.ID_ANY, u"Majuscule la première lettre du nom", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.firstMaj_radioButton.SetValue( True ) 
		sbSizer3.Add( self.firstMaj_radioButton, 0, wx.ALL, 5 )
		
		self.title_radioButton = wx.RadioButton( self, wx.ID_ANY, u"Majuscule la première lettre de chaque mot", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.title_radioButton, 0, wx.ALL, 5 )
		
		self.upper_radioButton = wx.RadioButton( self, wx.ID_ANY, u"Tout en majuscule", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.upper_radioButton, 0, wx.ALL, 5 )
		
		
		boxSizer.Add( sbSizer3, 0, wx.ALL, 5 )
		
		
		self.SetSizer( boxSizer )
		self.Layout()
		boxSizer.Fit( self )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ReplaceStringGui_panel
###########################################################################

class ReplaceStringGui_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self, wx.ID_ANY, u"Remplacement de chaîne", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		boxSizer.Add( self.title, 0, wx.ALL, 5 )
		
		self.description = wx.StaticText( self, wx.ID_ANY, u"todo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.description.Wrap( -1 )
		self.description.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		boxSizer.Add( self.description, 0, wx.ALL, 5 )
		
		options_staticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Options" ), wx.VERTICAL )
		
		options_gridSizer = wx.GridSizer( 0, 2, 0, 0 )
		
		self.oldStr_staticText = wx.StaticText( self, wx.ID_ANY, u"Remplacer : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.oldStr_staticText.Wrap( -1 )
		options_gridSizer.Add( self.oldStr_staticText, 0, wx.ALL, 5 )
		
		self.oldStr_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		options_gridSizer.Add( self.oldStr_textCtrl, 0, wx.ALL, 5 )
		
		self.newStr_staticText = wx.StaticText( self, wx.ID_ANY, u"Par : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.newStr_staticText.Wrap( -1 )
		options_gridSizer.Add( self.newStr_staticText, 0, wx.ALL, 5 )
		
		self.newStr_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		options_gridSizer.Add( self.newStr_textCtrl, 0, wx.ALL, 5 )
		
		
		options_staticBoxSizer.Add( options_gridSizer, 0, wx.ALL, 0 )
		
		
		boxSizer.Add( options_staticBoxSizer, 0, wx.ALL, 5 )
		
		appliquerA_staticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Appliquer à" ), wx.VERTICAL )
		
		self.filename_radioButton = wx.RadioButton( self, wx.ID_ANY, u"Nom du fichier", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.filename_radioButton.SetValue( True ) 
		appliquerA_staticBoxSizer.Add( self.filename_radioButton, 0, wx.ALL, 5 )
		
		self.extension_radioButton = wx.RadioButton( self, wx.ID_ANY, u"Extension", wx.DefaultPosition, wx.DefaultSize, 0 )
		appliquerA_staticBoxSizer.Add( self.extension_radioButton, 0, wx.ALL, 5 )
		
		
		boxSizer.Add( appliquerA_staticBoxSizer, 0, wx.ALL, 5 )
		
		
		self.SetSizer( boxSizer )
		self.Layout()
		boxSizer.Fit( self )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class CutGui_panel
###########################################################################

class CutGui_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self, wx.ID_ANY, u"Couper le nom du fichier", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		boxSizer.Add( self.title, 0, wx.ALL, 5 )
		
		self.description = wx.StaticText( self, wx.ID_ANY, u"todo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.description.Wrap( -1 )
		self.description.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		boxSizer.Add( self.description, 0, wx.ALL, 5 )
		
		options_gridSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Options" ), wx.VERTICAL )
		
		gridSizer = wx.GridSizer( 3, 2, 0, 0 )
		
		self.nomber_staticText = wx.StaticText( self, wx.ID_ANY, u"Nombre de caractères à supprimer : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nomber_staticText.Wrap( -1 )
		gridSizer.Add( self.nomber_staticText, 0, wx.ALL, 5 )
		
		self.number_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, 0, 999, 0 )
		gridSizer.Add( self.number_spinCtrl, 0, wx.ALL, 5 )
		
		self.position_staticText = wx.StaticText( self, wx.ID_ANY, u"A partir de la position : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.position_staticText.Wrap( -1 )
		gridSizer.Add( self.position_staticText, 0, wx.ALL, 5 )
		
		self.position_spinCtrl = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gridSizer.Add( self.position_spinCtrl, 0, wx.ALL, 5 )
		
		self.sens_staticText = wx.StaticText( self, wx.ID_ANY, u"En partant : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sens_staticText.Wrap( -1 )
		gridSizer.Add( self.sens_staticText, 0, wx.ALL, 5 )
		
		sens_boxSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.beginSens_radioButton = wx.RadioButton( self, wx.ID_ANY, u"du début", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.beginSens_radioButton.SetValue( True ) 
		sens_boxSizer.Add( self.beginSens_radioButton, 0, wx.ALL, 5 )
		
		self.endSens_radioButton = wx.RadioButton( self, wx.ID_ANY, u"de la fin", wx.DefaultPosition, wx.DefaultSize, 0 )
		sens_boxSizer.Add( self.endSens_radioButton, 0, wx.ALL, 5 )
		
		
		gridSizer.Add( sens_boxSizer, 0, wx.ALL, 0 )
		
		
		options_gridSizer.Add( gridSizer, 0, wx.ALL, 0 )
		
		
		boxSizer.Add( options_gridSizer, 0, wx.ALL, 5 )
		
		appliquerA_staticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Appliquer à" ), wx.VERTICAL )
		
		self.filename_radioButton = wx.RadioButton( self, wx.ID_ANY, u"Nom du fichier", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.filename_radioButton.SetValue( True ) 
		appliquerA_staticBoxSizer.Add( self.filename_radioButton, 0, wx.ALL, 5 )
		
		self.extension_radioButton = wx.RadioButton( self, wx.ID_ANY, u"Extension", wx.DefaultPosition, wx.DefaultSize, 0 )
		appliquerA_staticBoxSizer.Add( self.extension_radioButton, 0, wx.ALL, 5 )
		
		
		boxSizer.Add( appliquerA_staticBoxSizer, 0, wx.ALL, 5 )
		
		
		self.SetSizer( boxSizer )
		self.Layout()
		boxSizer.Fit( self )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class InsertStringGui_panel
###########################################################################

class InsertStringGui_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self, wx.ID_ANY, u"Insertion d'une chaîne", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		boxSizer.Add( self.title, 0, wx.ALL, 5 )
		
		self.description = wx.StaticText( self, wx.ID_ANY, u"Insérer une chaîne de caractères dans le nom du fichier", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.description.Wrap( -1 )
		self.description.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		boxSizer.Add( self.description, 0, wx.ALL, 5 )
		
		gridSizer = wx.GridSizer( 0, 2, 0, 0 )
		
		self.string_staticStext = wx.StaticText( self, wx.ID_ANY, u"Chaîne à insérer : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.string_staticStext.Wrap( -1 )
		gridSizer.Add( self.string_staticStext, 0, wx.ALL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gridSizer.Add( self.m_textCtrl7, 0, wx.ALL, 5 )
		
		self.position_staticText1 = wx.StaticText( self, wx.ID_ANY, u"A partir de la position : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.position_staticText1.Wrap( -1 )
		gridSizer.Add( self.position_staticText1, 0, wx.ALL, 5 )
		
		self.m_spinCtrl3 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gridSizer.Add( self.m_spinCtrl3, 0, wx.ALL, 5 )
		
		self.sens_staticText = wx.StaticText( self, wx.ID_ANY, u"A partir : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sens_staticText.Wrap( -1 )
		gridSizer.Add( self.sens_staticText, 0, wx.ALL, 5 )
		
		sens_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.beginSens_radioButton = wx.RadioButton( self, wx.ID_ANY, u"du début", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.beginSens_radioButton.SetValue( True ) 
		sens_sizer.Add( self.beginSens_radioButton, 0, wx.ALL, 5 )
		
		self.endSens_radioButton = wx.RadioButton( self, wx.ID_ANY, u"de la fin", wx.DefaultPosition, wx.DefaultSize, 0 )
		sens_sizer.Add( self.endSens_radioButton, 0, wx.ALL, 5 )
		
		
		gridSizer.Add( sens_sizer, 1, wx.ALL, 0 )
		
		
		boxSizer.Add( gridSizer, 0, wx.ALL, 5 )
		
		
		self.SetSizer( boxSizer )
		self.Layout()
		boxSizer.Fit( self )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class UpdateTagsGui_panel
###########################################################################

class UpdateTagsGui_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self, wx.ID_ANY, u"Tags", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		boxSizer.Add( self.title, 0, wx.ALL, 5 )
		
		self.description = wx.StaticText( self, wx.ID_ANY, u"todo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.description.Wrap( -1 )
		self.description.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		boxSizer.Add( self.description, 0, wx.ALL, 5 )
		
		description_staticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Description" ), wx.VERTICAL )
		
		description_gridSizer = wx.GridSizer( 0, 2, 0, 0 )
		
		self.title_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Titre : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		description_gridSizer.Add( self.title_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		title_comboBoxChoices = [ u"%auto%", u"%filename%", wx.EmptyString ]
		self.title_comboBox = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, title_comboBoxChoices, 0 )
		self.title_comboBox.SetSelection( 1 )
		description_gridSizer.Add( self.title_comboBox, 0, wx.ALL, 5 )
		
		self.subtitle_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Sous-titre : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.subtitle_checkBox.SetValue(True) 
		description_gridSizer.Add( self.subtitle_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.subtitle_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		description_gridSizer.Add( self.subtitle_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.notation_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Notation : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.notation_checkBox.Enable( False )
		
		description_gridSizer.Add( self.notation_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.notation_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		valeurs_notation_boxSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		
		valeurs_notation_boxSizer.AddSpacer( ( 5, 0), 0, wx.ALL, 0 )
		
		self.notation_1_radioButton = wx.RadioButton( self.notation_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		valeurs_notation_boxSizer.Add( self.notation_1_radioButton, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.notation_2_radioButton = wx.RadioButton( self.notation_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		valeurs_notation_boxSizer.Add( self.notation_2_radioButton, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.notation_3_radioButton = wx.RadioButton( self.notation_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		valeurs_notation_boxSizer.Add( self.notation_3_radioButton, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.notation_4_radioButton = wx.RadioButton( self.notation_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		valeurs_notation_boxSizer.Add( self.notation_4_radioButton, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.notation_5_radioButton = wx.RadioButton( self.notation_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		valeurs_notation_boxSizer.Add( self.notation_5_radioButton, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.notation_panel.SetSizer( valeurs_notation_boxSizer )
		self.notation_panel.Layout()
		valeurs_notation_boxSizer.Fit( self.notation_panel )
		description_gridSizer.Add( self.notation_panel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
		
		self.comment_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Commentaire : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.comment_checkBox.SetValue(True) 
		self.comment_checkBox.Enable( False )
		
		description_gridSizer.Add( self.comment_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.comment_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.comment_textCtrl.Enable( False )
		
		description_gridSizer.Add( self.comment_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		description_staticBoxSizer.Add( description_gridSizer, 0, wx.ALL, 0 )
		
		
		boxSizer.Add( description_staticBoxSizer, 0, wx.ALL, 5 )
		
		media_staticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Média" ), wx.VERTICAL )
		
		media_gridSizer = wx.GridSizer( 0, 2, 0, 0 )
		
		self.albumArtist_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Artiste de l'album : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.albumArtist_checkBox.SetValue(True) 
		media_gridSizer.Add( self.albumArtist_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.artistAlbum_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		media_gridSizer.Add( self.artistAlbum_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.artiste_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Artiste : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		media_gridSizer.Add( self.artiste_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.artiste_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		media_gridSizer.Add( self.artiste_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.album_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Album : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		media_gridSizer.Add( self.album_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.album_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		media_gridSizer.Add( self.album_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.annee_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Année : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		media_gridSizer.Add( self.annee_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.annee_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		media_gridSizer.Add( self.annee_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.trackNumber_checkBox = wx.CheckBox( self, wx.ID_ANY, u"N° : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		media_gridSizer.Add( self.trackNumber_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.trackNumber_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		media_gridSizer.Add( self.trackNumber_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.genre_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Genre : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		media_gridSizer.Add( self.genre_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.genre_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		media_gridSizer.Add( self.genre_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		media_staticBoxSizer.Add( media_gridSizer, 0, wx.ALL, 0 )
		
		
		boxSizer.Add( media_staticBoxSizer, 0, wx.ALL, 5 )
		
		origine_staticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Origine" ), wx.VERTICAL )
		
		origine_gridSizer = wx.GridSizer( 0, 2, 0, 0 )
		
		self.publisher_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Éditeur : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.publisher_checkBox.SetValue(True) 
		origine_gridSizer.Add( self.publisher_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.publisher_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		origine_gridSizer.Add( self.publisher_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.encodedBy_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Encodé par : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.encodedBy_checkBox.SetValue(True) 
		origine_gridSizer.Add( self.encodedBy_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.encodedBy_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		origine_gridSizer.Add( self.encodedBy_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.urlAuteur_checkBox = wx.CheckBox( self, wx.ID_ANY, u"URL de l'auteur : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.urlAuteur_checkBox.SetValue(True) 
		origine_gridSizer.Add( self.urlAuteur_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.urlAuteur_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		origine_gridSizer.Add( self.urlAuteur_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		origine_staticBoxSizer.Add( origine_gridSizer, 0, wx.ALL, 0 )
		
		
		boxSizer.Add( origine_staticBoxSizer, 0, wx.ALL, 5 )
		
		contenu_staticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Contenu" ), wx.VERTICAL )
		
		contenu_gridSizer = wx.GridSizer( 0, 2, 0, 0 )
		
		self.composer_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Compositeur : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.composer_checkBox.SetValue(True) 
		contenu_gridSizer.Add( self.composer_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.composer_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		contenu_gridSizer.Add( self.composer_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.conductor_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Chef d'orchestre : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.conductor_checkBox.SetValue(True) 
		contenu_gridSizer.Add( self.conductor_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.conductor_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		contenu_gridSizer.Add( self.conductor_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.groupDescription_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Description du groupe : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.groupDescription_checkBox.SetValue(True) 
		self.groupDescription_checkBox.Enable( False )
		
		contenu_gridSizer.Add( self.groupDescription_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.groupDescription_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.groupDescription_textCtrl.Enable( False )
		
		contenu_gridSizer.Add( self.groupDescription_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ambiance_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Ambiance : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ambiance_checkBox.SetValue(True) 
		self.ambiance_checkBox.Enable( False )
		
		contenu_gridSizer.Add( self.ambiance_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ambiance_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ambiance_textCtrl.Enable( False )
		
		contenu_gridSizer.Add( self.ambiance_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.discNumber_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Partie du coffret : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.discNumber_checkBox.SetValue(True) 
		contenu_gridSizer.Add( self.discNumber_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.discNumber_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		contenu_gridSizer.Add( self.discNumber_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.originalKey_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Clé d'origine : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.originalKey_checkBox.SetValue(True) 
		self.originalKey_checkBox.Enable( False )
		
		contenu_gridSizer.Add( self.originalKey_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.originalKey_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.originalKey_textCtrl.Enable( False )
		
		contenu_gridSizer.Add( self.originalKey_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.bpm_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Battements par minute : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bpm_checkBox.SetValue(True) 
		contenu_gridSizer.Add( self.bpm_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.bpm_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		contenu_gridSizer.Add( self.bpm_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.compilation_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Partie d'une compilation ? ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.compilation_checkBox.SetValue(True) 
		contenu_gridSizer.Add( self.compilation_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		compilation_boxSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.yes_compilation_radioBtn = wx.RadioButton( self, wx.ID_ANY, u"oui", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		compilation_boxSizer.Add( self.yes_compilation_radioBtn, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.no_compilation_radioBtn = wx.RadioButton( self, wx.ID_ANY, u"non", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.no_compilation_radioBtn.SetValue( True ) 
		compilation_boxSizer.Add( self.no_compilation_radioBtn, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		contenu_gridSizer.Add( compilation_boxSizer, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )
		
		
		contenu_staticBoxSizer.Add( contenu_gridSizer, 0, wx.ALL, 0 )
		
		
		boxSizer.Add( contenu_staticBoxSizer, 0, wx.ALL, 5 )
		
		
		self.SetSizer( boxSizer )
		self.Layout()
		boxSizer.Fit( self )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class AboutFrame
###########################################################################

class AboutFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"À propos", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		frame_boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		main_boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title_staticText = wx.StaticText( self.main_panel, wx.ID_ANY, u"FormatMP3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title_staticText.Wrap( -1 )
		self.title_staticText.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		main_boxSizer.Add( self.title_staticText, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		gridSizer = wx.GridSizer( 0, 2, 0, 0 )
		
		self.title_version_staticText = wx.StaticText( self.main_panel, wx.ID_ANY, u"Version :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title_version_staticText.Wrap( -1 )
		self.title_version_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gridSizer.Add( self.title_version_staticText, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.value_version_staticText = wx.StaticText( self.main_panel, wx.ID_ANY, u"1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.value_version_staticText.Wrap( -1 )
		gridSizer.Add( self.value_version_staticText, 0, wx.ALL, 5 )
		
		self.title_sources_staticText = wx.StaticText( self.main_panel, wx.ID_ANY, u"Sources :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title_sources_staticText.Wrap( -1 )
		self.title_sources_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gridSizer.Add( self.title_sources_staticText, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.value_sources_hyperlinkCtrl = wx.HyperlinkCtrl( self.main_panel, wx.ID_ANY, u"GitHub", u"https://github.com/pinguet62/FormatMP3", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		gridSizer.Add( self.value_sources_hyperlinkCtrl, 0, wx.ALL, 5 )
		
		self.title_licence_staticText = wx.StaticText( self.main_panel, wx.ID_ANY, u"Licence :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title_licence_staticText.Wrap( -1 )
		self.title_licence_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gridSizer.Add( self.title_licence_staticText, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.value_licence_hyperlinkCtrl = wx.HyperlinkCtrl( self.main_panel, wx.ID_ANY, u"Beerware", u"http://fr.wikipedia.org/wiki/Beerware", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		gridSizer.Add( self.value_licence_hyperlinkCtrl, 0, wx.ALL, 5 )
		
		self.title_developpePar_staticText = wx.StaticText( self.main_panel, wx.ID_ANY, u"Développé par :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title_developpePar_staticText.Wrap( -1 )
		self.title_developpePar_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gridSizer.Add( self.title_developpePar_staticText, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.value_developpePar_staticText = wx.StaticText( self.main_panel, wx.ID_ANY, u"Julien PINGUET", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.value_developpePar_staticText.Wrap( -1 )
		gridSizer.Add( self.value_developpePar_staticText, 0, wx.ALL, 5 )
		
		self.title_contact_staticText = wx.StaticText( self.main_panel, wx.ID_ANY, u"Contact :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title_contact_staticText.Wrap( -1 )
		self.title_contact_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gridSizer.Add( self.title_contact_staticText, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.value_contact_hyperlinkCtrl = wx.HyperlinkCtrl( self.main_panel, wx.ID_ANY, u"Email", u"mailto:pinguet62@gmail.com?subject=FormatMP3", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		gridSizer.Add( self.value_contact_hyperlinkCtrl, 0, wx.ALL, 5 )
		
		
		main_boxSizer.Add( gridSizer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )
		
		
		self.main_panel.SetSizer( main_boxSizer )
		self.main_panel.Layout()
		main_boxSizer.Fit( self.main_panel )
		frame_boxSizer.Add( self.main_panel, 1, wx.EXPAND|wx.ALL, 0 )
		
		
		self.SetSizer( frame_boxSizer )
		self.Layout()
		frame_boxSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

