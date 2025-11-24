from Terrain import Terrain, Case
from StrategieReseau import StrategieReseau, StrategieReseauAuto

class Reseau:
    def __init__(self):
        self.strat = StrategieReseauAuto()
        self.noeuds = {}
        self.arcs = []
        self.noeud_entree = -1

    def definir_entree(self, n: int) -> None:
        if n in self.noeuds.keys():
            self.noeud_entree = n
        else:
            self.noeud_entree = -1

    def ajouter_noeud(self, n: int, coords: tuple[int, int]):
        if n >= 0:
            self.noeuds[n] = coords

    def ajouter_arc(self, n1: int, n2: int) -> None:
        if n1 > n2:
            tmp = n2
            n2 = n1
            n1 = tmp
        if n1 not in self.noeuds.keys() or n2 not in self.noeuds.keys():
            return
        if (n1, n2) not in self.arcs:
            self.arcs.append((n1, n2))

    def set_strategie(self, strat: StrategieReseau):
        self.strat = strat

    def valider_reseau(self) -> bool:
        if not self.noeuds:
            return False
        
        if self.noeud_entree == -1 or self.noeud_entree not in self.noeuds:
            return False
        
        if len(self.noeuds) == 1:
            return True
        
        visites = set()
        file = [self.noeud_entree]
        visites.add(self.noeud_entree)
        
        adjacence = {n: [] for n in self.noeuds.keys()}
        for n1, n2 in self.arcs:
            adjacence[n1].append(n2)
            adjacence[n2].append(n1)
        
        while file:
            noeud_actuel = file.pop(0)
            for voisin in adjacence[noeud_actuel]:
                if voisin not in visites:
                    visites.add(voisin)
                    file.append(voisin)
        
        return len(visites) == len(self.noeuds)

    def valider_distribution(self, t: Terrain) -> bool:
        if not self.valider_reseau():
            return False
        
        for coords in self.noeuds.values():
            x, y = coords
            if x < 0 or y < 0 or x >= len(t.cases) or y >= len(t.cases[0]):
                return False
            if t.cases[x][y] == Case.OBSTACLE:
                return False
        
        clients = []
        for x in range(len(t.cases)):
            for y in range(len(t.cases[0])):
                if t.cases[x][y] == Case.CLIENT:
                    clients.append((x, y))
        
        if not clients:
            return True
        
        rayon_desserte = 2
        
        for client_x, client_y in clients:
            est_desservi = False
            for noeud_coords in self.noeuds.values():
                noeud_x, noeud_y = noeud_coords
                distance = abs(client_x - noeud_x) + abs(client_y - noeud_y)
                if distance <= rayon_desserte:
                    est_desservi = True
                    break
            
            if not est_desservi:
                return False
        
        return True

    def configurer(self, t: Terrain):
        self.noeud_entree, self.noeuds, self.arcs = self.strat.configurer(t)

    def afficher(self) -> None:
        print("Noeud d'entrée :", self.noeud_entree)
        print("Les noeuds :", self.noeuds)
        print("Les arcs :", self.arcs)

    def afficher_avec_terrain(self, t: Terrain) -> None:
        for ligne in range(len(t.cases)):
            for colonne in range(len(t.cases[0])):
                case = t.cases[ligne][colonne]
                
                noeud_present = (ligne, colonne) in self.noeuds.values()
                
                if noeud_present:
                    if case == Case.ENTREE:
                        print("E", end="")
                    elif case == Case.CLIENT:
                        print("©", end="")
                    elif case == Case.OBSTACLE:
                        print("T", end="")
                    else:
                        print("+", end="")
                else:
                    if case == Case.OBSTACLE:
                        print("X", end="")
                    elif case == Case.CLIENT:
                        print("C", end="")
                    elif case == Case.VIDE:
                        print("~", end="")
                    elif case == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
            print()

    def calculer_cout(self, t: Terrain) -> float:
        cout = 0.0
        
        for _ in self.arcs:
            cout += 1.5
        
        for coords in self.noeuds.values():
            x, y = coords
            if x >= 0 and x < len(t.cases) and y >= 0 and y < len(t.cases[0]):
                if t.cases[x][y] == Case.OBSTACLE:
                    cout += 2
                else:
                    cout += 1
            else:
                cout += 10
        
        return cout