#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Tests du module eyed3
@author: Julien
'''



import eyed3
import eyed3.id3
import mutagen.id3
import mutagen.easyid3
import os
import shutil
import unittest



current_dir = os.path.dirname(__file__)
dir_src = os.path.join(current_dir, "src")
dir_tgt = os.path.join(current_dir, "tgt")



class TestRead(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        '''Copie des fichiers source'''
        if os.path.exists(dir_tgt):
            shutil.rmtree(dir_tgt)
        shutil.copytree(dir_src, dir_tgt)
    
    
    @classmethod
    def tearDownClass(cls):
        '''Suppression des fichiers source'''
        shutil.rmtree(dir_tgt)
    
    
    def test_full_eyed3(self):
        audio_path = os.path.join(dir_tgt, "full.mp3")
        audio_file = eyed3.load(audio_path)
        
        self.assertEqual(audio_file.tag.title, "title") # titre
        # sous-titre
        # notation
        # commentaire
        self.assertEqual(audio_file.tag.artist, "artist1/artist2") # artiste ayant participé
        # artiste de l'album
        self.assertEqual(audio_file.tag.album, "album") # album
        # année
        self.assertEqual(audio_file.tag.track_num[0], 11) # n°
        self.assertEqual(audio_file.tag.genre.name, "genre") # genre
        self.assertEqual(audio_file.tag.publisher, "publisher") # éditeur
        # encodé par
        self.assertEqual(audio_file.tag.artist_url, "urlAuteur") # URL de l'auteur
        # compositeur
        # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(audio_file.tag.disc_num[0], 1) # partie du coffret
        # clé d'origine
        self.assertEqual(audio_file.tag.bpm, 111) # battements par minute
        # partie d'une compilation
        
        #print audio_file.info.time_secs # ?
    
    
    def test_full_mutagen(self):
        audio_path = os.path.join(dir_tgt, "full.mp3")
        audio_file = mutagen.easyid3.EasyID3(audio_path)
        
        self.assertEqual(audio_file["title"][0], "title") # titre
        self.assertEqual(audio_file["version"][0], "subtitle") # sous-titre
        # notation
        # commentaire
        self.assertEqual(audio_file["artist"][0], "artist1/artist2") # artiste ayant participé
        self.assertEqual(audio_file["performer"][0], "albumArtist") # artiste de l'album
        self.assertEqual(audio_file["album"][0], "album") # album
        self.assertEqual(audio_file["date"][0], "1111") # année
        self.assertEqual(audio_file["tracknumber"][0], "11") # n°
        self.assertEqual(audio_file["genre"][0], "genre") # genre
        self.assertEqual(audio_file["organization"][0], "publisher") # éditeur
        self.assertEqual(audio_file["encodedby"][0], "encodedBy") # encodé par
        self.assertEqual(audio_file["website"][0], "urlAuteur") # URL de l'auteur
        self.assertEqual(audio_file["composer"][0], "composer1/composer2") # compositeur
        self.assertEqual(audio_file["conductor"][0], "conductor") # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(audio_file["discnumber"][0], "1") # partie du coffret
        # clé d'origine
        self.assertEqual(audio_file["bpm"][0], "111") # battements par minute
        self.assertEqual(audio_file["compilation"][0], "0") # partie d'une compilation
        
        #print int(audio_file["arranger"][0])
        #print mutagen.easyid3.EasyID3.valid_keys.keys()
        #print mutagen.File(audio_path, easy=True)
    
    
    def test_empty_eyed3(self):
        audio_path = os.path.join(dir_tgt, "none.mp3")
        audio_file = eyed3.load(audio_path)
        
        self.assertEqual(audio_file.tag.title, None) # titre
        # sous-titre
        # notation
        # commentaire
        self.assertEqual(audio_file.tag.artist, None) # artiste ayant participé
        # artiste de l'album
        self.assertEqual(audio_file.tag.album, None) # album
        # année
        self.assertEqual(audio_file.tag.track_num[0], None) # n°
        self.assertEqual(audio_file.tag.genre, None) # genre
        self.assertEqual(audio_file.tag.publisher, None) # éditeur
        # encodé par
        self.assertEqual(audio_file.tag.artist_url, None) # URL de l'auteur
        # compositeur
        # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(audio_file.tag.disc_num[0], None) # partie du coffret
        # clé d'origine
        self.assertEqual(audio_file.tag.bpm, None) # battements par minute
        # partie d'une compilation
    
    
    def test_none_mutagen(self):
        audio_path = os.path.join(dir_tgt, "none.mp3")
        audio_file = mutagen.easyid3.EasyID3(audio_path)
        
        try:
            self.assertEqual(audio_file["title"][0], None) # titre
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio_file["version"][0], "subtitle") # sous-titre
            self.assert_(False)
        except KeyError: pass
        # notation
        # commentaire
        try:
            self.assertEqual(audio_file["artist"][0], "artist1/artist2") # artiste ayant participé
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio_file["performer"][0], "albumArtist") # artiste de l'album
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio_file["album"][0], "album") # album
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio_file["date"][0], "1111") # année
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio_file["tracknumber"][0], "11") # n°
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio_file["genre"][0], "genre") # genre
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio_file["organization"][0], "publisher") # éditeur
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio_file["encodedby"][0], "encodedBy") # encodé par
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio_file["website"][0], "urlAuteur") # URL de l'auteur
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio_file["composer"][0], "composer1/composer2") # compositeur
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio_file["conductor"][0], "conductor") # chef d'orchestre
            self.assert_(False)
        except KeyError: pass
        # description du groupe
        # ambiance
        try:
            self.assertEqual(int(audio_file["discnumber"][0]), 1) # partie du coffret
            self.assert_(False)
        except KeyError: pass
        # clé d'origine
        try:
            self.assertEqual(int(audio_file["bpm"][0]), 111) # battements par minute
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(int(audio_file["compilation"][0]), 0) # partie d'une compilation
            self.assert_(False)
        except KeyError: pass



class TestWrite(unittest.TestCase):
    
    def setUp(self):
        '''Copie des fichiers source'''
        if os.path.exists(dir_tgt):
            shutil.rmtree(dir_tgt)
        shutil.copytree(dir_src, dir_tgt)
    
    
    def tearDown(self):
        '''Suppression des fichiers source'''
        shutil.rmtree(dir_tgt)
    
    
    def test_full_eyed3(self):
        audio_path = os.path.join(dir_tgt, "full.mp3")
        audio_file = eyed3.load(audio_path)
        
        audio_file.tag.title = unicode("new_title") # titre
        # sous-titre
        # notation
        # commentaire
        audio_file.tag.artist = unicode("new_artist") # artiste ayant participé
        # artiste de l'album
        audio_file.tag.album = unicode("new_album") # album
        # année
        audio_file.tag.track_num = 22 # n°
        audio_file.tag.genre = eyed3.id3.Genre(u"new_genre") # genre
        audio_file.tag.publisher = unicode("new_publisher") # éditeur
        # encodé par
        audio_file.tag.artist_url = unicode("new_urlAuteur") # URL de l'auteur
        # compositeur
        # chef d'orchestre
        # description du groupe
        # ambiance
        audio_file.tag.disc_num = 2 # partie du coffret
        # clé d'origine
        audio_file.tag.bpm = 222 # battements par minute
        # partie d'une compilation
        
        audio_file.tag.save()
        audio_file = eyed3.load(audio_path)
        
        self.assertEqual(audio_file.tag.title, "new_title") # titre
        # sous-titre
        # notation
        # commentaire
        self.assertEqual(audio_file.tag.artist, "new_artist") # artiste ayant participé
        # artiste de l'album
        self.assertEqual(audio_file.tag.album, "new_album") # album
        # année
        self.assertEqual(audio_file.tag.track_num[0], 22) # n°
        self.assertEqual(audio_file.tag.genre.name, "new_genre") # genre
        self.assertEqual(audio_file.tag.publisher, "new_publisher") # éditeur
        # encodé par
        self.assertEqual(audio_file.tag.artist_url, "new_urlAuteur") # URL de l'auteur
        # compositeur
        # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(audio_file.tag.disc_num[0], 2) # partie du coffret
        # clé d'origine
        self.assertEqual(audio_file.tag.bpm, 222) # battements par minute
        # partie d'une compilation
    
    
    def test_full_mutagen(self):
        audio_path = os.path.join(dir_tgt, "full.mp3")
        audio_file = mutagen.easyid3.EasyID3(audio_path)
        
        audio_file["title"] = "new_title" # titre
        audio_file["version"] = "new_subtitle" # sous-titre
        # notation
        # commentaire
        audio_file["artist"] = "new_artist" # artiste ayant participé
        audio_file["performer"] = "new_albumArtist" # artiste de l'album
        audio_file["album"] = "new_album" # album
        audio_file["date"] = "2222" # année
        audio_file["tracknumber"] = "22" # n°
        audio_file["genre"] = "new_genre" # genre
        audio_file["organization"] = "new_publisher" # éditeur
        audio_file["encodedby"] = "new_encodedBy" # encodé par
        audio_file["website"] = "new_urlAuteur" # URL de l'auteur
        audio_file["composer"] = "new_composer" # compositeur
        audio_file["conductor"] = "new_conductor" # chef d'orchestre
        # description du groupe
        # ambiance
        audio_file["discnumber"] = "2" # partie du coffret
        # clé d'origine
        audio_file["bpm"] = "222" # battements par minute
        audio_file["compilation"] = "1" # partie d'une compilation
        
        audio_file.save()
        audio_file = mutagen.easyid3.EasyID3(audio_path)
        
        self.assertEqual(audio_file["title"][0], "new_title") # titre
        self.assertEqual(audio_file["version"][0], "new_subtitle") # sous-titre
        # notation
        # commentaire
        self.assertEqual(audio_file["artist"][0], "new_artist") # artiste ayant participé
        self.assertEqual(audio_file["performer"][0], "new_albumArtist") # artiste de l'album
        self.assertEqual(audio_file["album"][0], "new_album") # album
        self.assertEqual(audio_file["date"][0], "2222") # année
        self.assertEqual(audio_file["tracknumber"][0], "22") # n°
        self.assertEqual(audio_file["genre"][0], "new_genre") # genre
        self.assertEqual(audio_file["organization"][0], "new_publisher") # éditeur
        self.assertEqual(audio_file["encodedby"][0], "new_encodedBy") # encodé par
        self.assertEqual(audio_file["website"][0], "new_urlAuteur") # URL de l'auteur
        self.assertEqual(audio_file["composer"][0], "new_composer") # compositeur
        self.assertEqual(audio_file["conductor"][0], "new_conductor") # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(audio_file["discnumber"][0], "2") # partie du coffret
        # clé d'origine
        self.assertEqual(audio_file["bpm"][0], "222") # battements par minute
        self.assertEqual(audio_file["compilation"][0], "1") # partie d'une compilation



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