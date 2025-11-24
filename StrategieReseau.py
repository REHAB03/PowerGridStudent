
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
        #ajout des arcs
        reponse = input("\nAjouter un arc ? (o/n) : ")
        while reponse == "o":
            print("Créer un arc entre deux noeuds")
            id_a = int(input("id du premier noeud : "))
            id_b = int(input("id du second noeud : "))
            # ici on suppose que les id sont valides (code simple)
            arcs.append((id_a, id_b))
            reponse = input("Ajouter un autre arc ? (o/n) : ")
        return id_entree, noeuds, arcs

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        # TODO
        return -1, {}, []

