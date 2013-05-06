#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Action sur les fichiers
@author: Julien
'''



from formatmp3.actions.Path import *
import copy
import eyed3
import os



class Action(object):
    '''
    Définition des méthodes du pattern stratégie.
    @author: Julien
    '''
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
    
    # Informations
    
    @staticmethod
    def getTitle():
        '''
        Obtenir le titre de l'action
        @return: Titre
        @raise: NotImplementedError Méthode non surchargée
        @author: Julien
        '''
        raise NotImplementedError()
    
    
    @staticmethod
    def getDescription():
        '''
        Obtenir la description de l'action
        @return: Description
        @raise: NotImplementedError Méthode non surchargée
        @author: Julien
        '''
        return NotImplementedError()
    
    # Exécution
    
    def getOverview(self, oldPath):
        '''
        Obtenir l'aperçu de la modification
        @param oldPath: Chemin du fichier
        @return: Chemin du fichier modifié
        @raise: NotImplementedError Méthode non surchargée
        @author: Julien
        '''
        raise NotImplementedError()
    
    
    def execute(self, path):
        '''
        Exécuter la modification
        @param path: Chemin du fichier (modifié après exécution)
        @raise: NotImplementedError Méthode non surchargée
        @author: Julien
        '''
        raise NotImplementedError()



class CaseChange(Action):
    '''
    Modifier le nom du fichier : mettre en majuscule, minuscules, ...
    @author: Julien
    '''
    
    
    # Modifications possibles
    LOWER = 1
    FIRST_MAJ = 2
    TITLE = 4
    UPPER = 8
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        Action.__init__(self)
        
        self.range = PathModification.FILENAME
        self.modification = CaseChange.FIRST_MAJ
    
    # Informations
    
    @staticmethod
    def getTitle():
        '''
        Obtenir le titre de l'action
        @return: Titre
        @author: Julien
        '''
        return "Changement de case"
    
    
    @staticmethod
    def getDescription():
        '''
        Obtenir la description de l'action
        @return: Description
        @author: Julien
        '''
        return "Mettre en minuscule, majuscule, ... le nom du fichier"
    
    # Exécution
    
    def getOverview(self, oldPath):
        '''
        Obtenir l'aperçu de la modification
        @param oldPath: Chemin du fichier
        @return: Chemin du fichier modifié
        @raise: NotImplementedError Méthode non surchargée
        @author: Julien
        '''
        # Partie à modifier
        pModif = PathModification()
        pModif.path = copy.deepcopy(oldPath)
        pModif.range = self.range
        newStr = pModif.get()
        # Modification
        if self.modification is CaseChange.LOWER:
            newStr = newStr.lower()
        elif self.modification is CaseChange.FIRST_MAJ:
            if len(newStr) is not 0:
                newStr = newStr[0].upper() + newStr[1:].lower()
        elif self.modification is CaseChange.TITLE:
            newStr = newStr.title()
        elif self.modification is CaseChange.UPPER:
            newStr = newStr.upper()
        else:
            pass
        # Appliquer la modification
        pModif.set(newStr)
        return pModif.path
    
    
    def execute(self, path):
        '''
        Exécuter la modification
        @param path: Chemin du fichier (modifié après exécution)
        @raise BaseException: Exception levée
        @author: Julien
        '''
        newPath = self.getOverview(path)
        #TODO os.rename(oldPath.get(), newPath.get())
        path.set(newPath.get())



class ReplaceString(Action):
    '''
    Modifier le nom du fichier : remplacer un caractère par un autre
    @author: Julien
    @todo: Case sensitive
    @todo: Toutes les occurrence
    '''
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        Action.__init__(self)
        
        self.range = PathModification.FILENAME
        self.oldStr = ""
        self.newStr = ""
    
    # Informations
    
    @staticmethod
    def getTitle():
        '''
        Obtenir le titre de l'action
        @return: Titre
        @author: Julien
        '''
        return "Remplacement de chaîne"
    
    
    @staticmethod
    def getDescription():
        '''
        Obtenir la description de l'action
        @return: Description
        @author: Julien
        '''
        return "Remplacer une chaîne de caractères par une autre"
    
    # Exécution
    
    def getOverview(self, oldPath):
        '''
        Obtenir l'aperçu de la modification
        @param oldPath: Chemin du fichier
        @return: Chemin du fichier modifié
        @raise: NotImplementedError Méthode non surchargée
        @author: Julien
        '''
        # Partie à modifier
        pModif = PathModification()
        pModif.path = copy.deepcopy(oldPath)
        pModif.range = self.range
        new = pModif.get()
        # Modification
        new = new.replace(self.oldStr, self.newStr)
        # Appliquer la modification
        pModif.set(new)
        return pModif.path
    
    
    def execute(self, path):
        '''
        Exécuter la modification
        @param path: Chemin du fichier (modifié après exécution)
        @raise BaseException: Exception levée
        @author: Julien
        '''
        newPath = self.getOverview(path)
        #TODO os.rename(oldPath.get(), newPath.get())
        path.set(newPath.get())



class Cut(Action):
    '''
    Modifier le nom du fichier : couper un morceau
    @author: Julien
    '''
    
    
    A_PARTIR_DEBUT = True
    A_PARTIR_FIN = False
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        Action.__init__(self)
        
        self.range = PathModification.FILENAME
        self._position = 0
        self._nomber = 0
        self.sens = Cut.A_PARTIR_DEBUT
    
    # Informations
    
    @staticmethod
    def getTitle():
        '''
        Obtenir le titre de l'action
        @return: Titre
        @author: Julien
        '''
        return "Suppression de caractères"
    
    
    @staticmethod
    def getDescription():
        '''
        Obtenir la description de l'action
        @return: Description
        @author: Julien
        '''
        return "Supprimer des caractères du nom de fichier"
    
    # Propriétés
    
    def get_position(self):
        '''
        Obtenir la position du 1er caractère à supprimer
        @return: Position
        @author: Julien
        '''
        return self._position
    
    
    def set_position(self, position):
        '''
        Spécifier la position du 1er caractère à supprimer
        @param oldStr: Position
        @raise ValueError: valeuVr incorrecte
        @author: Julien
        '''
        if position < 0:
            raise ValueError("Valeur incorrecte")
        self._position = int(position)
    
    
    def get_nomber(self):
        '''
        Obtenir le nombre de caractères à couper
        @return: Nombre de caractères
        @author: Julien
        '''
        return self._nomber
    
    
    def set_nomber(self, nomber):
        '''
        Spécifier le nombre de caractères à couper
        @param nombre: Nombre de cractères
        @raise ValueError: valeuVr incorrecte
        @author: Julien
        '''
        if nomber < 0:
            raise ValueError("Valeur incorrecte")
        self._nomber = int(nomber)
    
    
    position = property(fget = get_position, fset = set_position)
    nomber = property(fget = get_nomber, fset = set_nomber)
    
    # Exécution
    
    def getOverview(self, oldPath):
        '''
        Obtenir l'aperçu de la modification
        @param oldPath: Chemin du fichier
        @return: Chemin du fichier modifié
        @author: Julien
        '''
        # Partie à modifier
        pModif = PathModification()
        pModif.path = copy.deepcopy(oldPath)
        pModif.range = self.range
        newStr = pModif.get()
        # Modification
        if self.nomber is not 0:
            if self.sens is Cut.A_PARTIR_DEBUT:
                newStr = newStr[:self.position] + newStr[self.position+self.nomber:]
            elif self.sens is Cut.A_PARTIR_FIN:
                newStr = newStr[:-(self.position+self.nomber)] + newStr[len(newStr)-self.position:]
        # Appliquer la modification
        pModif.set(newStr)
        return pModif.path
    
    
    def execute(self, path):
        '''
        Exécuter la modification
        @param path: Chemin du fichier (modifié après exécution)
        @raise BaseException: Exception levée
        @author: Julien
        '''
        newPath = self.getOverview(path)
        #TODO os.rename(oldPath.get(), newPath.get())
        path.set(newPath.get())



class InsertString(Action):
    '''
    Modifier le nom du fichier : insérer une chaine de caractères
    @author: Julien
    '''
    
    
    A_PARTIR_DEBUT = True
    A_PARTIR_FIN = False
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        Action.__init__(self)
        
        self.range = PathModification.FILENAME
        self.string = ""
        self._position = 0
        self.sens = InsertString.A_PARTIR_DEBUT
    
    # Informations
    
    @staticmethod
    def getTitle():
        '''
        Obtenir le titre de l'action
        @return: Titre
        @author: Julien
        '''
        return "Insertion de chaîne"
    
    
    @staticmethod
    def getDescription():
        '''
        Obtenir la description de l'action
        @return: Description
        @author: Julien
        '''
        return "Insérer une chaîne de caractères dans le nom du fichier"
    
    # Propriétés
    
    def get_position(self):
        '''
        Obtenir la position d'insertion
        @return: Position
        @author: Julien
        '''
        return self._position
    
    
    def set_position(self, position):
        '''
        Spécifier la position d'insertion
        @param position: Position
        @raise ValueError: Valeur incorrecte
        @author: Julien
        '''
        if position < 0:
            raise ValueError("Valeur incorrecte")
        self._position = position
    
    
    position = property(fget = get_position, fset = set_position)
    
    # Exécution
    
    def getOverview(self, oldPath):
        '''
        Obtenir l'aperçu de la modification
        @param oldPath: Chemin du fichier
        @return: Chemin du fichier modifié
        @author: Julien
        '''
        # Partie à modifier
        pModif = PathModification()
        pModif.path = copy.deepcopy(oldPath)
        pModif.range = self.range
        newStr = pModif.get()
        # Modification
        if self.sens is InsertString.A_PARTIR_DEBUT:
            newStr = newStr[:self.position] + self.string + newStr[self.position:]
        elif self.sens is InsertString.A_PARTIR_FIN:
            size = len(newStr)
            newStr = newStr[:max(size-self.position,0)] + self.string + newStr[max(size-self.position,0):]
        # Appliquer la modification
        pModif.set(newStr)
        return pModif.path
    
    
    def execute(self, path):
        '''
        Exécuter la modification
        @param path: Chemin du fichier (modifié après exécution)
        @raise BaseException: Exception levée
        @author: Julien
        '''
        newPath = self.getOverview(path)
        #TODO os.rename(oldPath.get(), newPath.get())
        path.set(newPath.get())



class UpdateTags(Action):
    '''
    Modifier les tags des MP3
    @author: Julien
    '''
    
    
    AUTO = "%auto%"
    FILENAME = "%filename"
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        Action.__init__(self)
        
        self.title = None
        self.subtitle = ""
        self.notation = 1 # non dispo
        self.comment = None
        self.artist = None
        self.albumArtist = None
        self.album = None
        self.year = None
        self.trackNumber = None
        self.genre = None
        self.publisher = None
        self.encodedBy = None
        self.urlAuteur = None
        self.composer = None
        self.conductor = None
        #self.groupDescription = None
        #self.ambiance = None
        self.discNumber = None
        #self.originalKey = None
        self.bpm = None
        self.compilation = None
    
    # Informations
    
    @staticmethod
    def getTitle():
        '''
        Obtenir le titre de l'action
        @return: Titre
        @author: Julien
        '''
        return "Tags MP3"
    
    
    @staticmethod
    def getDescription():
        '''
        Obtenir la description de l'action
        @return: Description
        @author: Julien
        '''
        return "Modifier les tags musicaux d'un fichier MP3"
    
    # Exécution
    
    def getOverview(self, oldPath):
        '''
        Obtenir l'aperçu de la modification
        @param oldPath: Chemin du fichier
        @return: Chemin du fichier modifié
        @author: Julien
        '''
        return oldPath
    
    
    def execute(self, path):
        '''
        Exécuter la modification
        @param path: Chemin du fichier (modifié après exécution)
        @raise BaseException: Exception levée
        @author: Julien
        '''
        pass



if __name__ == "__main__":
    pass