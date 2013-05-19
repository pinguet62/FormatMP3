#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Action sur les fichiers
@author: Julien
'''



from formatmp3.actions.Path import *
import copy
import eyed3.id3
import mutagen.easyid3
import mutagen.id3
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
    
    _EYED3_RATING = {1:1, 2:64, 3:128, 4:196, 5:255}
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        Action.__init__(self)
        
        self.title = ""
        self.subtitle = ""
        self.rating = None # 0 # TODO: non dispo
        self.comment = ""
        self.artist = "" # TODO: liste
        self.albumArtist = ""
        self.album = ""
        self.year = ""
        self.trackNumber = ""
        self.genre = ""
        self.publisher = ""
        self.encodedBy = ""
        self.urlAuteur = ""
        self.composers = "" # TODO: liste
        self.conductors = ""
        self.groupDescription = None # "" # TODO: non dispo
        self.ambiance = None # "" # TODO: non dispo
        self.discNumber = ""
        self.originalKey = None # "" # TODO: non dispo
        self.bpm = ""
        self.compilation = False
    
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
        # notation
        if self.rating is not None:
            audio = eyed3.load(path.get())
            value = UpdateTags._EYED3_RATING[self.rating]
            audio.tag.frame_set["POPM"] = eyed3.id3.frames.PopularityFrame(id="POPM", rating=value)
            audio.tag.save()
        
        audio = mutagen.easyid3.EasyID3(path.get())
        
        # titre
        if self.title is not None:
            if self.title == UpdateTags.FILENAME:
                newTitle = path.filename
            else:
                newTitle = self.title
            audio["title"] = newTitle
        # sous-titre
        if self.subtitle is not None:
            audio["version"] = self.subtitle
        # notation
        # TODO: réorganiser le code, ou voir avec mutagen
        # commentaire
        # artiste ayant participé
        if self.artist is not None:
            audio["artist"] = self.artist
        # artiste de l'album
        if self.albumArtist is not None:
            audio["performer"] = self.albumArtist
        # album
        if self.album is not None:
            audio["album"] = self.album
        # année
        if self.year is not None:
            audio["date"] = str(self.year)
        # n°
        if self.trackNumber is not None:
            audio["tracknumber"] = str(self.trackNumber)
        # genre
        if self.genre is not None:
            audio["genre"] = self.genre
        # éditeur
        if self.publisher is not None:
            audio["organization"] = self.publisher
        # encodé par
        if self.encodedBy is not None:
            audio["encodedby"] = self.encodedBy
        # URL de l'auteur
        if self.urlAuteur is not None:
            audio["website"] = self.urlAuteur
        # compositeur
        if self.composers is not None:
            audio["composer"] = self.composers
        # chef d'orchestre
        if self.conductors is not None:
            audio["conductor"] = self.conductors
        # description du groupe
        # ambiance
        # partie du coffret
        if self.discNumber is not None:
            audio["discnumber"] = str(self.discNumber)
        # clé d'origine
        # battements par minute
        if self.bpm is not None:
            audio["bpm"] = self.bpm
        # partie d'une compilation
        if self.compilation is not None:
            if self.compilation:
                audio["compilation"] = "1"
            else:
                audio["compilation"] = "0"
        
        audio.tag.save()



if __name__ == "__main__":
    pass