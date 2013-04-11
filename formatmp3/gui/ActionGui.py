#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Interface graphique de chacune des actions
Permettent de paramétrer les actions
@author: Julien
'''



import wx
from wx.lib.pubsub import pub as Publisher
from formatmp3.action.Action import *



# Messages des interfaces graphiques des actions
ACTION_CHANGED = "ACTION_CHANGED"



def createGui(parent, action):
    '''
    Créer l'interface graphique correspondante à l'action
    @param parent: Fenêtre parent
    @param action: Action
    @return: Interface graphique
    @author: Julien
    '''
    actionGuiClass = eval(action.__class__.__name__ + "Gui")
    return actionGuiClass(parent, action)



class ActionGui(wx.Panel):
    '''
    Interface de base des interfaces graphiques
    @author: Julien
    '''
    
    
    def __init__(self, parent, action):
        '''
        Constructeur
        @param parent: Fenêtre parent
        @param action: Action
        @author: Julien
        '''
        self._action = action
        
        wx.Panel.__init__(self, parent)
        self.boxSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.boxSizer)
        # Title
        title = wx.StaticText(self, label=action.__class__.getTitle())
        font_title = wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92)
        title.SetFont(font_title)
        self.boxSizer.Add(title)
        # Description
        description = wx.StaticText(self, label=action.__class__.getDescription())
        self.boxSizer.Add(description)
    
    
    def get_action(self):
        '''
        Obtenir l'action
        @return: Action
        @author: Julien
        '''
        return self._action
    
    
    def set_action(self, action):
        '''
        Spécifier l'action
        @param action: Action
        @author: Julien
        '''
        self._action = action
    
    
    # Propriétés
    action = property(fget = get_action, fset = set_action)



class CaseChangeGui(ActionGui):
    '''
    Interface graphique de la classe CaseChange
    @author: Julien
    '''
    
    
    def __init__(self, parent, action):
        '''
        Constructeur
        @param parent: Fenêtre parent
        @param action: Action
        @author: Julien
        '''
        ActionGui.__init__(self, parent, action)



class ReplaceStringGui(ActionGui):
    '''
    Interface graphique de la classe ReplaceString
    @author: Julien
    '''
    
    
    def __init__(self, parent, action):
        '''
        Constructeur
        @param parent: Fenêtre parent
        @param action: Action
        @author: Julien
        '''
        ActionGui.__init__(self, parent, action)
        gridSizer = wx.GridSizer(0, 2)
        self.boxSizer.Add(gridSizer)
        # Remplacer...
        #     Title
        remplacer_title = wx.StaticText(self, label="Remplacer : ")
        gridSizer.Add(remplacer_title, flag=wx.ALL, border=5)
        #     Valeur
        self.oldStr_textCtrl = wx.TextCtrl(self, value=self.action.oldStr)
        self.oldStr_textCtrl.Bind(wx.EVT_TEXT, self.OnOldStrChanged)
        gridSizer.Add(self.oldStr_textCtrl, flag=wx.ALL, border=5)
        # ...Par
        #     Title
        newStr_title = wx.StaticText(self, label="Par : ")
        gridSizer.Add(newStr_title, flag=wx.ALL, border=5)
        #     Valeur
        self.newStr_textCtrl = wx.TextCtrl(self, value=self.action.newStr)
        self.newStr_textCtrl.Bind(wx.EVT_TEXT, self.OnNewStrChanged)
        gridSizer.Add(self.newStr_textCtrl, flag=wx.ALL, border=5)
    
    
    def OnOldStrChanged(self, event):
        '''
        Modification de la chaîne à remplacer
        @param event: Événement
        @author: Julien
        '''
        self.action.oldStr = self.oldStr_textCtrl.Value
        Publisher.sendMessage(ACTION_CHANGED)
    
    
    def OnNewStrChanged(self, event):
        '''
        Modification de la nouvelle chaîne
        @param event: Événement
        @author: Julien
        '''
        self.action.newStr = self.newStr_textCtrl.Value
        Publisher.sendMessage(ACTION_CHANGED)



class CutGui(ActionGui):
    '''
    Interface graphique de la classe Cut
    @author: Julien
    '''
    
    
    def __init__(self, parent, action):
        '''
        Constructeur
        @param parent: Fenêtre parent
        @param action: Action
        @author: Julien
        '''
        ActionGui.__init__(self, parent, action)
        gridSizer = wx.GridSizer(0, 2)
        self.boxSizer.Add(gridSizer)
        # Nombre de caractères
        #     Title
        nomber_staticText = wx.StaticText(self, label="Nombre de caractères à supprimer : ")
        gridSizer.Add(nomber_staticText, flag=wx.ALL, border=5)
        #     Valeur
        self.number_spinCtrl = wx.SpinCtrl(self, value=str(self.action.nombre))
        self.number_spinCtrl.Bind(wx.EVT_SPINCTRL, self.OnNomberChanged)
        gridSizer.Add(self.number_spinCtrl, flag=wx.ALL, border=5)
        # Position
        #     Title
        position_staticText = wx.StaticText(self, label="A partir de la position : ")
        gridSizer.Add(position_staticText, flag=wx.ALL, border=5)
        #     Valeur
        self.position_spinCtrl = wx.SpinCtrl(self, value=str(self.action.position))
        self.position_spinCtrl.Bind(wx.EVT_SPINCTRL, self.OnPositionChanged)
        gridSizer.Add(self.position_spinCtrl, flag=wx.ALL, border=5)
        # Sens
        #     Title
        sens_staticText = wx.StaticText(self, label="En partant : ")
        gridSizer.Add(sens_staticText, flag=wx.ALL, border=5)
        #     Valeur
        sens_boxSizer = wx.BoxSizer()
        gridSizer.Add(sens_boxSizer, flag=wx.ALL)
        #         Début
        self.beginSens_radioButton = wx.RadioButton(self, label="du début")
        self.beginSens_radioButton.Value = self.action.sens
        self.beginSens_radioButton.Bind(wx.EVT_RADIOBUTTON, self.OnSensChanged)
        sens_boxSizer.Add(self.beginSens_radioButton, flag=wx.ALL, border=5)
        #         Fin
        endSens_radioButton = wx.RadioButton(self, label="de la fin")
        endSens_radioButton.Value = not self.action.sens
        endSens_radioButton.Bind(wx.EVT_RADIOBUTTON, self.OnSensChanged)
        sens_boxSizer.Add(endSens_radioButton, flag=wx.ALL, border=5)
    
    
    def OnNomberChanged(self, event):
        '''
        Modification du nombre de caractères
        @param event: Événement
        @author: Julien
        '''
        self.action.nombre = self.number_spinCtrl.Value
        Publisher.sendMessage(ACTION_CHANGED)
    
    
    def OnPositionChanged(self, event):
        '''
        Modification de la position
        @param event: Événement
        @author: Julien
        '''
        self.action.position = self.position_spinCtrl.Value
        Publisher.sendMessage(ACTION_CHANGED)
    
    
    def OnSensChanged(self, event):
        '''
        Modification du sens
        @param event: Événement
        @author: Julien
        '''
        self.action.sens = self.beginSens_radioButton.Value
        Publisher.sendMessage(ACTION_CHANGED)



class InsertStringGui(ActionGui):
    '''
    Interface graphique de la classe InsertString
    @author: Julien
    '''
    
    
    def __init__(self, parent, action):
        '''
        Constructeur
        @param parent: Fenêtre parent
        @param action: Action
        @author: Julien
        '''
        ActionGui.__init__(self, parent, action)
        gridSizer = wx.GridSizer(0, 2)
        self.boxSizer.Add(gridSizer)
        # Chaîne à insérer
        #     Title
        string_staticText = wx.StaticText(self, label="Chaîne à insérer : ")
        gridSizer.Add(string_staticText, flag=wx.ALL, border=5)
        #     Valeur
        self.string_textCtrl = wx.TextCtrl(self, value=self.action.string)
        self.string_textCtrl.Bind(wx.EVT_TEXT, self.OnStringChanged)
        gridSizer.Add(self.string_textCtrl, flag=wx.ALL, border=5)
        # Position
        #     Title
        position_staticText = wx.StaticText(self, label="A partir de la position : ")
        gridSizer.Add(position_staticText, flag=wx.ALL, border=5)
        #     Valeur
        self.position_spinCtrl = wx.SpinCtrl(self, value=str(self.action.position))
        self.position_spinCtrl.Bind(wx.EVT_SPINCTRL, self.OnPositionChanged)
        gridSizer.Add(self.position_spinCtrl, flag=wx.ALL, border=5)
        # Sens
        #     Title
        sens_staticText = wx.StaticText(self, label="A partir : ")
        gridSizer.Add(sens_staticText, flag=wx.ALL, border=5)
        #     Valeur
        sens_boxSizer = wx.BoxSizer()
        gridSizer.Add(sens_boxSizer, flag=wx.ALL)
        #         Début
        self.beginSens_radioButton = wx.RadioButton(self, label="du début")
        self.beginSens_radioButton.Value = self.action.sens
        self.beginSens_radioButton.Bind(wx.EVT_RADIOBUTTON, self.OnSensChanged)
        sens_boxSizer.Add(self.beginSens_radioButton, flag=wx.ALL, border=5)
        #         Fin
        endSens_radioButton = wx.RadioButton(self, label="de la fin")
        endSens_radioButton.Value = not self.action.sens
        endSens_radioButton.Bind(wx.EVT_RADIOBUTTON, self.OnSensChanged)
        sens_boxSizer.Add(endSens_radioButton, flag=wx.ALL, border=5)
    
    
    def OnStringChanged(self, event):
        '''
        Modification de la chaîne à insérer
        @param event: Événement
        @author: Julien
        '''
        self.action.string = self.string_textCtrl.Value
        Publisher.sendMessage(ACTION_CHANGED)
    
    
    def OnPositionChanged(self, event):
        '''
        Modification de la position
        @param event: Événement
        @author: Julien
        '''
        self.action.position = self.position_spinCtrl.Value
        Publisher.sendMessage(ACTION_CHANGED)
    
    
    def OnSensChanged(self, event):
        '''
        Modification du sens
        @param event: Événement
        @author: Julien
        '''
        self.action.sens = self.beginSens_radioButton.Value
        Publisher.sendMessage(ACTION_CHANGED)
