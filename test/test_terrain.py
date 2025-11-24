
import unittest
import xmlrunner

from Terrain import Terrain, Case

class TestTerrain(unittest.TestCase):

    def test_chargement(self):
        #fichier de test représente le terrain
        contenu = """E~ /n
        ~C~/n
         ~~~/n"""
        with open("terrain_test.txt", "w") as f:
           f.write(contenu)
        #chargement du fichier
        t = Terrain()
        t.charger("terrain_test.txt")
        #vérification
        self.assertEqual(t.largeur, 3)
        self.assertEqual(t.hauteur, 3)
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[0][2], Case.OBSTACLE)
        self.assertEqual(t[1][0], Case.VIDE)
        self.assertEqual(t[1][1], Case.CLIENT)
        self.assertEqual(t[1][2], Case.VIDE)
        self.assertEqual(t[2][0], Case.VIDE)
        self.assertEqual(t[2][1], Case.VIDE)
        self.assertEqual(t[2][2], Case.VIDE)

    def test_accesseur(self):
        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]
        self.assertEqual(t[0][0], Case.ENTREE)
        self.assertEqual(t[0][1], Case.VIDE)
        self.assertEqual(t[1][2], Case.CLIENT)

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

