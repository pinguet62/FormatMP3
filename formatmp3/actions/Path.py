#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Gestion des noms de fichier
@author: Julien
'''



import os.path
from formatmp3.actions import *



class PathModification(object):
    '''
    Modifier une partie du nom de fichier
    @author: Julien
    '''
    
    
    FILENAME = 1
    EXTENSION = 2
    #BASENAME = FILENAME|EXTENSION
    
    
    def __init__(self, path=None, range=None):
        '''
        Constructeur
        @param path: Chemin du fichier
        @author: Julien
        '''
        self.path = path
        if range is not None and range in [PathModification.FILENAME, PathModification.EXTENSION, PathModification.BASENAME]:
            self.range = range
        else:
            self.range = None
    
    
    def get(self):
        '''
        Obtenir la partie du nom de fichier à modifier
        @return: Chaîne de caractères
        @author: Julien
        '''
        if self.range is PathModification.FILENAME:
            return self.path.filename
        elif self.range is PathModification.EXTENSION:
            return self.path.extension
        #elif self.range is PathModification.BASENAME:
        #    return self.path.basename
        else:
            return None
    
    
    def set(self, newStr):
        '''
        Remplacer la partie du nom de fichier
        @param newStr: Nouvelle chaîne de caractères
        @author: Julien
        '''
        if self.range is PathModification.FILENAME:
            self.path.filename = newStr
        elif self.range is PathModification.EXTENSION:
            self.path.extension = newStr
        #elif self.range is PathModification.BASENAME:
        #    self.path.basename = newStr
        else:
            pass



class Path(object):
    '''
    Nom de fichier
    @author: Julien
    '''
    
    
    def __init__(self, path):
        '''
        Constructeur
        @param path: Path
        @author: Julien
        '''
        self._path = path
    
    
    def get(self):
        '''
        Obtenir le chemin du fichier
        @return: Chemin
        @author: Julien
        '''
        return self._path
    
    
    def set(self, newPath):
        '''
        Spécifier le chemin du fichier
        @param newPath: Chemin
        @author: Julien
        '''
        self._path = newPath
    
    
    def get_dirname(self):
        '''
        Obtenir le répertoire du fichier
        @return: Répertoire
        @author: Julien
        '''
        return os.path.dirname(self._path)
    
    
    def set_dirname(self, newDirname):
        '''
        Spécifier le répertoire du fichier
        @param newDirname: Répertoire
        @author: Julien
        '''
        self._path = os.path.join(newDirname, self.basename)
    
    
    def get_basename(self):
        '''
        Obtenir le nom simple du fichier (avec extension)
        @return: Nom simple
        @author: Julien
        '''
        return os.path.basename(self._path)
    
    
    def set_basename(self, newBasename):
        '''
        Spécifier le nom simple du fichier (avec extension)
        @param newBasename: Nom simple
        @author: Julien
        '''
        self._path = os.path.join(self.dirname, newBasename)
    
    
    def get_filename(self):
        '''
        Obtenir le nom du fichier (sans extension)
        @return: Nom
        @author: Julien
        '''
        return os.path.splitext(self.basename)[0]
    
    
    def set_filename(self, newFilename):
        '''
        Spécifier le nom du fichier (sans extension)
        @param newFilename: Nom
        @author: Julien
        '''
        self._path = os.path.join(self.dirname, newFilename) + "." + self.extension
    
    
    def get_extension(self):
        '''
        Obtenir l'extension du fichier (sans le point)
        @return: Extension
        @author: Julien
        '''
        return os.path.splitext(self._path)[1][1:]
    
    
    def set_extension(self, newExtension):
        '''
        Spécifier l'extension du fichier
        @param extension: Extension
        @author: Julien
        '''
        if newExtension in ['', '.']:
            newExtension = ''
        elif newExtension[0] is not '.':
            newExtension = "." + newExtension
        self._path = os.path.join(self.dirname, self.filename) + newExtension
    
    
    # Propriétés
    dirname = property(fget = get_dirname, fset = set_dirname)
    basename = property(fget = get_basename, fset = set_basename)
    filename = property(fget = get_filename, fset = set_filename)
    extension = property(fget = get_extension, fset = set_extension)
