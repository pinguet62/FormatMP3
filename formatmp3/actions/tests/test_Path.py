#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Tests unitaire du module Path
@author: Julien
'''



import unittest
from formatmp3.actions.Path import *



class TestModification(unittest.TestCase):
    '''
    Tests de la classe PathModification
    @author: Julien
    '''
    
    
    def test_filename(self):
        modif = PathModification()
        modif.path = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        modif.range = PathModification.FILENAME
        modif.set("toto")
        self.assertEqual(modif.path.get(), "C:\\chemin\\du\\repertoire\\toto.ext")
    
    
    def test_extension(self):
        modif = PathModification()
        modif.path = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        modif.range = PathModification.EXTENSION
        modif.set("toto")
        self.assertEqual(modif.path.get(), "C:\\chemin\\du\\repertoire\\fichier.toto")
    
    
    #def test_basename(self):
    #    modif = PathModification()
    #    modif.path = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
    #    modif.range = PathModification.BASENAME
    #    modif.set("toto")
    #    self.assertEqual(modif.path.get(), "C:\\chemin\\du\\repertoire\\toto")



class TestPath(unittest.TestCase):
    '''
    Tests de la classe Path
    @author: Julien
    '''
    
    def test_get_basename(self):
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier.ext").basename, "fichier.ext")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier").basename, "fichier")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier\\").basename, "")
    
    
    def test_set_basename(self):
        path = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        path.basename = "toto.con"
        self.assertEqual(path.basename, "toto.con")
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\toto.con")
    
    
    def test_get_filename(self):
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier.ext").filename, "fichier")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier").filename, "fichier")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier\\").filename, "")
    
    
    def test_set_filename(self):
        path = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        path.filename = "toto"
        self.assertEqual(path.filename, "toto")
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\toto.ext")
    
    
    def test_get_extension(self):
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier.ext").extension, "ext")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier").extension, "")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier\\").extension, "")
    
    
    def test_set_extension(self):
        path1 = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        path1.extension = "toto"
        self.assertEqual(path1.extension, "toto")
        self.assertEqual(path1.get(), "C:\\chemin\\du\\repertoire\\fichier.toto")
        
        path2 = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        path2.extension = ".toto"
        self.assertEqual(path2.extension, "toto")
        self.assertEqual(path2.get(), "C:\\chemin\\du\\repertoire\\fichier.toto")
        
        path3 = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        path3.extension = "."
        self.assertEqual(path3.extension, "")
        self.assertEqual(path3.get(), "C:\\chemin\\du\\repertoire\\fichier")
        
        path4 = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        path4.extension = ""
        self.assertEqual(path4.extension, "")
        self.assertEqual(path4.get(), "C:\\chemin\\du\\repertoire\\fichier")
        
        



if __name__ == "__main__":
    unittest.main()