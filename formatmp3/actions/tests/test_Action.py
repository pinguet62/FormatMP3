#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
Tests unitaire du module Action
@author: Julien
'''



from formatmp3.actions.Action import *
import unittest



class TestCaseChange(unittest.TestCase):
    '''
    Tests de la classe CaseChange
    @author: Julien
    '''
    
    
    def test_getOverview_filename_lower(self):
        action = CaseChange()
        action.range = PathModification.FILENAME
        action.modification = CaseChange.LOWER
        self.assertEqual(action.getOverview(Path("C:\\PATH\\nOm DE FicHier.eXt")).get(), "C:\\PATH\\nom de fichier.eXt")
    
    def test_getOverview_filename_firstMaj(self):
        action = CaseChange()
        action.range = PathModification.FILENAME
        action.modification = CaseChange.FIRST_MAJ
        self.assertEqual(action.getOverview(Path("C:\\PATH\\nOm DE FicHier.eXt")).get(), "C:\\PATH\\Nom de fichier.eXt")
    
    def test_getOverview_filename_title(self):
        action = CaseChange()
        action.range = PathModification.FILENAME
        action.modification = CaseChange.TITLE
        self.assertEqual(action.getOverview(Path("C:\\PATH\\nom DE FicHier.eXt")).get(), "C:\\PATH\\Nom De Fichier.eXt")
    
    def test_getOverview_filename_upper(self):
        action = CaseChange()
        action.range = PathModification.FILENAME
        action.modification = CaseChange.UPPER
        self.assertEqual(action.getOverview(Path("C:\\PATH\\nOm DE FicHier.eXt")).get(), "C:\\PATH\\NOM DE FICHIER.eXt")
    
    
    def test_getOverview_extension_lower(self):
        action = CaseChange()
        action.range = PathModification.EXTENSION
        action.modification = CaseChange.LOWER
        self.assertEqual(action.getOverview(Path("C:\\PATH\\nOm DE FicHier.eXt")).get(), "C:\\PATH\\nOm DE FicHier.ext")
    
    def test_getOverview_extension_firstMaj(self):
        action = CaseChange()
        action.range = PathModification.EXTENSION
        action.modification = CaseChange.FIRST_MAJ
        self.assertEqual(action.getOverview(Path("C:\\PATH\\nOm DE FicHier.eXt")).get(), "C:\\PATH\\nOm DE FicHier.Ext")
    
    def test_getOverview_extension_title(self):
        action = CaseChange()
        action.range = PathModification.EXTENSION
        action.modification = CaseChange.TITLE
        self.assertEqual(action.getOverview(Path("C:\\PATH\\nOm DE FicHier.eXt")).get(), "C:\\PATH\\nOm DE FicHier.Ext")
    
    def test_getOverview_extension_upper(self):
        action = CaseChange()
        action.range = PathModification.EXTENSION
        action.modification = CaseChange.UPPER
        self.assertEqual(action.getOverview(Path("C:\\PATH\\nOm DE FicHier.eXt")).get(), "C:\\PATH\\nOm DE FicHier.EXT")



class TestReplaceString(unittest.TestCase):
    '''
    Tests de la classe ReplaceString
    @author: Julien
    '''
    
    
    def test_getOverview_filename(self):
        action = ReplaceString()
        action.range = PathModification.FILENAME
        action.oldStr = "_"
        action.newStr = " "
        self.assertEqual(action.getOverview(Path("C:\\PATH_ESPACE\\remplacer_les__under___score.e_t")).get(), "C:\\PATH_ESPACE\\remplacer les  under   score.e_t")
    
    def test_getOverview_extension(self):
        action = ReplaceString()
        action.range = PathModification.EXTENSION
        action.oldStr = "_"
        action.newStr = " "
        self.assertEqual(action.getOverview(Path("C:\\PATH_ESPACE\\remplacer_les__under___score.e_t")).get(), "C:\\PATH_ESPACE\\remplacer_les__under___score.e t")



class TestCut(unittest.TestCase):
    '''
    Tests de la classe Cut
    @author: Julien
    '''
    
    
    def test_setX_valeursIncorrectes(self):
        action = Cut()
        self.assertRaises(ValueError, action.set_nomber, -1)
        self.assertRaises(ValueError, action.set_position, -1)
    
    
    def test_getOverview_aPartirDebut_filename(self):
        listParams = [# 1er caractère
                      [0, 0, "0123456789"], # rien
                      [0, 1, "123456789"],
                      [0, 5, "56789"],
                      [0, 9, "9"],
                      [0, 10, ""], # jusqu'au bout
                      [0, 11, ""], # débordement
                      # caractère du milieu
                      [5, 0, "0123456789"], # rien
                      [5, 1, "012346789"],
                      [5, 2, "01234789"],
                      [5, 4, "012349"],
                      [5, 5, "01234"], # jusqu'au bout
                      [5, 6, "01234"], # débordement
                      # dernier caractère
                      [9, 0, "0123456789"], # rien
                      [9, 1, "012345678"], # jusqu'au bout
                      [9, 2, "012345678"], # débordement
                      # caractère hors du nom
                      [10, 0, "0123456789"],
                      [10, 1, "0123456789"]]
        for position, nomber, resultat in listParams:
            action = Cut()
            action.range = PathModification.FILENAME
            action.position = position
            action.nomber = nomber
            action.sens = Cut.A_PARTIR_DEBUT
            self.assertEquals(action.getOverview(Path("C:\\PATH\\0123456789.ext")).get(), "C:\\PATH\\" + resultat + ".ext", "'%s' != '%s' pour (position, nomber)=(%d, %d)" % (action.getOverview(Path("C:\\PATH\\0123456789.ext")).get(), "C:\\PATH\\" + resultat + ".ext", position, nomber))
    
    def test_getOverview_aPartirDebut_extension(self):
        listParams = [# 1er caractère
                      [0, 0, ".012"], # rien
                      [0, 1, ".12"],
                      [0, 2, ".2"],
                      [0, 3, ""], # jusqu'au bout
                      [0, 4, ""], # débordement
                      # caractère du milieu
                      [1, 0, ".012"], # rien
                      [1, 1, ".02"],
                      [1, 2, ".0"], # jusqu'au bout
                      [1, 3, ".0"], # débordement
                      # dernier caractère
                      [2, 0, ".012"], # rien
                      [2, 1, ".01"],
                      [2, 2, ".01"], # débordement
                      # caractère hors du nom
                      [3, 0, ".012"],
                      [3, 1, ".012"]]
        for position, nomber, resultat in listParams:
            action = Cut()
            action.range = PathModification.EXTENSION
            action.position = position
            action.nomber = nomber
            action.sens = Cut.A_PARTIR_DEBUT
            self.assertEquals(action.getOverview(Path("C:\\PATH\\fichier.012")).get(), "C:\\PATH\\fichier" + resultat, "'%s' != '%s' pour (position, nomber)=(%d, %d)" % (action.getOverview(Path("C:\\PATH\\fichier.0123")).get(), "C:\\PATH\\fichier" + resultat, position, nomber))
    
    
    def test_getOverview_aPartirFin_filename(self):
        listParams = [# dernier caractère
                      [0, 0, "0123456789"], # rien
                      [0, 1, "012345678"],
                      [0, 5, "01234"],
                      [0, 9, "0"],
                      [0, 10, ""], # jusqu'au bout
                      [0, 11, ""], # débordement
                      # caractère du milieu
                      [5, 0, "0123456789"], # rien
                      [5, 1, "012356789"],
                      [5, 2, "01256789"],
                      [5, 4, "056789"],
                      [5, 5, "56789"], # jusqu'au bout
                      [5, 6, "56789"], # débordement
                      # 1er caractère
                      [9, 0, "0123456789"], # rien
                      [9, 1, "123456789"], # jusqu'au bout
                      [9, 2, "123456789"], # débordement
                      # caractère hors du nom
                      [10, 0, "0123456789"],
                      [10, 1, "0123456789"]]
        for position, nomber, resultat in listParams:
            action = Cut()
            action.range = PathModification.FILENAME
            action.position = position
            action.nomber = nomber
            action.sens = Cut.A_PARTIR_FIN
            self.assertEquals(action.getOverview(Path("C:\\PATH\\0123456789.ext")).get(), "C:\\PATH\\" + resultat + ".ext", "'%s' != '%s' pour (position, nomber)=(%d, %d)" % (action.getOverview(Path("C:\\PATH\\0123456789.ext")).get(), "C:\\PATH\\" + resultat + ".ext", position, nomber))
    
    def test_getOverview_aPartirFin_extension(self):
        listParams = [# dernier caractère
                      [0, 0, ".012"], # rien
                      [0, 1, ".01"],
                      [0, 2, ".0"],
                      [0, 3, ""], # jusqu'au bout
                      [0, 4, ""], # débordement
                      # caractère du milieu
                      [1, 0, ".012"], # rien
                      [1, 1, ".02"],
                      [1, 2, ".2"], # jusqu'au bout
                      [1, 3, ".2"], # débordement
                      # 1er caractère
                      [2, 0, ".012"], # rien
                      [2, 1, ".12"],
                      [2, 2, ".12"], # débordement
                      # caractère hors du nom
                      [3, 0, ".012"],
                      [3, 1, ".012"]]
        for position, nomber, resultat in listParams:
            action = Cut()
            action.range = PathModification.EXTENSION
            action.position = position
            action.nomber = nomber
            action.sens = Cut.A_PARTIR_FIN
            self.assertEquals(action.getOverview(Path("C:\\PATH\\fichier.012")).get(), "C:\\PATH\\fichier" + resultat, "'%s' != '%s' pour (position, nomber)=(%d, %d)" % (action.getOverview(Path("C:\\PATH\\fichier.0123")).get(), "C:\\PATH\\fichier" + resultat, position, nomber))



class TestInsertString(unittest.TestCase):
    '''
    Tests de la classe InsertString
    @author: Julien
    '''
    
    
    def test_getOverview_aPartirDebut_filename(self):
        listParams = [# position correcte
                      [0, "toto01234"],
                      [1, "0toto1234"],
                      [2, "01toto234"],
                      [3, "012toto34"],
                      [4, "0123toto4"],
                      # débordement
                      [5, "01234toto"],
                      [6, "01234toto"]]
        for position, resultat in listParams:
            action = InsertString()
            action.range = PathModification.FILENAME
            action.position = position
            action.string = "toto"
            action.sens = Cut.A_PARTIR_DEBUT
            self.assertEquals(action.getOverview(Path("C:\\PATH\\01234.ext")).get(), "C:\\PATH\\" + resultat + ".ext", "'%s' != '%s' pour position=%d" % (action.getOverview(Path("C:\\PATH\\0123456789.ext")).get(), "C:\\PATH\\" + resultat + ".ext", position))
    
    def test_getOverview_aPartirDebut_extension(self):
        listParams = [# position correcte
                      [0, ".ext012"],
                      [1, ".0ext12"],
                      [2, ".01ext2"],
                      # débordement
                      [3, ".012ext"],
                      [4, ".012ext"]]
        for position, resultat in listParams:
            action = InsertString()
            action.range = PathModification.EXTENSION
            action.position = position
            action.string = "ext"
            action.sens = Cut.A_PARTIR_DEBUT
            self.assertEquals(action.getOverview(Path("C:\\PATH\\fichier.012")).get(), "C:\\PATH\\fichier" + resultat, "'%s' != '%s' pour position=%d" % (action.getOverview(Path("C:\\PATH\\fichier.012")).get(), "C:\\PATH\\fichier" + resultat, position))
    
    
    def test_getOverview_aPartirFin_filename(self):
        listParams = [# position correcte
                      [0, "01234toto"],
                      [1, "0123toto4"],
                      [2, "012toto34"],
                      [3, "01toto234"],
                      [4, "0toto1234"],
                      # débordement
                      [5, "toto01234"],
                      [6, "toto01234"]]
        for position, resultat in listParams:
            action = InsertString()
            action.range = PathModification.FILENAME
            action.position = position
            action.string = "toto"
            action.sens = Cut.A_PARTIR_FIN
            self.assertEquals(action.getOverview(Path("C:\\PATH\\01234.ext")).get(), "C:\\PATH\\" + resultat + ".ext", "'%s' != '%s' pour position=%d" % (action.getOverview(Path("C:\\PATH\\0123456789.ext")).get(), "C:\\PATH\\" + resultat + ".ext", position))
    
    def test_getOverview_aPartirFin_extension(self):
        listParams = [# position correcte
                      [0, ".012ext"],
                      [1, ".01ext2"],
                      [2, ".0ext12"],
                      # débordement
                      [3, ".ext012"],
                      [4, ".ext012"]]
        for position, resultat in listParams:
            action = InsertString()
            action.range = PathModification.EXTENSION
            action.position = position
            action.string = "ext"
            action.sens = Cut.A_PARTIR_FIN
            self.assertEquals(action.getOverview(Path("C:\\PATH\\fichier.012")).get(), "C:\\PATH\\fichier" + resultat, "'%s' != '%s' pour position=%d" % (action.getOverview(Path("C:\\PATH\\fichier.012")).get(), "C:\\PATH\\fichier" + resultat, position))



if __name__ == "__main__":
    unittest.main()