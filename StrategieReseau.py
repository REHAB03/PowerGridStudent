from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
        #déclaration des noeuds et des arcs
        noeuds: dict[int, tuple[int, int]] = {} 
        arcs: list[tuple[int, int]] = [] 
        
        #initialisation du noeud d'entrée
        id_entree = 0
        x_entree = int(input("Saisir x du noeud d'entrée : "))
        y_entree = int(input("Saisir y du noeud d'entrée : "))
        noeuds[id_entree] = (x_entree, y_entree)
        
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
            id_a = int(input("Id du premier noeud : "))
            id_b = int(input("Id du second noeud : "))
        #si les ids sont valides
            arcs.append((id_a, id_b))
            reponse = input("Ajouter un autre arc ? (o/n) : ")
        
        return id_entree, noeuds, arcs

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[tuple[int, int]]]:
       
         noeuds = {}
         arcs = []

         entree = None
         for y, ligne in enumerate(t.cases):
            for x, case in enumerate(ligne):
                if case == Case.ENTREE:
                    entree = (y, x)
                    break
            if entree:
                break

         if not entree:
            return -1, {}, []

         noeuds[0] = entree
         nid = 1

         for y, ligne in enumerate(t.cases):
            for x, case in enumerate(ligne):
                if case == Case.CLIENT:
                    noeuds[nid] = (y, x)
                    arcs.append((0, nid))
                    nid += 1

         return 0, noeuds, arcs