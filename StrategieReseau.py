from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        
        noeuds: dict[int, tuple[int, int]] = {} 
        arcs: list[tuple[int, int]] = [] 
        
        
        id_entree = 0
        x_entree = int(input("Saisir x du noeud d'entrée : "))
        y_entree = int(input("Saisir y du noeud d'entrée : "))
        noeuds[id_entree] = (x_entree, y_entree)
        
        
        reponse = input("Ajouter un autre noeud ? (yes/no) : ")
        id_next = 1
        while reponse == "yes":
            print(f"--- Noeud {id_next} ---")
            x = int(input("x : "))
            y = int(input("y : "))
            noeuds[id_next] = (x, y)
            id_next += 1
            reponse = input("Ajouter un autre noeud ? (yes/no) : ")
        
        
        reponse = input("\nAjouter un arc ? (o/n) : ")
        while reponse == "o":
            print("Créer un arc entre deux noeuds")
            id_a = int(input("Id du premier noeud : "))
            id_b = int(input("Id du second noeud : "))
            
            arcs.append((id_a, id_b))
            reponse = input("Ajouter un autre arc ? (o/n) : ")
        
        return id_entree, noeuds, arcs

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
       
        noeuds: dict[int, tuple[int, int]] = {}
        arcs: list[tuple[int, int]] = []
        
        
        positions_valides = []
        for x in range(t.largeur):
            for y in range(t.hauteur):
                case = t.get_case(x, y)
                
                if case is not None:  
                    positions_valides.append((x, y))
        
        
        if not positions_valides:
            return -1, {}, []
        
        
        id_entree = 0
        noeuds[id_entree] = positions_valides[0]
        
       
        id_noeud = 1
        espacement = 5 
        
        for x in range(0, t.largeur, espacement):
            for y in range(0, t.hauteur, espacement):
                if (x, y) in positions_valides and (x, y) != noeuds[id_entree]:
                    noeuds[id_noeud] = (x, y)
                    id_noeud += 1
        
        
        ids = list(noeuds.keys())
        for i in range(len(ids) - 1):
            
            arcs.append((ids[i], ids[i + 1]))
        
        for i in range(0, len(ids) - 2, 2):
            if i + 2 < len(ids):
                arcs.append((ids[i], ids[i + 2]))
        
        return id_entree, noeuds, arcs