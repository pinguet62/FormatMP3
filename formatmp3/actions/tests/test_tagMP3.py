#!/usr/bin/python
# -*- coding: utf-8 -*-
from formatmp3.actions.Action import Action



'''
Tests du module eyed3
@author: Julien
'''



import eyed3
import eyed3.id3
import mutagen.easyid3
import mutagen.id3
import os
import shutil
import unittest



current_dir = os.path.dirname(__file__)
# Répertoires
dir_src = os.path.join(current_dir, "src")
dir_tgt = os.path.join(current_dir, "tgt")
# Fichiers
fullMP3 = os.path.join(dir_tgt, "full.mp3")
noneMP3 = os.path.join(dir_tgt, "none.mp3")



class TestId3(unittest.TestCase):
    
    def setUp(self):
        '''Copie des fichiers source'''
        if os.path.exists(dir_tgt):
            shutil.rmtree(dir_tgt)
            self.assertFalse(os.path.exists(dir_tgt))
        shutil.copytree(dir_src, dir_tgt)
        self.assertTrue(os.path.exists(dir_tgt))
    
    
    def tearDown(self):
        '''Suppression des fichiers source'''
        shutil.rmtree(dir_tgt)
        self.assertFalse(os.path.exists(dir_tgt))
    
    
    def test_read_full_eyed3(self):
        audio = eyed3.load(fullMP3)
        
        self.assertEqual(audio.tag.title, "title") # titre
        # sous-titre
        self.assertEqual(audio.tag.frame_set["POPM"][0].rating, 1) # notation
        # commentaire
        self.assertEqual(audio.tag.artist, "artist1/artist2") # artiste ayant participé
        # artiste de l'album
        self.assertEqual(audio.tag.album, "album") # album
        # année
        self.assertEqual(audio.tag.track_num[0], 11) # n°
        self.assertEqual(audio.tag.genre.name, "genre") # genre
        self.assertEqual(audio.tag.publisher, "publisher") # éditeur
        # encodé par
        self.assertEqual(audio.tag.artist_url, "urlAuteur") # URL de l'auteur
        # compositeur
        # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(audio.tag.disc_num[0], 1) # partie du coffret
        # clé d'origine
        self.assertEqual(audio.tag.bpm, 111) # battements par minute
        # partie d'une compilation
    
    
    def test_read_full_mutagen(self):
        audio = mutagen.easyid3.EasyID3(fullMP3)
        
        self.assertEqual(audio["title"][0], "title") # titre
        self.assertEqual(audio["version"][0], "subtitle") # sous-titre
        # notation
        # commentaire
        self.assertEqual(audio["artist"][0], "artist1/artist2") # artiste ayant participé
        self.assertEqual(audio["performer"][0], "albumArtist") # artiste de l'album
        self.assertEqual(audio["album"][0], "album") # album
        self.assertEqual(audio["date"][0], "1111") # année
        self.assertEqual(audio["tracknumber"][0], "11") # n°
        self.assertEqual(audio["genre"][0], "genre") # genre
        self.assertEqual(audio["organization"][0], "publisher") # éditeur
        self.assertEqual(audio["encodedby"][0], "encodedBy") # encodé par
        self.assertEqual(audio["website"][0], "urlAuteur") # URL de l'auteur
        self.assertEqual(audio["composer"][0], "composer1/composer2") # compositeur
        self.assertEqual(audio["conductor"][0], "conductor") # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(audio["discnumber"][0], "1") # partie du coffret
        # clé d'origine
        self.assertEqual(audio["bpm"][0], "111") # battements par minute
        self.assertEqual(audio["compilation"][0], "0") # partie d'une compilation
    
    
    def test_read_none_eyed3(self):
        audio = eyed3.load(noneMP3)
        
        self.assertEqual(audio.tag.title, None) # titre
        # sous-titre
        self.assertFalse("POPM" in audio.tag.frame_set) # notation
        # commentaire
        self.assertEqual(audio.tag.artist, None) # artiste ayant participé
        # artiste de l'album
        self.assertEqual(audio.tag.album, None) # album
        # année
        self.assertEqual(audio.tag.track_num[0], None) # n°
        self.assertEqual(audio.tag.genre, None) # genre
        self.assertEqual(audio.tag.publisher, None) # éditeur
        # encodé par
        self.assertEqual(audio.tag.artist_url, None) # URL de l'auteur
        # compositeur
        # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(audio.tag.disc_num[0], None) # partie du coffret
        # clé d'origine
        self.assertEqual(audio.tag.bpm, None) # battements par minute
        # partie d'une compilation
    
    
    def test_read_none_mutagen(self):
        audio = mutagen.easyid3.EasyID3(noneMP3)
        
        try:
            self.assertEqual(audio["title"][0], None) # titre
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio["version"][0], "subtitle") # sous-titre
            self.assert_(False)
        except KeyError: pass
        # notation
        # commentaire
        try:
            self.assertEqual(audio["artist"][0], "artist1/artist2") # artiste ayant participé
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio["performer"][0], "albumArtist") # artiste de l'album
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio["album"][0], "album") # album
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio["date"][0], "1111") # année
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio["tracknumber"][0], "11") # n°
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio["genre"][0], "genre") # genre
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio["organization"][0], "publisher") # éditeur
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio["encodedby"][0], "encodedBy") # encodé par
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio["website"][0], "urlAuteur") # URL de l'auteur
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio["composer"][0], "composer1/composer2") # compositeur
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(audio["conductor"][0], "conductor") # chef d'orchestre
            self.assert_(False)
        except KeyError: pass
        # description du groupe
        # ambiance
        try:
            self.assertEqual(int(audio["discnumber"][0]), 1) # partie du coffret
            self.assert_(False)
        except KeyError: pass
        # clé d'origine
        try:
            self.assertEqual(int(audio["bpm"][0]), 111) # battements par minute
            self.assert_(False)
        except KeyError: pass
        try:
            self.assertEqual(int(audio["compilation"][0]), 0) # partie d'une compilation
            self.assert_(False)
        except KeyError: pass
    
    
    def test_write_full_eyed3(self):
        self.test_read_full_eyed3()
        
        audio = eyed3.load(fullMP3)
        
        audio.tag.title = unicode("new_title") # titre
        # sous-titre
        audio.tag.frame_set["POPM"][0].rating = 64 # notation
        # commentaire
        audio.tag.artist = unicode("new_artist") # artiste ayant participé
        # artiste de l'album
        audio.tag.album = unicode("new_album") # album
        # année
        audio.tag.track_num = 22 # n°
        audio.tag.genre = eyed3.id3.Genre(u"new_genre") # genre
        audio.tag.publisher = unicode("new_publisher") # éditeur
        # encodé par
        audio.tag.artist_url = unicode("new_urlAuteur") # URL de l'auteur
        # compositeur
        # chef d'orchestre
        # description du groupe
        # ambiance
        audio.tag.disc_num = 2 # partie du coffret
        # clé d'origine
        audio.tag.bpm = 222 # battements par minute
        # partie d'une compilation
        
        audio.tag.save()
        
        audio = eyed3.load(fullMP3)
        
        self.assertEqual(audio.tag.title, "new_title") # titre
        # sous-titre
        self.assertEqual(audio.tag.frame_set["POPM"][0].rating, 64) # notation
        # commentaire
        self.assertEqual(audio.tag.artist, "new_artist") # artiste ayant participé
        # artiste de l'album
        self.assertEqual(audio.tag.album, "new_album") # album
        # année
        self.assertEqual(audio.tag.track_num[0], 22) # n°
        self.assertEqual(audio.tag.genre.name, "new_genre") # genre
        self.assertEqual(audio.tag.publisher, "new_publisher") # éditeur
        # encodé par
        self.assertEqual(audio.tag.artist_url, "new_urlAuteur") # URL de l'auteur
        # compositeur
        # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(audio.tag.disc_num[0], 2) # partie du coffret
        # clé d'origine
        self.assertEqual(audio.tag.bpm, 222) # battements par minute
        # partie d'une compilation
    
    
    def test_write_full_mutagen(self):
        self.test_read_full_mutagen()
        
        audio = mutagen.easyid3.EasyID3(fullMP3)
        
        audio["title"] = "new_title" # titre
        audio["version"] = "new_subtitle" # sous-titre
        # notation
        # commentaire
        audio["artist"] = "new_artist" # artiste ayant participé
        audio["performer"] = "new_albumArtist" # artiste de l'album
        audio["album"] = "new_album" # album
        audio["date"] = "2222" # année
        audio["tracknumber"] = "22" # n°
        audio["genre"] = "new_genre" # genre
        audio["organization"] = "new_publisher" # éditeur
        audio["encodedby"] = "new_encodedBy" # encodé par
        audio["website"] = "new_urlAuteur" # URL de l'auteur
        audio["composer"] = "new_composer" # compositeur
        audio["conductor"] = "new_conductor" # chef d'orchestre
        # description du groupe
        # ambiance
        audio["discnumber"] = "2" # partie du coffret
        # clé d'origine
        audio["bpm"] = "222" # battements par minute
        audio["compilation"] = "1" # partie d'une compilation
        
        audio.save()
        
        audio = mutagen.easyid3.EasyID3(fullMP3)
        
        self.assertEqual(audio["title"][0], "new_title") # titre
        self.assertEqual(audio["version"][0], "new_subtitle") # sous-titre
        # notation
        # commentaire
        self.assertEqual(audio["artist"][0], "new_artist") # artiste ayant participé
        self.assertEqual(audio["performer"][0], "new_albumArtist") # artiste de l'album
        self.assertEqual(audio["album"][0], "new_album") # album
        self.assertEqual(audio["date"][0], "2222") # année
        self.assertEqual(audio["tracknumber"][0], "22") # n°
        self.assertEqual(audio["genre"][0], "new_genre") # genre
        self.assertEqual(audio["organization"][0], "new_publisher") # éditeur
        self.assertEqual(audio["encodedby"][0], "new_encodedBy") # encodé par
        self.assertEqual(audio["website"][0], "new_urlAuteur") # URL de l'auteur
        self.assertEqual(audio["composer"][0], "new_composer") # compositeur
        self.assertEqual(audio["conductor"][0], "new_conductor") # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(audio["discnumber"][0], "2") # partie du coffret
        # clé d'origine
        self.assertEqual(audio["bpm"][0], "222") # battements par minute
        self.assertEqual(audio["compilation"][0], "1") # partie d'une compilation
    
    
    def test_write_none_eyed3(self):
        self.test_read_none_eyed3()
        
        audio = eyed3.load(noneMP3)
        
        audio.tag.title = unicode("title") # titre
        # sous-titre
        audio.tag.frame_set["POPM"] = eyed3.id3.frames.PopularityFrame(id="POPM", rating=1) # notation
        # commentaire
        audio.tag.artist = unicode("artist") # artiste ayant participé
        # artiste de l'album
        audio.tag.album = unicode("album") # album
        # année
        audio.tag.track_num = 11 # n°
        audio.tag.genre = eyed3.id3.Genre(u"genre") # genre
        audio.tag.publisher = unicode("publisher") # éditeur
        # encodé par
        audio.tag.artist_url = unicode("urlAuteur") # URL de l'auteur
        # compositeur
        # chef d'orchestre
        # description du groupe
        # ambiance
        audio.tag.disc_num = 1 # partie du coffret
        # clé d'origine
        audio.tag.bpm = 111 # battements par minute
        # partie d'une compilation
        
        audio.tag.save()
        
        audio = eyed3.load(noneMP3)
        
        self.assertEqual(audio.tag.title, "title") # titre
        # sous-titre
        self.assertEqual(audio.tag.frame_set["POPM"][0].rating, 1) # notation
        # commentaire
        self.assertEqual(audio.tag.artist, "artist") # artiste ayant participé
        # artiste de l'album
        self.assertEqual(audio.tag.album, "album") # album
        # année
        self.assertEqual(audio.tag.track_num[0], 11) # n°
        self.assertEqual(audio.tag.genre.name, "genre") # genre
        self.assertEqual(audio.tag.publisher, "publisher") # éditeur
        # encodé par
        self.assertEqual(audio.tag.artist_url, "urlAuteur") # URL de l'auteur
        # compositeur
        # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(audio.tag.disc_num[0], 1) # partie du coffret
        # clé d'origine
        self.assertEqual(audio.tag.bpm, 111) # battements par minute
        # partie d'une compilation
    
    
    def test_write_none_mutagen(self):
        self.test_read_none_mutagen()
        
        audio = mutagen.easyid3.EasyID3(noneMP3)
        
        audio["title"] = "title" # titre
        audio["version"] = "subtitle" # sous-titre
        # notation
        # commentaire
        audio["artist"] = "artist" # artiste ayant participé
        audio["performer"] = "albumArtist" # artiste de l'album
        audio["album"] = "album" # album
        audio["date"] = "1111" # année
        audio["tracknumber"] = "11" # n°
        audio["genre"] = "genre" # genre
        audio["organization"] = "publisher" # éditeur
        audio["encodedby"] = "encodedBy" # encodé par
        audio["website"] = "urlAuteur" # URL de l'auteur
        audio["composer"] = "composer" # compositeur
        audio["conductor"] = "conductor" # chef d'orchestre
        # description du groupe
        # ambiance
        audio["discnumber"] = "1" # partie du coffret
        # clé d'origine
        audio["bpm"] = "111" # battements par minute
        audio["compilation"] = "0" # partie d'une compilation
        
        audio.save()
        
        audio = mutagen.easyid3.EasyID3(noneMP3)
        
        self.assertEqual(audio["title"][0], "title") # titre
        self.assertEqual(audio["version"][0], "subtitle") # sous-titre
        # notation
        # commentaire
        self.assertEqual(audio["artist"][0], "artist") # artiste ayant participé
        self.assertEqual(audio["performer"][0], "albumArtist") # artiste de l'album
        self.assertEqual(audio["album"][0], "album") # album
        self.assertEqual(audio["date"][0], "1111") # année
        self.assertEqual(audio["tracknumber"][0], "11") # n°
        self.assertEqual(audio["genre"][0], "genre") # genre
        self.assertEqual(audio["organization"][0], "publisher") # éditeur
        self.assertEqual(audio["encodedby"][0], "encodedBy") # encodé par
        self.assertEqual(audio["website"][0], "urlAuteur") # URL de l'auteur
        self.assertEqual(audio["composer"][0], "composer") # compositeur
        self.assertEqual(audio["conductor"][0], "conductor") # chef d'orchestre
        # description du groupe
        # ambiance
        self.assertEqual(audio["discnumber"][0], "1") # partie du coffret
        # clé d'origine
        self.assertEqual(audio["bpm"][0], "111") # battements par minute
        self.assertEqual(audio["compilation"][0], "0") # partie d'une compilation
    
    



#print audio.info.time_secs # ?

#print int(audio["arranger"][0])
#print mutagen.easyid3.EasyID3.valid_keys.keys()
#print mutagen.File(audio_path, easy=True)



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