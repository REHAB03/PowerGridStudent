
from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
       #déclaration des noeuds et arcs
        noeuds: dict[int, tuple[int, int]]
        arcs: list[tuple[int, int]]
       #initialisation du noeud d'entrée
        id_entree = 0
        x_entree = int(input("saisir x du noeud d'entree:"))
        y_entree = int(input("saisir y du noeud d'entree:"))
        noeuds[id_entree]= (x_entree,y_entree)
        #ajout des noeuds
        reponse = input("Ajouter un autre noeud ? (yes/no) : ")
        id_next = 1
        while reponse == "yes":
            print(f"--- Noeud {id_next} ---")
            x = int(input("x : "))
            y = int(input("y : "))
            noeuds[id_next] = (x, y)
            id_next += 1
            reponse = input("Ajouter un autre noeud ? (yes/no) : ")
        return -1, {}, []

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        # TODO
        return -1, {}, []

