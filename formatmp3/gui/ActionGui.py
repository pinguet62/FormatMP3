#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Interface graphique de chacune des actions
Permettent de paramétrer les actions
@author: Julien
'''



import wx
from formatmp3.action.Action import *



class ActionGui(wx.Frame):
    '''
    Interface de base des interfaces graphiques
    @author: Julien
    '''
    
    
    def __init__(self, parent):
        '''
        Constructeur
        @param parent: Fenêtre parent
        @author: Julien 
        '''
        wx.Frame.__init__(self, parent)
    
    
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
    
    
    def __init__(self, parent):
        '''
        Constructeur
        @param parent: Fenêtre parent
        @author: Julien
        '''
        ActionGui.__init__(self, parent)
        boxSizer = wx.BoxSizer()
        
        button = wx.Button(self, "CaseChangeGui") # tmp
        boxSizer.Add(button) # tmp



class ReplaceStringGui(ActionGui):
    '''
    Interface graphique de la classe ReplaceString
    @author: Julien
    '''
    
    
    def __init__(self, parent):
        '''
        Constructeur
        @param parent: Fenêtre parent
        @author: Julien
        '''
        ActionGui.__init__(self, parent)
        boxSizer = wx.BoxSizer()
        
        button = wx.Button(self, "ReplaceString") # tmp
        boxSizer.Add(button) # tmp
