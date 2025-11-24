import unittest
import xmlrunner

from Reseau import Reseau
from Terrain import Terrain, Case

class TestReseau(unittest.TestCase):

    def test_definition_entree(self):
        r = Reseau()
        r.ajouter_noeud(0, (0, 0))
        r.definir_entree(0)
        self.assertEqual(r.noeud_entree, 0)
        r.definir_entree(99)
        self.assertEqual(r.noeud_entree, -1)

    def test_ajout_noeud(self):
        r = Reseau()
        r.ajouter_noeud(0, (0, 0))
        self.assertIn(0, r.noeuds)
        self.assertEqual(r.noeuds[0], (0, 0))
        r.ajouter_noeud(-1, (1, 1))
        self.assertNotIn(-1, r.noeuds)
        r.ajouter_noeud(1, (1, 0))
        r.ajouter_noeud(2, (0, 1))
        self.assertEqual(len(r.noeuds), 3)

    def test_ajout_arc(self):
        r = Reseau()
        r.ajouter_noeud(0, (0, 0))
        r.ajouter_noeud(1, (1, 0))
        r.ajouter_noeud(2, (0, 1))
        r.ajouter_arc(0, 1)
        self.assertIn((0, 1), r.arcs)
        r.ajouter_arc(2, 0)  
        self.assertIn((0, 2), r.arcs)
        r.ajouter_arc(0, 99)
        self.assertNotIn((0, 99), r.arcs)
        initial_arc_count = len(r.arcs)
        r.ajouter_arc(0, 1)
        self.assertEqual(len(r.arcs), initial_arc_count)

    def test_validation_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0
        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))
        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))
        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))
        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))
        self.assertTrue(r.valider_reseau())

    def test_validation_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0
        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))
        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))
        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))
        r.noeuds[4] = (1, 2)
        self.assertFalse(r.valider_reseau())

    def test_distribution_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0
        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))
        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))
        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))
        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))
        t = Terrain()
        t.cases = [
            [Case.ENTREE, Case.VIDE, Case.VIDE],
            [Case.CLIENT, Case.VIDE, Case.CLIENT],
        ]
        self.assertTrue(r.valider_distribution(t))

    def test_distribution_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0
        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))
        t = Terrain()
        t.cases = [
            [Case.ENTREE, Case.VIDE, Case.VIDE, Case.VIDE, Case.VIDE],
            [Case.CLIENT, Case.VIDE, Case.VIDE, Case.VIDE, Case.CLIENT],
        ]
        self.assertFalse(r.valider_distribution(t))

    def test_noeud_sur_obstacle(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0
        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))
        t = Terrain()
        t.cases = [
            [Case.ENTREE, Case.VIDE],
            [Case.OBSTACLE, Case.CLIENT],
        ]
        self.assertFalse(r.valider_distribution(t))

    def test_noeud_hors_limites(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0
        r.noeuds[1] = (5, 5)
        r.arcs.append((0, 1))
        t = Terrain()
        t.cases = [
            [Case.ENTREE, Case.VIDE],
            [Case.CLIENT, Case.VIDE],
        ]
        self.assertFalse(r.valider_distribution(t))

    def test_reseau_vide(self):
        r = Reseau()
        self.assertFalse(r.valider_reseau())

    def test_reseau_sans_entree(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))
        self.assertFalse(r.valider_reseau())

    def test_terrain_sans_clients(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0
        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))
        t = Terrain()
        t.cases = [
            [Case.ENTREE, Case.VIDE, Case.VIDE],
            [Case.VIDE, Case.VIDE, Case.VIDE],
        ]
        self.assertTrue(r.valider_distribution(t))

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))