#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Interface graphique de chacune des actions
Permettent de paramétrer les actions
@author: Julien
@todo: Mettre ne commun "Appliquer à"
'''



from formatmp3.actions.Action import *
from wx.lib.pubsub import pub as Publisher
import wx



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
    
    
    # Messages des interfaces graphiques des actions
    ACTION_CHANGED = "ACTION_CHANGED"
    
    
    def __init__(self, parent, action):
        '''
        Constructeur
        @param parent: Fenêtre parent
        @param action: Action
        @author: Julien
        '''
        self.action = action
        
        wx.Panel.__init__(self, parent)
        self.boxSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.boxSizer)
        # Title
        title = wx.StaticText(self, label=str(action.__class__.getTitle()))
        font_title = wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92)
        title.SetFont(font_title)
        self.boxSizer.Add(title)
        # Description
        description = wx.StaticText(self, label=str(action.__class__.getDescription()))
        font_description = wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 93, 90)
        description.SetFont(font_description)
        self.boxSizer.Add(description)



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
        
        # Options
        options_staticBoxSizer = wx.StaticBoxSizer(wx.StaticBox(self, label="Options"), wx.VERTICAL)
        self.boxSizer.Add(options_staticBoxSizer)
        #     LOWER
        lower_radioButton = wx.RadioButton(self, label="Tout en minuscule", style=wx.RB_GROUP)
        lower_radioButton.Value = (self.action.modification is CaseChange.LOWER)
        lower_radioButton.Bind(wx.EVT_RADIOBUTTON,
                               lambda event, modification=CaseChange.LOWER:
                                   self.OnModificationChanged(event, modification)
                               )
        options_staticBoxSizer.Add(lower_radioButton, flag=wx.ALL, border=5)
        #     FIRST_MAJ
        firstMaj_radioButton = wx.RadioButton(self, label="Majuscule la première lettre du nom")
        firstMaj_radioButton.Value = (self.action.modification is CaseChange.FIRST_MAJ)
        firstMaj_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                  lambda event, modification=CaseChange.FIRST_MAJ:
                                      self.OnModificationChanged(event, modification)
                                  )
        options_staticBoxSizer.Add(firstMaj_radioButton, flag=wx.ALL, border=5)
        #     TITLE
        title_radioButton = wx.RadioButton(self, label="Majuscule la première lettre de chaque mot")
        title_radioButton.Value = (self.action.modification is CaseChange.TITLE)
        title_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                   lambda event, modification=CaseChange.TITLE:
                                       self.OnModificationChanged(event, modification)
                               )
        options_staticBoxSizer.Add(title_radioButton, flag=wx.ALL, border=5)
        #     UPPER
        upper_radioButton = wx.RadioButton(self, label="Tout en majuscule")
        upper_radioButton.Value = (self.action.modification is CaseChange.UPPER)
        upper_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                    lambda event, modification=CaseChange.UPPER:
                                        self.OnModificationChanged(event, modification)
                               )
        options_staticBoxSizer.Add(upper_radioButton, flag=wx.ALL, border=5)
        # Appliquer à
        appliquerA_staticBoxSizer = wx.StaticBoxSizer(wx.StaticBox(self, label="Appliquer à"), wx.VERTICAL)
        self.boxSizer.Add(appliquerA_staticBoxSizer)
        #     FILENAME
        filename_radioButton = wx.RadioButton(self, label="Nom du fichier", style=wx.RB_GROUP)
        filename_radioButton.Value = (self.action.range is PathModification.FILENAME)
        filename_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                      lambda event, range=PathModification.FILENAME:
                                          self.OnRangeChanged(event, range)
                                  )
        appliquerA_staticBoxSizer.Add(filename_radioButton, flag=wx.ALL, border=5)
        #     EXTENSION
        extension_radioButton = wx.RadioButton(self, label="Extension")
        extension_radioButton.Value = (self.action.range is PathModification.EXTENSION)
        extension_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                       lambda event, range=PathModification.EXTENSION:
                                           self.OnRangeChanged(event, range)
                                   )
        appliquerA_staticBoxSizer.Add(extension_radioButton, flag=wx.ALL, border=5)
    
    
    def OnModificationChanged(self, event, modification):
        '''
        Modification de la modification
        @param event: Événement
        @param modification: Modification
        '''
        self.action.modification = modification
        Publisher.sendMessage(ActionGui.ACTION_CHANGED)
    
    
    def OnRangeChanged(self, event, range):
        '''
        Modification de la partie à modifier
        @param event: Événement
        @param range: Partie
        '''
        self.action.range = range
        Publisher.sendMessage(ActionGui.ACTION_CHANGED)



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
        
        # Options
        options_staticBoxSizer = wx.StaticBoxSizer(wx.StaticBox(self, label="Options"), wx.VERTICAL)
        self.boxSizer.Add(options_staticBoxSizer)
        # Sous-Sizer
        options_gridSizer = wx.GridSizer(0, 2)
        options_staticBoxSizer.Add(options_gridSizer, flag=wx.ALL)
        #     Remplacer...
        #         Title
        remplacer_title = wx.StaticText(self, label="Remplacer : ")
        options_gridSizer.Add(remplacer_title, flag=wx.ALL, border=5)
        #         Valeur
        self.oldStr_textCtrl = wx.TextCtrl(self, value=self.action.oldStr)
        self.oldStr_textCtrl.Bind(wx.EVT_TEXT, self.OnOldStrChanged)
        options_gridSizer.Add(self.oldStr_textCtrl, flag=wx.ALL, border=5)
        #     ...Par
        #         Title
        newStr_title = wx.StaticText(self, label="Par : ")
        options_gridSizer.Add(newStr_title, flag=wx.ALL, border=5)
        #         Valeur
        self.newStr_textCtrl = wx.TextCtrl(self, value=self.action.newStr)
        self.newStr_textCtrl.Bind(wx.EVT_TEXT, self.OnNewStrChanged)
        options_gridSizer.Add(self.newStr_textCtrl, flag=wx.ALL, border=5)
        # Appliquer à
        appliquerA_staticBoxSizer = wx.StaticBoxSizer(wx.StaticBox(self, label="Appliquer à"), wx.VERTICAL)
        self.boxSizer.Add(appliquerA_staticBoxSizer)
        #     FILENAME
        filename_radioButton = wx.RadioButton(self, label="Nom du fichier", style=wx.RB_GROUP)
        filename_radioButton.Value = (self.action.range is PathModification.FILENAME)
        filename_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                      lambda event, range=PathModification.FILENAME:
                                          self.OnRangeChanged(event, range)
                                  )
        appliquerA_staticBoxSizer.Add(filename_radioButton, flag=wx.ALL, border=5)
        #     EXTENSION
        extension_radioButton = wx.RadioButton(self, label="Extension")
        extension_radioButton.Value = (self.action.range is PathModification.EXTENSION)
        extension_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                       lambda event, range=PathModification.EXTENSION:
                                           self.OnRangeChanged(event, range)
                                   )
        appliquerA_staticBoxSizer.Add(extension_radioButton, flag=wx.ALL, border=5)
    
    
    def OnOldStrChanged(self, event):
        '''
        Modification de la chaîne à remplacer
        @param event: Événement
        @author: Julien
        '''
        self.action.oldStr = self.oldStr_textCtrl.Value
        Publisher.sendMessage(ActionGui.ACTION_CHANGED)
    
    
    def OnNewStrChanged(self, event):
        '''
        Modification de la nouvelle chaîne
        @param event: Événement
        @author: Julien
        '''
        self.action.newStr = self.newStr_textCtrl.Value
        Publisher.sendMessage(ActionGui.ACTION_CHANGED)
    
    
    def OnRangeChanged(self, event, range):
        '''
        Modification de la partie à modifier
        @param event: Événement
        @param range: Partie
        '''
        self.action.range = range
        Publisher.sendMessage(ActionGui.ACTION_CHANGED)



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
        
        # Options
        options_staticBoxSizer = wx.StaticBoxSizer(wx.StaticBox(self, label="Options"), wx.VERTICAL)
        self.boxSizer.Add(options_staticBoxSizer)
        # Sous-Sizer
        options_gridSizer = wx.GridSizer(0, 2)
        options_staticBoxSizer.Add(options_gridSizer, flag=wx.ALL)
        # Nombre de caractères
        #     Title
        nomber_staticText = wx.StaticText(self, label="Nombre de caractères à supprimer : ")
        options_gridSizer.Add(nomber_staticText, flag=wx.ALL, border=5)
        #     Valeur
        self.number_spinCtrl = wx.SpinCtrl(self, value=str(self.action.nomber))
        self.number_spinCtrl.Bind(wx.EVT_SPINCTRL, self.OnNomberChanged)
        options_gridSizer.Add(self.number_spinCtrl, flag=wx.ALL, border=5)
        # Position
        #     Title
        position_staticText = wx.StaticText(self, label="A partir de la position : ")
        options_gridSizer.Add(position_staticText, flag=wx.ALL, border=5)
        #     Valeur
        self.position_spinCtrl = wx.SpinCtrl(self, value=str(self.action.position))
        self.position_spinCtrl.Bind(wx.EVT_SPINCTRL, self.OnPositionChanged)
        options_gridSizer.Add(self.position_spinCtrl, flag=wx.ALL, border=5)
        # Sens
        #     Title
        sens_staticText = wx.StaticText(self, label="En partant : ")
        options_gridSizer.Add(sens_staticText, flag=wx.ALL, border=5)
        #     Valeur
        sens_boxSizer = wx.BoxSizer()
        options_gridSizer.Add(sens_boxSizer, flag=wx.ALL)
        #         Début
        self.beginSens_radioButton = wx.RadioButton(self, label="du début", style=wx.RB_GROUP)
        self.beginSens_radioButton.Value = self.action.sens
        self.beginSens_radioButton.Bind(wx.EVT_RADIOBUTTON, self.OnSensChanged)
        sens_boxSizer.Add(self.beginSens_radioButton, flag=wx.ALL, border=5)
        #         Fin
        endSens_radioButton = wx.RadioButton(self, label="de la fin")
        endSens_radioButton.Value = not self.action.sens
        endSens_radioButton.Bind(wx.EVT_RADIOBUTTON, self.OnSensChanged)
        sens_boxSizer.Add(endSens_radioButton, flag=wx.ALL, border=5)
        # Appliquer à
        appliquerA_staticBoxSizer = wx.StaticBoxSizer(wx.StaticBox(self, label="Appliquer à"), wx.VERTICAL)
        self.boxSizer.Add(appliquerA_staticBoxSizer)
        #     FILENAME
        filename_radioButton = wx.RadioButton(self, label="Nom du fichier", style=wx.RB_GROUP)
        filename_radioButton.Value = (self.action.range is PathModification.FILENAME)
        filename_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                      lambda event, range=PathModification.FILENAME:
                                          self.OnRangeChanged(event, range)
                                  )
        appliquerA_staticBoxSizer.Add(filename_radioButton, flag=wx.ALL, border=5)
        #     EXTENSION
        extension_radioButton = wx.RadioButton(self, label="Extension")
        extension_radioButton.Value = (self.action.range is PathModification.EXTENSION)
        extension_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                       lambda event, range=PathModification.EXTENSION:
                                           self.OnRangeChanged(event, range)
                                   )
        appliquerA_staticBoxSizer.Add(extension_radioButton, flag=wx.ALL, border=5)
    
    
    def OnNomberChanged(self, event):
        '''
        Modification du nombre de caractères
        @param event: Événement
        @author: Julien
        '''
        self.action.nomber = self.number_spinCtrl.Value
        Publisher.sendMessage(ActionGui.ACTION_CHANGED)
    
    
    def OnPositionChanged(self, event):
        '''
        Modification de la position
        @param event: Événement
        @author: Julien
        '''
        self.action.position = self.position_spinCtrl.Value
        Publisher.sendMessage(ActionGui.ACTION_CHANGED)
    
    
    def OnSensChanged(self, event):
        '''
        Modification du sens
        @param event: Événement
        @author: Julien
        '''
        self.action.sens = self.beginSens_radioButton.Value
        Publisher.sendMessage(ActionGui.ACTION_CHANGED)
    
    
    def OnRangeChanged(self, event, range):
        '''
        Modification de la partie à modifier
        @param event: Événement
        @param range: Partie
        '''
        self.action.range = range
        Publisher.sendMessage(ActionGui.ACTION_CHANGED)



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
        
        # Options
        options_staticBoxSizer = wx.StaticBoxSizer(wx.StaticBox(self, label="Options"), wx.VERTICAL)
        self.boxSizer.Add(options_staticBoxSizer)
        # Sous-Sizer
        options_gridSizer = wx.GridSizer(0, 2)
        options_staticBoxSizer.Add(options_gridSizer, flag=wx.ALL)
        # Chaîne à insérer
        #     Title
        string_staticText = wx.StaticText(self, label="Chaîne à insérer : ")
        options_gridSizer.Add(string_staticText, flag=wx.ALL, border=5)
        #     Valeur
        self.string_textCtrl = wx.TextCtrl(self, value=self.action.string)
        self.string_textCtrl.Bind(wx.EVT_TEXT, self.OnStringChanged)
        options_gridSizer.Add(self.string_textCtrl, flag=wx.ALL, border=5)
        # Position
        #     Title
        position_staticText = wx.StaticText(self, label="A partir de la position : ")
        options_gridSizer.Add(position_staticText, flag=wx.ALL, border=5)
        #     Valeur
        self.position_spinCtrl = wx.SpinCtrl(self, value=str(self.action.position))
        self.position_spinCtrl.Bind(wx.EVT_SPINCTRL, self.OnPositionChanged)
        options_gridSizer.Add(self.position_spinCtrl, flag=wx.ALL, border=5)
        # Sens
        #     Title
        sens_staticText = wx.StaticText(self, label="A partir : ")
        options_gridSizer.Add(sens_staticText, flag=wx.ALL, border=5)
        #     Valeur
        sens_boxSizer = wx.BoxSizer()
        options_gridSizer.Add(sens_boxSizer, flag=wx.ALL)
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
        # Appliquer à
        appliquerA_staticBoxSizer = wx.StaticBoxSizer(wx.StaticBox(self, label="Appliquer à"), wx.VERTICAL)
        self.boxSizer.Add(appliquerA_staticBoxSizer)
        #     FILENAME
        filename_radioButton = wx.RadioButton(self, label="Nom du fichier", style=wx.RB_GROUP)
        filename_radioButton.Value = (self.action.range is PathModification.FILENAME)
        filename_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                      lambda event, range=PathModification.FILENAME:
                                          self.OnRangeChanged(event, range)
                                  )
        appliquerA_staticBoxSizer.Add(filename_radioButton, flag=wx.ALL, border=5)
        #     EXTENSION
        extension_radioButton = wx.RadioButton(self, label="Extension")
        extension_radioButton.Value = (self.action.range is PathModification.EXTENSION)
        extension_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                       lambda event, range=PathModification.EXTENSION:
                                           self.OnRangeChanged(event, range)
                                   )
        appliquerA_staticBoxSizer.Add(extension_radioButton, flag=wx.ALL, border=5)
    
    
    def OnStringChanged(self, event):
        '''
        Modification de la chaîne à insérer
        @param event: Événement
        @author: Julien
        '''
        self.action.string = self.string_textCtrl.Value
        Publisher.sendMessage(ActionGui.ACTION_CHANGED)
    
    
    def OnPositionChanged(self, event):
        '''
        Modification de la position
        @param event: Événement
        @author: Julien
        '''
        self.action.position = self.position_spinCtrl.Value
        Publisher.sendMessage(ActionGui.ACTION_CHANGED)
    
    
    def OnSensChanged(self, event):
        '''
        Modification du sens
        @param event: Événement
        @author: Julien
        '''
        self.action.sens = self.beginSens_radioButton.Value
        Publisher.sendMessage(ActionGui.ACTION_CHANGED)
    
    
    def OnRangeChanged(self, event, range):
        '''
        Modification de la partie à modifier
        @param event: Événement
        @param range: Partie
        '''
        self.action.range = range
        Publisher.sendMessage(ActionGui.ACTION_CHANGED)



if __name__ == "__main__":
    pass