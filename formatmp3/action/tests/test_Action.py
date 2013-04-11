#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Tests unitaire du module formatmp3.action.Action
@author: Julien
'''



from formatmp3.action.Action import *
import unittest



class TestAction(unittest.TestCase):
    '''
    Tests de la classe formatmp3.action.Action
    @author: Julien
    '''
    
    
    def test_getFilename(self):
        action = Action()
        action.path = "C:\\path\\fichier.ext"
        self.assertEqual(action.filename, "fichier")
    
    
    def test_setFilename(self):
        action = Action()
        action.path = "C:\\path\\fichier.ext"
        action.filename = "toto"
        self.assertEqual(action.filename, "toto")
        self.assertEqual(action.path, "C:\\path\\toto.ext")




class TestCaseChange(unittest.TestCase):
    '''
    Tests de la classe formatmp3.action.CaseChange
    @author: Julien
    '''
    
    
    def test_execute_noExtension(self):
        action = CaseChange()
        action.path = "C:\\PATH\\nom DE FicHier AveC EspaCes"
        action.execute()
        self.assertEqual(action.path, "C:\\PATH\\Nom de fichier avec espaces")
    
    
    def test_execute_ok(self):
        action = CaseChange()
        action.path = "C:\\PATH\\nom DE FicHier AveC EspaCes.EXT"
        action.execute()
        self.assertEqual(action.path, "C:\\PATH\\Nom de fichier avec espaces.EXT")



class TestReplaceString(unittest.TestCase):
    '''
    Tests de la classe formatmp3.action.ReplaceString
    @author: Julien
    '''
    
    
    def test_execute_ok(self):
        action = ReplaceString()
        action.path = "C:\\PATH\\remplacer_les__under___score.EXT"
        action.oldStr = "_"
        action.newStr = " "
        action.execute()
        self.assertEqual(action.path, "C:\\PATH\\remplacer les  under   score.EXT")



class TestCut(unittest.TestCase):
    '''
    Tests de la classe formatmp3.action.Cut
    @author: Julien
    '''
    
    
    def test_setX_valeursIncorrectes(self):
        action = Cut()
        self.assertRaises(ValueError, action.set_nomber, -1)
        self.assertRaises(ValueError, action.set_position, -1)
    
    
    def test_execute(self):
        listParams = [# 1er caractère
                      [0, 0, InsertString.A_PARTIR_DEBUT, "0123456789"], # rien
                      [1, 0, InsertString.A_PARTIR_DEBUT, "123456789"],
                      [5, 0, InsertString.A_PARTIR_DEBUT, "56789"],
                      [9, 0, InsertString.A_PARTIR_DEBUT, "9"],
                      [10, 0, InsertString.A_PARTIR_DEBUT, ""], # jusqu'au bout
                      [11, 0, InsertString.A_PARTIR_DEBUT, ""], # débordement
                      # caractère du milieu
                      [0, 5, InsertString.A_PARTIR_DEBUT, "0123456789"], # rien
                      [1, 5, InsertString.A_PARTIR_DEBUT, "012346789"],
                      [2, 5, InsertString.A_PARTIR_DEBUT, "01234789"],
                      [4, 5, InsertString.A_PARTIR_DEBUT, "012349"],
                      [5, 5, InsertString.A_PARTIR_DEBUT, "01234"], # jusqu'au bout
                      [6, 5, InsertString.A_PARTIR_DEBUT, "01234"], # débordement
                      # dernier caractère
                      [0, 9, InsertString.A_PARTIR_DEBUT, "0123456789"], # rien
                      [1, 9, InsertString.A_PARTIR_DEBUT, "012345678"], # rien
                      [2, 9, InsertString.A_PARTIR_DEBUT, "012345678"], # débordement
                      # caractère hors du nom
                      [0, 10, InsertString.A_PARTIR_DEBUT, "0123456789"],
                      [1, 10, InsertString.A_PARTIR_DEBUT, "0123456789"]]
        for nomber, position, sens, resultat in listParams:
            action = Cut()
            action.path = "C:\\PATH\\0123456789.EXT"
            action.nomber = nomber
            action.position = position
            action.sens = sens
            action.execute()
            self.assertEquals(action.path, "C:\\PATH\\" + resultat + ".EXT")



class TestInsertString(unittest.TestCase):
    '''
    Tests de la classe formatmp3.action.InsertString
    @author: Julien
    '''
    
    
    def test_execute(self):
        listParams = [[0, InsertString.A_PARTIR_DEBUT, "_0123456789"],
                      [1, InsertString.A_PARTIR_DEBUT, "0_123456789"],
                      [5, InsertString.A_PARTIR_DEBUT, "01234_56789"],
                      [9, InsertString.A_PARTIR_DEBUT, "012345678_9"],
                      [10, InsertString.A_PARTIR_DEBUT, "0123456789_"],
                      [11, InsertString.A_PARTIR_DEBUT, "0123456789_"],
                      [0, InsertString.A_PARTIR_FIN, "0123456789_"],
                      [1, InsertString.A_PARTIR_FIN, "012345678_9"],
                      [5, InsertString.A_PARTIR_FIN, "01234_56789"],
                      [9, InsertString.A_PARTIR_FIN, "0_123456789"],
                      [10, InsertString.A_PARTIR_FIN, "_0123456789"],
                      [11, InsertString.A_PARTIR_FIN, "_0123456789"]]
        for position, sens, resultat in listParams:
            action = InsertString()
            action.path = "C:\\PATH\\0123456789.EXT"
            action.string = "_"
            action.position = position
            action.sens = sens
            action.execute()
            self.assertEquals(action.path, "C:\\PATH\\" + resultat + ".EXT")
        

if __name__ == "__main__":
    unittest.main()
