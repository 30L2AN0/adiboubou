global liste_obstacles, liste_blocs, liste_regles, taille, grille, liste_liste_objets, hauteur, largeur

taille = 40
hauteur = 680
largeur = 1200
liste_blocs = []
liste_obstacles = []
liste_regles = []
grille = [[None for j in range(hauteur//taille)] for i in range(largeur//taille)]

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
    def __init__(self, type, mot, position):
        Obstacle.__init__(self, mot, position)
        self.type = type

    def copy(self):
        a = Bloc(self.type, self.mot, self.position)
        return a
