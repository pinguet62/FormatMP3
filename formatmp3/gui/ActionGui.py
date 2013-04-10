#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Interface graphique de chacune des actions
Permettent de paramétrer les actions
@author: Julien
'''



import wx
from formatmp3.action.Action import *



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
        boxSizer = wx.BoxSizer()
        self.SetSizer(boxSizer)
        
        button = wx.Button(self, label="CaseChangeGui") # tmp
        boxSizer.Add(button) # tmp



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
        boxSizer = wx.BoxSizer()
        self.SetSizer(boxSizer)
        
        button = wx.Button(self, label="ReplaceString") # tmp
        boxSizer.Add(button) # tmp



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
        boxSizer = wx.BoxSizer()
        self.SetSizer(boxSizer)
        
        button = wx.Button(self, label="Cut") # tmp
        boxSizer.Add(button) # tmp



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
        boxSizer = wx.BoxSizer()
        self.SetSizer(boxSizer)
        
        button = wx.Button(self, label="InsertString") # tmp
        boxSizer.Add(button) # tmp
