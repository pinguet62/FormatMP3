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
    
    
    def test_operators(self):
        # __eq__
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier.ext"), Path("C:\\chemin\\du\\repertoire\\fichier.ext"))
        self.assertNotEqual(Path("C:\\chemin\\repertoire\\fichier.ext"), Path("C:\\chemin\\différent\\fichier.eXt"))
        
        # __str__
        string = "C:\\chemin\\du\\repertoire\\fichier.ext"
        self.assertEqual(str(Path(string)), string)
        
        # list.sort()
        liste = [Path("C:\\path5"), Path("C:\\path3"), Path("C:\\path1"), Path("C:\\path2"), Path("C:\\path4")]
        liste.sort()
        self.assertListEqual(liste, [Path("C:\\path1"), Path("C:\\path2"), Path("C:\\path3"), Path("C:\\path4"), Path("C:\\path5")])
        
        # in list
        liste = [Path("C:\\path1"), Path("C:\\path2")]
        self.assertIn(Path("C:\\path1"), liste)
        liste = [Path("C:\\path1"), Path("C:\\path2")]
        self.assertNotIn(Path("C:\\toto"), liste)
    
    
    def test_swap(self):
        listUp = [Path("C:\\path1"), Path("C:\\path2"), Path("C:\\path3")]
        i = 1
        listUp[i], listUp[i-1] = listUp[i-1], listUp[i]
        self.assertListEqual(listUp, [Path("C:\\path2"), Path("C:\\path1"), Path("C:\\path3")])
        
        listDown = [Path("C:\\path1"), Path("C:\\path2"), Path("C:\\path3")]
        i = 1
        listDown[i], listDown[i+1] = listDown[i+1], listDown[i]
        self.assertListEqual(listDown, [Path("C:\\path1"), Path("C:\\path3"), Path("C:\\path2")])
    
    
    def test_get_basename(self):
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\").basename, "repertoire")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier").basename, "fichier")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\.ext").basename, ".ext")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier.ext").basename, "fichier.ext")
    
    
    def test_set_basename(self):
        # "fichier"
        path = Path("C:\\chemin\\du\\repertoire\\fichier")
        path.basename = "toto"
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\toto")
        
        path = Path("C:\\chemin\\du\\repertoire\\.ext")
        path.basename = "toto"
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\toto")
        
        path = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        path.basename = "toto"
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\toto")
        
        # ".ext"
        path = Path("C:\\chemin\\du\\repertoire\\fichier")
        path.basename = ".con"
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\.con")
        
        path = Path("C:\\chemin\\du\\repertoire\\.ext")
        path.basename = ".con"
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\.con")
        
        path = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        path.basename = ".con"
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\.con")
        
        # "fichier.ext"
        path = Path("C:\\chemin\\du\\repertoire\\fichier")
        path.basename = "toto.con"
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\toto.con")
        
        path = Path("C:\\chemin\\du\\repertoire\\.ext")
        path.basename = "toto.con"
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\toto.con")
        
        path = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        path.basename = "toto.con"
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\toto.con")
        
    
    
    def test_get_filename(self):
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\").filename, "repertoire")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier").filename, "fichier")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\.ext").filename, "")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier.ext").filename, "fichier")
    
    
    def test_set_filename(self):
        path = Path("C:\\chemin\\du\\repertoire\\fichier")
        self.assertRaises(ValueError, path.set_filename, "")
        
        path = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        path.filename = ""
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\.ext")
        
        path = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        path.filename = "toto"
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\toto.ext")
    
    
    def test_get_extension(self):
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier").extension, "")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\.ext").extension, "ext")
        self.assertEqual(Path("C:\\chemin\\du\\repertoire\\fichier.ext").extension, "ext")
    
    
    def test_set_extension(self):
        path = Path("C:\\chemin\\du\\repertoire\\.ext")
        self.assertRaises(ValueError, path.set_extension, "")
        
        path = Path("C:\\chemin\\du\\repertoire\\fichier")
        path.extension = "con"
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\fichier.con")
        
        path = Path("C:\\chemin\\du\\repertoire\\fichier.ext")
        path.extension = "con"
        self.assertEqual(path.get(), "C:\\chemin\\du\\repertoire\\fichier.con")



if __name__ == "__main__":
    unittest.main()