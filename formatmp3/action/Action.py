#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Action sur les fichiers
@author: Julien
'''



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
        self._path = ""
    
    
    @staticmethod
    def getTitle():
        '''
        Obtenir le titre de l'action
        @return: Titre
        @raise: NotImplementedError Méthode non surchargée
        @author: Julien
        '''
        raise NotImplementedError
    
    
    def get_path(self):
        '''
        Obtenir le chemin du fichier
        @return: Chemin du fichier
        @author: Julien
        '''
        return self._path
    
    
    def set_path(self, path):
        '''
        Spécifier le chemin du fichier
        @param path: Chemin du fichier
        @author: Julien
        '''
        self._path = path
    
    
    def get_filename(self):
        '''
        Obtenir le nom du fichier (sans extension)
        @return: Nom du fichier
        @author: Julien
        '''
        basename = os.path.basename(self._path)
        return os.path.splitext(basename)[0]
    
    
    def set_filename(self, filename):
        '''
        Spécifier le nom du fichier (sans extension)
        @param path: Nom du fichier
        @author: Julien
        '''
        direname = os.path.dirname(self._path)
        basename = os.path.basename(self._path)
        extension = os.path.splitext(basename)[1]
        self._path = os.path.join(direname, filename) + extension
    
    
    # Propriétés
    path = property(fget = get_path, fset = set_path)
    filename = property(fget = get_filename, fset = set_filename)
    
    
    def rename(self, newFilename):
        '''
        Renommer le fichier
        Les changements ne sont pas appliqués en cas d'échec
        @param newFilename: Nouveau nom de fichier
        @raise BaseException: Exception levée
        @author: Julien
        '''
        oldPath = self.path
        try:
            self.filename = newFilename
            newPath = self.path
            pass #TODO os.rename(oldPath, newPath)
        except BaseException as err:
            self.path = oldPath
            raise err
    
    
    def execute(self):
        '''
        Exécuter la modification
        @raise: NotImplementedError Méthode non surchargée
        @author: Julien
        '''
        raise NotImplementedError



class CaseChange(Action):
    '''
    Modifier le nom du fichier :
    1ère lettre en majuscule puis minuscules
    @author: Julien
    '''
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        Action.__init__(self)
    
    
    @staticmethod
    def getTitle():
        '''
        Obtenir le titre de l'action
        @return: Titre
        @author: Julien
        '''
        return "Changement de case"
    
    
    def execute(self):
        '''
        Exécuter la modification
        @raise BaseException: Exception levée
        @author: Julien
        '''
        # Nouveau nom de fichier
        newFilename = self.filename
        newFilename = newFilename.lower()
        listNewFilename = list(newFilename)
        listNewFilename[0] = listNewFilename[0].upper()
        newFilename = ''.join(listNewFilename)
        # Renommer le fichier
        self.rename(newFilename)



class ReplaceString(Action):
    '''
    Modifier le nom du fichier :
    Remplacer un caractère par un autre
    @author: Julien
    '''
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        Action.__init__(self)
        self._oldStr = ""
        self._newStr = ""
    
    
    @staticmethod
    def getTitle():
        '''
        Obtenir le titre de l'action
        @return: Titre
        @author: Julien
        '''
        return "Remplacement de chaîne"
    
    
    def get_oldStr(self):
        '''
        Obtenir la chaine à remplacer
        @return: Chaine à remplacer
        @author: Julien
        '''
        return self._oldStr
    
    
    def set_oldStr(self, oldStr):
        '''
        Spécifier la chaine à remplacer
        @param oldStr: Chaine à remplacer
        @author: Julien
        '''
        self._oldStr = oldStr
    
    
    def get_newStr(self):
        '''
        Obtenir la nouvelle chaine
        @return: Nouvelle chaine
        @author: Julien
        '''
        return self._newStr
    
    
    def set_newStr(self, newStr):
        '''
        Spécifier la nouvelle chaine
        @param newStr: Nouvelle chaine
        @author: Julien
        '''
        self._newStr = newStr
    
    
    # Propriétés
    oldStr = property(fget = get_oldStr, fset = set_oldStr)
    newStr = property(fget = get_newStr, fset = set_newStr)
    
    
    def execute(self):
        '''
        Exécuter la modification
        @raise BaseException: Exception levée
        @author: Julien
        '''
        # Nouveau nom de fichier
        newFilename = self.filename
        newFilename = newFilename.replace(self.oldStr, self.newStr)
        # Renommer le fichier
        self.rename(newFilename)



class Cut(Action):
    '''
    Couper le nom du fichier
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
        self._nombre = 0
        self._position = 0
        self._sens = Cut.A_PARTIR_DEBUT
    
    
    @staticmethod
    def getTitle():
        '''
        Obtenir le titre de l'action
        @return: Titre
        @author: Julien
        '''
        return "Couper le nom de fichier"
    
    
    def get_nombre(self):
        '''
        Obtenir le nombre de caractères à couper
        @return: Nombre de caractères
        @author: Julien
        '''
        return self._nombre
    
    
    def set_nombre(self, nombre):
        '''
        Spécifier le nombre de caractères à couper
        @param nombre: Nombre de cractères
        @raise ValueError: valeuVr incorrecte
        @author: Julien
        '''
        if nombre < 0:
            raise ValueError("Valeur incorrecte")
        self._nombre = int(nombre)
    
    
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
    
    
    def get_sens(self):
        '''
        Obtenir le sens de parcours
        @return: Sens
        @author: Julien
        '''
        return self._sens
    
    
    def set_sens(self, sens):
        '''
        Spécifier le sens de parcours
        @param sens: Sens (A_PARTIR_DEBUT ou A_PARTIR_FIN)
        @raise ValueError: Valeur incorrecte
        @author: Julien
        '''
        if sens not in [Cut.A_PARTIR_DEBUT, Cut.A_PARTIR_FIN]:
            raise ValueError("Valeur incorrecte")
        self._sens = sens
    
    
    # Propriétés
    nombre = property(fget = get_nombre, fset = set_nombre)
    position = property(fget = get_position, fset = set_position)
    sens = property(fget = get_sens, fset = set_sens)
    
    
    def execute(self):
        '''
        Exécuter la modification
        @raise BaseException: Exception levée
        @author: Julien
        '''
        # Nouveau nom de fichier
        newFilename = self.filename
        if self.sens is Cut.A_PARTIR_DEBUT:
            newFilename = newFilename[:self.position] + newFilename[self.position+self.nombre:]
        elif self.sens is Cut.A_PARTIR_FIN:
            newFilename = newFilename[:self.position-self.nombre] + newFilename[self.position:]
        # Renommer le fichier
        self.rename(newFilename)



class InsertString(Action):
    '''
    Insérer une chaine dans le nom du fichier
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
        self.string = ""
        self._position = 0
        self._sens = InsertString.A_PARTIR_DEBUT
    
    
    @staticmethod
    def getTitle():
        '''
        Obtenir le titre de l'action
        @return: Titre
        @author: Julien
        '''
        return "Insertion d'un chaîne"
    
    
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
    
    
    def get_sens(self):
        '''
        Obtenir le sens de parcours
        @return: Sens
        @author: Julien
        '''
        return self._sens
    
    
    def set_sens(self, sens):
        '''
        Spécifier le sens de parcours
        @param sens: Sens (A_PARTIR_DEBUT ou A_PARTIR_FIN)
        @raise ValueError: Valeur incorrecte
        @author: Julien
        '''
        if sens not in [InsertString.A_PARTIR_DEBUT, InsertString.A_PARTIR_FIN]:
            raise ValueError("Valeur incorrecte")
        self._sens = sens
    
    
    # Propriétés
    position = property(fget = get_position, fset = set_position)
    sens = property(fget = get_sens, fset = set_sens)
    
    
    def execute(self):
        '''
        Exécuter la modification
        @raise BaseException: Exception levée
        @author: Julien
        '''
        # Nouveau nom de fichier
        newFilename = self.filename
        if self.sens is InsertString.A_PARTIR_DEBUT:
            newFilename = newFilename[:self.position] + self.string + newFilename[self.position:]
        elif self.sens is InsertString.A_PARTIR_FIN:
            size = len(newFilename)
            newFilename = newFilename[:max(size-self.position,0)] + self.string + newFilename[max(size-self.position,0):]
        # Renommer le fichier
        self.rename(newFilename)



class UpdateTags(Action):
    '''
    Modifier les tags des MP3
    @author: Julien
    '''
    
    
    AUTO = "%auto%"
    
    
    def __init__(self):
        '''
        Constructeur
        @author: Julien
        '''
        Action.__init__(self)
        self.artiste = None
        self.album = None
        self.genre = None
        self.annee = None
    
    
    @staticmethod
    def getTitle():
        '''
        Obtenir le titre de l'action
        @return: Titre
        @author: Julien
        '''
        return "Modification des tags"
    
    
    def execute(self):
        '''
        Exécuter la modification
        @raise BaseException: Exception levée
        @author: Julien
        '''
        pass # TODO



if __name__ == "__main__":
    path = "0123456789"
    print path
    
    nombre = 2
    position = 9
    sens = True
    
    size = len(path)
    if sens:
        print path[:position] + "_" + path[position+nombre:]
    else:
        print path[:position-nombre] + "_" + path[position:]