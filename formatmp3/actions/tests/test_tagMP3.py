#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Tests du module eyed3
@author: Julien
'''



import eyed3
import mutagen.id3
import mutagen.easyid3
import os
import shutil
import unittest



current_dir = os.path.dirname(__file__)
dir_src = os.path.join(current_dir, "src")
dir_tgt = os.path.join(current_dir, "tgt")



class TestEyed3(unittest.TestCase):
    '''
    Tests de modification des tags
    @author: Julien
    '''
    
    
    @classmethod
    def setUpClass(cls):
        '''
        Initialisation des tests
        @param cls: Classe
        @author: Julien
        '''
        if os.path.exists(dir_tgt):
            shutil.rmtree(dir_tgt)
        shutil.copytree(dir_src, dir_tgt)
    
    
    @classmethod
    def tearDownClass(cls):
        '''
        Terminaison des tests
        @param cls: Classe
        @author: Julien
        '''
        shutil.rmtree(dir_tgt)
    
    
    def test_lecture(self):
        audio1_path = os.path.join(dir_src, "audio1.mp3")
        audio1_file = eyed3.load(audio1_path)
        self.assertEqual(audio1_file.tag.title, "titre1") # titre
        # sous-titre
        # notation
        # commentaire
        self.assertEqual(audio1_file.tag.artist, "artiste1") # artiste ayant participé
        # artiste de l'album
        self.assertEqual(audio1_file.tag.album, "album1") # album
        # année
        self.assertEqual(audio1_file.tag.track_num[0], 11) # n°
        self.assertEqual(audio1_file.tag.genre.name, "genre1") # genre
        self.assertEqual(audio1_file.tag.publisher, "editeur1") # éditeur
        # encodé par
        self.assertEqual(audio1_file.tag.artist_url, "urlAuteur1") # URL de l'auteur
        # compositeur
        # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(audio1_file.tag.disc_num[0], 111) # partie du coffret
        # clé d'origine
        self.assertEqual(audio1_file.tag.bpm, 11111) # battements par minute
        # partie d'une compilation
        
        #print audio1_file.info.time_secs # ?



class TestMutagen(unittest.TestCase):
    '''
    Tests de modification des tags
    @author: Julien
    '''
    
    
    @classmethod
    def setUpClass(cls):
        '''
        Initialisation des tests
        @param cls: Classe
        @author: Julien
        '''
        if os.path.exists(dir_tgt):
            shutil.rmtree(dir_tgt)
        shutil.copytree(dir_src, dir_tgt)
    
    
    @classmethod
    def tearDownClass(cls):
        '''
        Terminaison des tests
        @param cls: Classe
        @author: Julien
        '''
        shutil.rmtree(dir_tgt)
    
    
    def test_lecture(self):
        audio1_path = os.path.join(dir_src, "audio1.mp3")
        audio1_file = mutagen.easyid3.EasyID3(audio1_path)
        self.assertEqual(audio1_file["title"][0], "titre1") # titre
        self.assertEqual(audio1_file["version"][0], "sousTitre1") # sous-titre
        # notation
        # commentaire
        self.assertEqual(audio1_file["artist"][0], "artiste1") # artiste ayant participé
        self.assertEqual(audio1_file["performer"][0], "artisteAlbum1") # artiste de l'album
        self.assertEqual(audio1_file["album"][0], "album1") # album
        self.assertEqual(int(audio1_file["date"][0]), 1111) # année
        self.assertEqual(int(audio1_file["tracknumber"][0]), 11) # n°
        self.assertEqual(audio1_file["genre"][0], "genre1") # genre
        self.assertEqual(audio1_file["organization"][0], "editeur1") # éditeur
        self.assertEqual(audio1_file["encodedby"][0], "encodePar1") # encodé par
        self.assertEqual(audio1_file["website"][0], "urlAuteur1") # URL de l'auteur
        self.assertEqual(audio1_file["composer"][0], "compositeur1") # compositeur
        self.assertEqual(audio1_file["conductor"][0], "chefOrchestre1") # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(int(audio1_file["discnumber"][0]), 111) # partie du coffret
        # clé d'origine
        self.assertEqual(int(audio1_file["bpm"][0]), 11111) # battements par minute
        self.assertEqual(int(audio1_file["compilation"][0]), 0) # partie d'une compilation
        
        #print int(audio1_file["arranger"][0])
        #print mutagen.easyid3.EasyID3.valid_keys.keys()
        print mutagen.File(audio1_path, easy=True)



if __name__ == "__main__":
    unittest.main()

# titre
# sous-titre
# notation
# commentaire
# artiste ayant participé
# artiste de l'album
# album
# année
# n°
# genre
# éditeur
# encodé par
# URL de l'auteur
# compositeur
# chef d'orchestre
# description du groupe
# ambiance
# partie du coffret
# clé d'origine
# battements par minute
# partie d'une compilation