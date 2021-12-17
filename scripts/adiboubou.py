#and compliqué à ajouter
#text compliqué à ajouter
#faire l'application des nouvelles regles


from __init__ import *

global liste_obstacles, liste_blocs, liste_regles, taille, grille, liste_liste_objets, images_blocs, images_obstacles, images_autres

from regles import *
exec(open("regles.py").read())
from rewind import *
exec(open("rewind.py").read())
exec(open("graphismes.py").read())

#on met à jour les listes en fonction de la map choisie
from map1 import *
exec(open("map1.py").read())

liste_liste_objets = [(copy_blocs(liste_blocs), copy_obstacles(liste_obstacles))]
grille, images_blocs, images_obstacles = afficher_grille0(liste_blocs, liste_obstacles)
liste_regles, images_obstacles = nouvelles_regles(liste_blocs, images_obstacles)
images_autres = []
for i in range(len(liste_obstacles)):
    images_obstacles = nouvelle_grille_is(liste_regles, liste_obstacles[i], i, images_obstacles)


def gauche(event):
    global liste_regles, grille, liste_obstacles, liste_blocs, liste_regles, liste_liste_objets, images_blocs, images_obstacles, images_autres
    if checker_regles(liste_regles, images_autres):
        a = check_deplacement([-1,0], liste_regles, liste_blocs, liste_obstacles, grille, liste_liste_objets)
        liste_regles, images_obstacles = nouvelles_regles(liste_blocs, images_obstacles)
        grille, images_blocs, images_obstacles = afficher_grille(liste_blocs, liste_obstacles, images_blocs, images_obstacles, liste_liste_objets, a)
    checker_regles(liste_regles, images_autres)

def droite(event):
    global liste_regles, grille, liste_obstacles, liste_blocs, liste_regles, liste_liste_objets, images_blocs, images_obstacles, images_autres
    if checker_regles(liste_regles, images_autres):
        a = check_deplacement([1,0], liste_regles, liste_blocs, liste_obstacles, grille, liste_liste_objets)
        liste_regles, images_obstacles = nouvelles_regles(liste_blocs, images_obstacles)
        grille,images_blocs, images_obstacles = afficher_grille(liste_blocs, liste_obstacles, images_blocs, images_obstacles, liste_liste_objets, a)
    checker_regles(liste_regles, images_autres)

def haut(event):
    global liste_regles, grille, liste_obstacles, liste_blocs, liste_regles, liste_liste_objets, images_blocs, images_obstacles, images_autres
    if checker_regles(liste_regles, images_autres):
        a = check_deplacement([0,-1], liste_regles, liste_blocs, liste_obstacles, grille, liste_liste_objets)
        liste_regles, images_obstacles = nouvelles_regles(liste_blocs, images_obstacles)
        grille, images_blocs, images_obstacles = afficher_grille(liste_blocs, liste_obstacles, images_blocs, images_obstacles, liste_liste_objets, a)
    checker_regles(liste_regles, images_autres)

def bas(event):
    global liste_regles, grille, liste_obstacles, liste_blocs, liste_regles, liste_liste_objets, images_blocs, images_obstacles, images_autres
    if checker_regles(liste_regles, images_autres):
        a = check_deplacement([0,1], liste_regles, liste_blocs, liste_obstacles, grille, liste_liste_objets)
        liste_regles, images_obstacles = nouvelles_regles(liste_blocs, images_obstacles)
        grille, images_blocs, images_obstacles = afficher_grille(liste_blocs, liste_obstacles, images_blocs, images_obstacles, liste_liste_objets, a)
    checker_regles(liste_regles, images_autres)

def revenir_temps(event):
    global liste_regles, liste_blocs, liste_obstacles, liste_liste_objets, grille, images_blocs, images_obstacles, images_autres
    grille, images_blocs, images_obstacles = afficher_grille_rewind(liste_blocs, liste_obstacles, images_blocs, images_obstacles, liste_liste_objets)
    liste_blocs, liste_obstacles = rewind(liste_liste_objets, liste_blocs, liste_obstacles)
    liste_regles, images_obstacles = nouvelles_regles(liste_blocs, images_obstacles)
    checker_regles(liste_regles, images_autres)

top.bind("<Left>", gauche)
top.bind("<Right>", droite)
top.bind("<Up>", haut)
top.bind("<Down>", bas)
top.bind("z", revenir_temps)

top.mainloop()