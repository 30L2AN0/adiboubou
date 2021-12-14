global liste_obstacles, liste_blocs, liste_regles, taille, grille, liste_liste_objets

taille = 40
liste_blocs = []
liste_obstacles = []
liste_regles = []
grille = [[None for j in range(640//taille)] for i in range(1200//taille)]

class Obstacle:
    def __init__(self, mot, position):
        self.mot = mot
        self.position = position

    def set(self, pos):
        self.position = pos

    def copy(self):
        b = Obstacle(self.mot, self.position)
        return b

class Bloc(Obstacle):
    def __init__(self, type, nom_affiche, mot, position):
        Obstacle.__init__(self, mot, position)
        self.type = type
        self.nom_affiche = nom_affiche

    def copy(self):
        a = Bloc(self.type, self.nom_affiche, self.mot, self.position)
        return a
