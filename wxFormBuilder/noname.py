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
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 634,771 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.menubar = wx.MenuBar( 0 )
		self.menu_fichier = wx.Menu()
		self.menu_fichier_quitter = wx.MenuItem( self.menu_fichier, wx.ID_ANY, u"Quitter", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_fichier.AppendItem( self.menu_fichier_quitter )
		
		self.menubar.Append( self.menu_fichier, u"Fichier" ) 
		
		self.SetMenuBar( self.menubar )
		
		self.toolBar = self.CreateToolBar( 0, wx.ID_ANY ) 
		self.toolBar.AddLabelTool( wx.ID_ANY, u"Supprimer les lignes", wx.Bitmap( u"../formatmp3/gui/icons/exit.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
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
		boxSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self.selectedAction_scrolledWindow, wx.ID_ANY, u"Couper le nom du fichier", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		boxSizer2.Add( self.title, 0, wx.ALL, 5 )
		
		self.description = wx.StaticText( self.selectedAction_scrolledWindow, wx.ID_ANY, u"todo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.description.Wrap( -1 )
		self.description.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		boxSizer2.Add( self.description, 0, wx.ALL, 5 )
		
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
		
		
		boxSizer2.Add( options_gridSizer, 0, wx.ALL, 5 )
		
		appliquerA_staticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.selectedAction_scrolledWindow, wx.ID_ANY, u"Appliquer à" ), wx.VERTICAL )
		
		self.filename_radioButton = wx.RadioButton( self.selectedAction_scrolledWindow, wx.ID_ANY, u"Nom du fichier", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.filename_radioButton.SetValue( True ) 
		appliquerA_staticBoxSizer.Add( self.filename_radioButton, 0, wx.ALL, 5 )
		
		self.extension_radioButton = wx.RadioButton( self.selectedAction_scrolledWindow, wx.ID_ANY, u"Extension", wx.DefaultPosition, wx.DefaultSize, 0 )
		appliquerA_staticBoxSizer.Add( self.extension_radioButton, 0, wx.ALL, 5 )
		
		
		boxSizer2.Add( appliquerA_staticBoxSizer, 0, wx.ALL, 5 )
		
		
		self.selectedAction_scrolledWindow.SetSizer( boxSizer2 )
		self.selectedAction_scrolledWindow.Layout()
		boxSizer2.Fit( self.selectedAction_scrolledWindow )
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
		
		self.beginSens_radioButton = wx.RadioButton( self, wx.ID_ANY, u"du début", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		
		gridSizer = wx.GridSizer( 0, 2, 0, 0 )
		
		self.artiste_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Artiste : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridSizer.Add( self.artiste_checkBox, 0, wx.ALL, 5 )
		
		self.artiste_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gridSizer.Add( self.artiste_textCtrl, 0, wx.ALL, 5 )
		
		self.album_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Album : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridSizer.Add( self.album_checkBox, 0, wx.ALL, 5 )
		
		self.album_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gridSizer.Add( self.album_textCtrl, 0, wx.ALL, 5 )
		
		self.genre_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Genre : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridSizer.Add( self.genre_checkBox, 0, wx.ALL, 5 )
		
		self.genre_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gridSizer.Add( self.genre_textCtrl, 0, wx.ALL, 5 )
		
		self.annee_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Année : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridSizer.Add( self.annee_checkBox, 0, wx.ALL, 5 )
		
		self.annee_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"azza", wx.DefaultPosition, wx.DefaultSize, 0 )
		gridSizer.Add( self.annee_textCtrl, 0, wx.ALL, 5 )
		
		
		boxSizer.Add( gridSizer, 0, wx.ALL, 5 )
		
		
		self.SetSizer( boxSizer )
		self.Layout()
		boxSizer.Fit( self )
	
	def __del__( self ):
		pass
	

