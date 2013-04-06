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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 576,702 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		
		self.listFiles_toolbar = wx.ToolBar( self.listFiles_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_FLAT|wx.TB_HORZ_TEXT ) 
		self.listFiles_toolbar.AddLabelTool( wx.ID_ANY, u"Ajouter un fichier", wx.Bitmap( u"../formatmp3/gui/icons/add_file.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Ajouter un fichier dans la liste", wx.EmptyString, None ) 
		
		self.listFiles_toolbar.AddLabelTool( wx.ID_ANY, u"Ajouter un répertoire", wx.Bitmap( u"../formatmp3/gui/icons/add_folder.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Ajouter une répertoire dans la liste", wx.EmptyString, None ) 
		
		self.listFiles_toolbar.AddLabelTool( wx.ID_ANY, u"Supprimer la sélection", wx.Bitmap( u"../formatmp3/gui/icons/delete.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Supprimer les fichiers sélectionnés de la liste", wx.EmptyString, None ) 
		
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
		self.m_toolBar4.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar4.AddLabelTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar4.Realize() 
		
		listActions_boxSizer.Add( self.m_toolBar4, 0, wx.EXPAND, 5 )
		
		listActionsToDo_listBoxChoices = []
		self.listActionsToDo_listBox = wx.ListBox( self.listActions_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listActionsToDo_listBoxChoices, 0 )
		listActions_boxSizer.Add( self.listActionsToDo_listBox, 1, wx.ALL|wx.EXPAND, 5 )
		
		listActions_action_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		listActions_options_boxSizer = wx.BoxSizer( wx.VERTICAL )
		
		listAvailableActions_choiceChoices = []
		self.listAvailableActions_choice = wx.Choice( self.listActions_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listAvailableActions_choiceChoices, 0 )
		self.listAvailableActions_choice.SetSelection( 0 )
		listActions_options_boxSizer.Add( self.listAvailableActions_choice, 0, wx.ALL, 5 )
		
		self.addChosenAction_button = wx.Button( self.listActions_panel, wx.ID_ANY, u"Ajouter", wx.DefaultPosition, wx.DefaultSize, 0 )
		listActions_options_boxSizer.Add( self.addChosenAction_button, 0, wx.ALL, 5 )
		
		self.deleteSelectedAction_button = wx.Button( self.listActions_panel, wx.ID_ANY, u"Supprimer", wx.DefaultPosition, wx.DefaultSize, 0 )
		listActions_options_boxSizer.Add( self.deleteSelectedAction_button, 0, wx.ALL, 5 )
		
		
		listActions_action_sizer.Add( listActions_options_boxSizer, 0, wx.ALL, 0 )
		
		self.selectedAction_panel = wx.Panel( self.listActions_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		listActions_action_sizer.Add( self.selectedAction_panel, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		listActions_boxSizer.Add( listActions_action_sizer, 0, wx.ALL|wx.EXPAND, 0 )
		
		
		self.listActions_panel.SetSizer( listActions_boxSizer )
		self.listActions_panel.Layout()
		listActions_boxSizer.Fit( self.listActions_panel )
		self.splitter.SplitHorizontally( self.listFiles_panel, self.listActions_panel, 405 )
		mainSizer.Add( self.splitter, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( mainSizer )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
	def splitterOnIdle( self, event ):
		self.splitter.SetSashPosition( 405 )
		self.splitter.Unbind( wx.EVT_IDLE )
	

