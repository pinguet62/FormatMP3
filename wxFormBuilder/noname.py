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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 820,761 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		
		mainSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.splitter = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_NO_XP_THEME )
		self.splitter.Bind( wx.EVT_IDLE, self.splitterOnIdle )
		
		self.listFiles_panel = wx.Panel( self.splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		listFiles_boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.listFiles_title_staticText = wx.StaticText( self.listFiles_panel, wx.ID_ANY, u"Fichiers", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.listFiles_title_staticText.Wrap( -1 )
		self.listFiles_title_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		listFiles_boxSizer.Add( self.listFiles_title_staticText, 0, wx.ALL, 5 )
		
		self.listFiles_toolbar = wx.ToolBar( self.listFiles_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT|wx.TB_TEXT ) 
		self.listFiles_toolbar.AddLabelTool( wx.ID_ANY, u"Ajouter un fichier", wx.Bitmap( u"../formatmp3/gui/icons/add_file.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Ajouter un fichier dans la liste", wx.EmptyString, None ) 
		
		self.listFiles_toolbar.AddLabelTool( wx.ID_ANY, u"Ajouter un répertoire", wx.Bitmap( u"../formatmp3/gui/icons/add_folder.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Ajouter une répertoire dans la liste", wx.EmptyString, None ) 
		
		self.listFiles_toolbar.AddSeparator()
		
		self.listFiles_toolbar.AddLabelTool( wx.ID_ANY, u"Supprimer la sélection", wx.Bitmap( u"../formatmp3/gui/icons/remove_selected.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Supprimer les fichiers sélectionnés de la liste", wx.EmptyString, None ) 
		
		self.listFiles_toolbar.AddLabelTool( wx.ID_ANY, u"Supprimer tous les fichiers de la liste", wx.Bitmap( u"../formatmp3/gui/icons/remove_all.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Supprimer tous les fichiers de la liste", wx.EmptyString, None ) 
		
		self.listFiles_toolbar.Realize() 
		
		listFiles_boxSizer.Add( self.listFiles_toolbar, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.listFiles_listCtrl = wx.ListCtrl( self.listFiles_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		listFiles_boxSizer.Add( self.listFiles_listCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.listFiles_panel.SetSizer( listFiles_boxSizer )
		self.listFiles_panel.Layout()
		listFiles_boxSizer.Fit( self.listFiles_panel )
		self.listActions_panel = wx.Panel( self.splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		listActions_boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.listActions_title_staticText = wx.StaticText( self.listActions_panel, wx.ID_ANY, u"Actions à réaliser", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.listActions_title_staticText.Wrap( -1 )
		self.listActions_title_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		listActions_boxSizer.Add( self.listActions_title_staticText, 0, wx.ALL, 5 )
		
		self.m_toolBar4 = wx.ToolBar( self.listActions_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL )
		self.m_toolBar4.SetToolBitmapSize( wx.Size( 16,16 ) )
		self.m_toolBar4.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"../formatmp3/gui/icons/add.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar4.AddSeparator()
		
		self.m_toolBar4.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"../formatmp3/gui/icons/remove_selected.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar4.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"../formatmp3/gui/icons/remove_all.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar4.AddSeparator()
		
		self.m_toolBar4.AddLabelTool( wx.ID_ANY, u"Up", wx.Bitmap( u"../formatmp3/gui/icons/up.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar4.AddLabelTool( wx.ID_ANY, u"Down", wx.Bitmap( u"../formatmp3/gui/icons/down.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar4.Realize() 
		
		listActions_boxSizer.Add( self.m_toolBar4, 0, wx.EXPAND, 5 )
		
		listActionsToDo_listBoxChoices = []
		self.listActionsToDo_listBox = wx.ListBox( self.listActions_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listActionsToDo_listBoxChoices, 0 )
		listActions_boxSizer.Add( self.listActionsToDo_listBox, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.selectedAction_panel = wx.Panel( self.listActions_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,50 ), wx.TAB_TRAVERSAL )
		listActions_boxSizer.Add( self.selectedAction_panel, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.listActions_panel.SetSizer( listActions_boxSizer )
		self.listActions_panel.Layout()
		listActions_boxSizer.Fit( self.listActions_panel )
		self.splitter.SplitHorizontally( self.listFiles_panel, self.listActions_panel, 301 )
		mainSizer.Add( self.splitter, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( mainSizer )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
	def splitterOnIdle( self, event ):
		self.splitter.SetSashPosition( 301 )
		self.splitter.Unbind( wx.EVT_IDLE )
	

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
		
		gridSizer = wx.GridSizer( 0, 2, 0, 0 )
		
		self.oldStr_staticText = wx.StaticText( self, wx.ID_ANY, u"Remplacer : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.oldStr_staticText.Wrap( -1 )
		gridSizer.Add( self.oldStr_staticText, 0, wx.ALL, 5 )
		
		self.oldStr_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gridSizer.Add( self.oldStr_textCtrl, 0, wx.ALL, 5 )
		
		self.newStr_staticText = wx.StaticText( self, wx.ID_ANY, u"Par : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.newStr_staticText.Wrap( -1 )
		gridSizer.Add( self.newStr_staticText, 0, wx.ALL, 5 )
		
		self.newStr_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gridSizer.Add( self.newStr_textCtrl, 0, wx.ALL, 5 )
		
		
		boxSizer.Add( gridSizer, 0, wx.ALL, 5 )
		
		
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
		
		self.beginSens_radioButton = wx.RadioButton( self, wx.ID_ANY, u"du début", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.beginSens_radioButton.SetValue( True ) 
		sens_boxSizer.Add( self.beginSens_radioButton, 0, wx.ALL, 5 )
		
		self.endSens_radioButton = wx.RadioButton( self, wx.ID_ANY, u"de la fin", wx.DefaultPosition, wx.DefaultSize, 0 )
		sens_boxSizer.Add( self.endSens_radioButton, 0, wx.ALL, 5 )
		
		
		gridSizer.Add( sens_boxSizer, 0, wx.ALL, 0 )
		
		
		boxSizer.Add( gridSizer, 0, wx.ALL, 5 )
		
		
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
	

