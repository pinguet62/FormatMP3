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
                                   self.OnModificationChanged(event, modification))
        options_staticBoxSizer.Add(lower_radioButton, flag=wx.ALL, border=5)
        #     FIRST_MAJ
        firstMaj_radioButton = wx.RadioButton(self, label="Majuscule la première lettre du nom")
        firstMaj_radioButton.Value = (self.action.modification is CaseChange.FIRST_MAJ)
        firstMaj_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                  lambda event, modification=CaseChange.FIRST_MAJ:
                                      self.OnModificationChanged(event, modification))
        options_staticBoxSizer.Add(firstMaj_radioButton, flag=wx.ALL, border=5)
        #     TITLE
        title_radioButton = wx.RadioButton(self, label="Majuscule la première lettre de chaque mot")
        title_radioButton.Value = (self.action.modification is CaseChange.TITLE)
        title_radioButton.Bind(wx.EVT_RADIOBUTTON,
                               lambda event, modification=CaseChange.TITLE:
                                   self.OnModificationChanged(event, modification))
        options_staticBoxSizer.Add(title_radioButton, flag=wx.ALL, border=5)
        #     UPPER
        upper_radioButton = wx.RadioButton(self, label="Tout en majuscule")
        upper_radioButton.Value = (self.action.modification is CaseChange.UPPER)
        upper_radioButton.Bind(wx.EVT_RADIOBUTTON,
                               lambda event, modification=CaseChange.UPPER:
                                   self.OnModificationChanged(event, modification))
        options_staticBoxSizer.Add(upper_radioButton, flag=wx.ALL, border=5)
        # Appliquer à
        appliquerA_staticBoxSizer = wx.StaticBoxSizer(wx.StaticBox(self, label="Appliquer à"), wx.VERTICAL)
        self.boxSizer.Add(appliquerA_staticBoxSizer)
        #     FILENAME
        filename_radioButton = wx.RadioButton(self, label="Nom du fichier", style=wx.RB_GROUP)
        filename_radioButton.Value = (self.action.range is PathModification.FILENAME)
        filename_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                  lambda event, range=PathModification.FILENAME:
                                      self.OnRangeChanged(event, range))
        appliquerA_staticBoxSizer.Add(filename_radioButton, flag=wx.ALL, border=5)
        #     EXTENSION
        extension_radioButton = wx.RadioButton(self, label="Extension")
        extension_radioButton.Value = (self.action.range is PathModification.EXTENSION)
        extension_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                   lambda event, range=PathModification.EXTENSION:
                                       self.OnRangeChanged(event, range))
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
                                      self.OnRangeChanged(event, range))
        appliquerA_staticBoxSizer.Add(filename_radioButton, flag=wx.ALL, border=5)
        #     EXTENSION
        extension_radioButton = wx.RadioButton(self, label="Extension")
        extension_radioButton.Value = (self.action.range is PathModification.EXTENSION)
        extension_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                   lambda event, range=PathModification.EXTENSION:
                                       self.OnRangeChanged(event, range))
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
                                      self.OnRangeChanged(event, range))
        appliquerA_staticBoxSizer.Add(filename_radioButton, flag=wx.ALL, border=5)
        #     EXTENSION
        extension_radioButton = wx.RadioButton(self, label="Extension")
        extension_radioButton.Value = (self.action.range is PathModification.EXTENSION)
        extension_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                   lambda event, range=PathModification.EXTENSION:
                                       self.OnRangeChanged(event, range))
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
                                      self.OnRangeChanged(event, range))
        appliquerA_staticBoxSizer.Add(filename_radioButton, flag=wx.ALL, border=5)
        #     EXTENSION
        extension_radioButton = wx.RadioButton(self, label="Extension")
        extension_radioButton.Value = (self.action.range is PathModification.EXTENSION)
        extension_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                   lambda event, range=PathModification.EXTENSION:
                                       self.OnRangeChanged(event, range))
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



class UpdateTagsGui(ActionGui):
    '''
    Interface graphique de la classe UpdateTags
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
        description_staticBoxSizer = wx.StaticBoxSizer(wx.StaticBox(self, label="Options"), wx.VERTICAL)
        self.boxSizer.Add(description_staticBoxSizer)
        # Sous-Sizer
        description_gridSizer = wx.GridSizer(0, 2)
        description_staticBoxSizer.Add(description_gridSizer, flag=wx.ALL)
        #     Titre
        #         Title
        title_checkBox = wx.CheckBox(self, label="Titre : ")
        title_checkBox.Value = self.action.title is not None
        title_checkBox.Bind(wx.EVT_CHECKBOX, self.OnTitleActived)
        description_gridSizer.Add(title_checkBox, flag=wx.ALL, border=5)
        #         Valeur
        choix_title_comboBox = [wx.EmptyString, UpdateTags.AUTO, UpdateTags.FILENAME]
        self.title_comboBox = wx.ComboBox(self, choices=choix_title_comboBox)
        if self.action.title is None:
            self.title_comboBox.Enabled = False
        else:
            self.title_comboBox.Value = self.action.title
        self.title_comboBox.Bind(wx.EVT_TEXT, self.OnTitleChanged)
        description_gridSizer.Add(self.title_comboBox, flag=wx.ALL, border=5)
        #     Sous-titre
        #         Title
        subtitle_checkBox = wx.CheckBox(self, label="Sous-titre : ")
        subtitle_checkBox.Value = self.action.subtitle is not None
        subtitle_checkBox.Bind(wx.EVT_CHECKBOX, self.OnSubtitleActived)
        description_gridSizer.Add(subtitle_checkBox, flag=wx.ALL, border=5)
        #         Valeur
        self.subtitle_textCtrl = wx.TextCtrl(self)
        if self.action.subtitle is None:
            self.subtitle_textCtrl.Enabled = False
        else:
            self.subtitle_textCtrl.Value = self.action.subtitle
        self.subtitle_textCtrl.Bind(wx.EVT_TEXT, self.OnSubtitleChanged)
        description_gridSizer.Add(self.subtitle_textCtrl, flag=wx.ALL, border=5)
        #     Notation
        #         Titre
        notation_checkBox = wx.CheckBox(self, label="Notation : ")
        notation_checkBox.Enabled = False # tmp
        notation_checkBox.Value = self.action.notation is not None
        notation_checkBox.Bind(wx.EVT_CHECKBOX, self.OnNotationActived)
        description_gridSizer.Add(notation_checkBox, flag=wx.ALL, border=5)
        #         Valueur
        #             Panel
        self.valeur_notation_panel = wx.Panel(self)
        self.valeur_notation_panel.Enabled = False # tmp
        if self.action.notation is None:
            self.valeur_notation_panel.Enabled = False
        self.valeur_notation_panel.Bind(wx.EVT_LEFT_UP,
                                        lambda event:
                                            self.resetNotation())
        description_gridSizer.Add(self.valeur_notation_panel, flag=wx.ALL)
        #             Sizer
        valeur_notation_boxSizer = wx.BoxSizer()
        self.valeur_notation_panel.SetSizer(valeur_notation_boxSizer)
        #             .
        valeur_notation_boxSizer.AddSpacer((10,0), flag=wx.ALL)
        #             1
        self.notation_1_radioButton = wx.RadioButton(self.valeur_notation_panel, style=wx.RB_GROUP)
        self.notation_1_radioButton.Value = False
        if self.action.notation == 1:
            self.notation_1_radioButton.Value = True
        self.notation_1_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                         lambda event:
                                             self.updateNotation())
        valeur_notation_boxSizer.Add(self.notation_1_radioButton, flag=wx.ALL, border=5)
        #             2
        self.notation_2_radioButton = wx.RadioButton(self.valeur_notation_panel)
        if self.action.notation == 2:
            self.notation_2_radioButton.Value = True
        self.notation_2_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                         lambda event:
                                             self.updateNotation())
        valeur_notation_boxSizer.Add(self.notation_2_radioButton, flag=wx.ALL, border=5)
        #             3
        self.notation_3_radioButton = wx.RadioButton(self.valeur_notation_panel)
        if self.action.notation == 3:
            self.notation_3_radioButton.Value = True
        self.notation_3_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                         lambda event:
                                             self.updateNotation())
        valeur_notation_boxSizer.Add(self.notation_3_radioButton, flag=wx.ALL, border=5)
        #             4
        self.notation_4_radioButton = wx.RadioButton(self.valeur_notation_panel)
        if self.action.notation == 4:
            self.notation_4_radioButton.Value = True
        self.notation_4_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                         lambda event:
                                             self.updateNotation())
        valeur_notation_boxSizer.Add(self.notation_4_radioButton, flag=wx.ALL, border=5)
        #             5
        self.notation_5_radioButton = wx.RadioButton(self.valeur_notation_panel)
        if self.action.notation == 5:
            self.notation_5_radioButton.Value = True
        self.notation_5_radioButton.Bind(wx.EVT_RADIOBUTTON,
                                         lambda event:
                                             self.updateNotation())
        valeur_notation_boxSizer.Add(self.notation_5_radioButton, flag=wx.ALL, border=5)
    
    
    def OnTitleActived(self, event):
        '''
        Activation de la modification du titre
        @param event: Événement
        @author: Julien
        '''
        if event.IsChecked():
            self.title_comboBox.Enabled = True
            self.action.title = self.title_comboBox.Value
        else:
            self.title_comboBox.Enabled = False
            self.action.title = None
    
    
    def OnTitleChanged(self, event):
        '''
        Modifitation du titre
        @param event: Événement
        @author: Julien
        '''
        self.action.title = event.GetString()
    
    
    def OnSubtitleActived(self, event):
        '''
        Activation de la modification du sous-titre
        @param event: Événement
        @author: Julien
        '''
        if event.IsChecked():
            self.subtitle_textCtrl.Enabled = True
            self.action.title = self.title_comboBox.Value
        else:
            self.subtitle_textCtrl.Enabled = False
            self.action.subtitle = None
    
    
    def OnSubtitleChanged(self, event):
        '''
        Modifitation du titre
        @param event: Événement
        @author: Julien
        '''
        self.action.subtitle = event.GetString()
    
    
    def OnNotationActived(self, event):
        '''
        Activation de la modification de la notation
        @param event: Événement
        @author: Julien
        '''
        if event.IsChecked():
            self.valeur_notation_panel.Enabled = True
            self.updateNotation()
        else:
            self.valeur_notation_panel.Enabled = False
            self.action.notation = None
    
    
    def resetNotation(self):
        '''
        Mise à jour de la notation vers 0
        @author: Julien
        '''
        print "ok"
        self.notation_1_radioButton.Value = False
        self.notation_2_radioButton.Value = False
        self.notation_3_radioButton.Value = False
        self.notation_4_radioButton.Value = False
        self.notation_5_radioButton.Value = False
        self.action.notation = 0
    
    
    def updateNotation(self):
        '''
        Mise à jour de la notation
        @author: Julien
        '''
        if self.notation_1_radioButton.Value:
            self.action.notation = 1
        elif self.notation_2_radioButton.Value:
            self.action.notation = 2
        elif self.notation_3_radioButton.Value:
            self.action.notation = 3
        elif self.notation_4_radioButton.Value:
            self.action.notation = 4
        elif self.notation_5_radioButton.Value:
            self.action.notation = 5
        else:
            self.action.notation = 0



if __name__ == "__main__":
    app = wx.App(False)
    import main
    controller = main.Controller(app)
    app.MainLoop()