#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Modèles du pattern MVC
@author: Julien
'''



from formatmp3.actions.Action import *
from wx.lib.pubsub import pub as Publisher
import os.path
import pickle



# Liste des actions de l'application
actions = [CaseChange, ReplaceString, Cut, InsertString]



class Model(object):
    '''
    Modèle de l'interface principale
    Contient les fichiers à modifier et les action à effectuer
    @author: Julien
    '''
    
    
    # Messages de l'interface graphique
    ERROR = "ERROR"
    FILELIST_CHANGED = "FILELIST_CHANGED"
    ACTIONLIST_CHANGED = "ACTIONLIST_CHANGED"
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        self._stop = False
        self.filesave = None
        self.filelist = []
        self.actionlist = []
    
    # Ajout/Suppression de fichiers/répertoire
    
    def _addFile(self, path):
        '''
        Ajouter un fichier
        @param path: path
        @author: Julien
        '''
        if path not in self.filelist:
            self.filelist.append(path)
    
    
    def addFile(self, path):
        '''
        Ajouter un fichier
        @param path: Path
        @author: Julien
        '''
        oldCount = len(self.filelist)
        self._addFile(path)
        newCount = len(self.filelist)
        if oldCount < newCount:
            self.filelist.sort()
            Publisher.sendMessage(Model.FILELIST_CHANGED)
    
    
    def addFiles(self, pathlist=[]):
        '''
        Ajouter des fichiers
        @param pathlist: Liste des path
        @author: Julien
        '''
        oldCount = len(self.filelist)
        for path in pathlist:
            self._addFile(path)
        newCount = len(self.filelist)
        if oldCount < newCount:
            self.filelist.sort()
            Publisher.sendMessage(Model.FILELIST_CHANGED)
    
    
    def _addFolder(self, strDirname):
        '''
        Ajout de chacun des fichiers contenus dans le répertoire de manière récursive
        @param strDirname: Path du répertoire
        @author: Julien
        '''
        for basename in os.listdir(strDirname):
            strPath = os.path.join(strDirname, basename)
            if os.path.isdir(strPath):
                self._addFolder(strPath)
            elif os.path.isfile(strPath):
                path = Path(strPath)
                self._addFile(path)
    
    
    def addFolder(self, path):
        '''
        Ajouter un répertoire
        @param path: Path du répertoire
        @author: Julien
        '''
        oldCount = len(self.filelist)
        self._addFolder(path)
        newCount = len(self.filelist)
        if oldCount < newCount:
            self.filelist.sort()
            Publisher.sendMessage(Model.FILELIST_CHANGED)
    
    
    def removeFiles(self, pathlist=[]):
        '''
        Retirer des fichiers
        @param pathlist: Liste des chemins des fichiers
        @author: Julien
        '''
        filesDeleted = False
        for path in pathlist:
            if path in self.filelist:
                self.filelist.remove(path)
                filesDeleted = True
        if filesDeleted:
            Publisher.sendMessage(Model.FILELIST_CHANGED)
    
    
    def removeAllFiles(self):
        '''
        Retirer tous les fichiers
        @author: Julien
        '''
        if self.filelist:
            self.filelist = []
            Publisher.sendMessage(Model.FILELIST_CHANGED)
    
    
    def AddAction(self, action):
        '''
        Ajouter une action
        @param action: Action
        @author: Julien
        '''
        self.actionlist.append(action)
        Publisher.sendMessage(Model.ACTIONLIST_CHANGED)
    
    
    def getOverviewFilelist(self):
        '''
        Obtenir la liste des fichiers avec l'aperçu des modifications
        @return: Liste des fichiers
        @author: Julien
        '''
        overviews = []
        for path in self.filelist:
            for action in self.actionlist:
                path = action.getOverview(path)
            overviews.append(path)
        return overviews
    
    
    def SwapActions(self, i1, i2):
        '''
        Echanger 2 actions
        @param i1: Indice 1
        @param i2: Indice 2
        @author: Julien
        '''
        self.actionlist[i1], self.actionlist[i2] = self.actionlist[i2], self.actionlist[i1]
        Publisher.sendMessage(Model.ACTIONLIST_CHANGED)
    
    
    def removeAction(self, action):
        '''
        Retirer des fichiers
        @param action: Action
        @author: Julien
        '''
        if action in self.actionlist:
            self.actionlist.remove(action)
            Publisher.sendMessage(Model.ACTIONLIST_CHANGED)
    
    
    def removeAllActions(self):
        '''
        Retirer toutes les actions
        @author: Julien
        '''
        if self.actionlist:
            self.actionlist = []
            Publisher.sendMessage(Model.ACTIONLIST_CHANGED)
    
    # Exécution
    
    def stop(self):
        '''
        Arrêter l'exécution
        @author: Julien
        '''
        self._stop = True
    
    
    def Execute(self):
        '''
        Exécuter les actions sur les fichiers
        @author: Julien
        '''
        for path in self.filelist:
            try:
                for action in self.actionlist:
                    if self._stop:
                        Publisher.sendMessage(Model.FILELIST_CHANGED)
                        return
                    action.execute(path)
            except BaseException, err:
                Publisher.sendMessage(Model.ERROR, error=err)
        Publisher.sendMessage(Model.FILELIST_CHANGED)
        self._stop = True
    
    # Chargement et sauvegarde
    
    def open(self, path):
        '''
        Charger les actions du fichier
        @param path: Fichier d'entrée
        @author: Julien
        '''
        fichier = open(path.get(), 'r')
        self.actionlist = pickle.load(fichier)
        self.filesave = path.get()
        Publisher.sendMessage(Model.ACTIONLIST_CHANGED)
    
    
    def save(self, path):
        '''
        Enregistrer les actions dans un fichier
        @param path: Fichier de sortie
        @author: Julien
        '''
        fichier = open(path.get(), 'w')
        pickle.dump(self.actionlist, fichier)
        fichier.close()
        self.filesave = path



if __name__ == '__main__':
    pass