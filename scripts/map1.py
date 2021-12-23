from __init__ import *
exec(open("__init__.py").read())

global liste_obstacles, liste_blocs, liste_regles, taille, grille, liste_liste_objets

liste_blocs.append(Bloc("adj", "stop", (25,7)))
liste_blocs.append(Bloc("noun", "anne", (5,4)))
liste_blocs.append(Bloc("adj", "you", (7,4)))
liste_blocs.append(Bloc("verb", "is", (6,4)))
liste_blocs.append(Bloc("noun", "wall", (0,0)))
liste_blocs.append(Bloc("verb", "is", (0,1)))
liste_blocs.append(Bloc("adj", "stop", (0,2)))
liste_blocs.append(Bloc("noun", "good champi", (4,8)))
liste_blocs.append(Bloc("verb", "is", (4,9)))
liste_blocs.append(Bloc("adj", "push", (4,10)))
liste_blocs.append(Bloc("noun", "grass", (13,6)))
liste_blocs.append(Bloc("verb", "is", (14,7)))
liste_blocs.append(Bloc("adj", "greener", (15,8)))
liste_blocs.append(Bloc("noun", "bad champi", (7,10)))
liste_blocs.append(Bloc("verb", "is", (7,11)))
liste_blocs.append(Bloc("adj", "shut", (7,12)))


liste_blocs.append(Bloc("noun", "good champi", (17,5)))
liste_blocs.append(Bloc("verb", "is", (17,6)))
liste_blocs.append(Bloc("adj", "open", (17,7)))

#obstacles
liste_obstacles.append(Obstacle("good champi", (7, 6)))
liste_obstacles.append(Obstacle("bad champi", (9, 6)))
liste_obstacles.append(Obstacle("anne", (11,2)))
liste_obstacles.append(Obstacle("grass", (0,3)))
liste_obstacles.append(Obstacle("grass", (1,0)))
liste_obstacles.append(Obstacle("grass", (1,1)))
liste_obstacles.append(Obstacle("grass", (1,2)))
liste_obstacles.append(Obstacle("grass", (1,3)))


for j in range(hauteur//taille):
    for i in range(22-j//2, 25-j//2):
        liste_obstacles.append(Obstacle("grass", (i,j)))

liste_obstacles.append(Obstacle("wall", (13,0)))
liste_obstacles.append(Obstacle("wall", (13,1)))
liste_obstacles.append(Obstacle("wall", (13,2)))
liste_obstacles.append(Obstacle("wall", (13,3)))
liste_obstacles.append(Obstacle("wall", (13,4)))
liste_obstacles.append(Obstacle("wall", (12,4)))
liste_obstacles.append(Obstacle("wall", (11,4)))
liste_obstacles.append(Obstacle("wall", (10,4)))
liste_obstacles.append(Obstacle("wall", (9,4)))
liste_obstacles.append(Obstacle("wall", (9,3)))
liste_obstacles.append(Obstacle("wall", (9,5)))
liste_obstacles.append(Obstacle("wall", (8,5)))
liste_obstacles.append(Obstacle("wall", (9,1)))
liste_obstacles.append(Obstacle("wall", (9,0)))
liste_obstacles.append(Obstacle("wall", (10,0)))
liste_obstacles.append(Obstacle("wall", (11,0)))
liste_obstacles.append(Obstacle("wall", (12,0)))
liste_obstacles.append(Obstacle("wall", (4,5)))
liste_obstacles.append(Obstacle("wall", (3,5)))
liste_obstacles.append(Obstacle("wall", (3,4)))
liste_obstacles.append(Obstacle("wall", (3,3)))
liste_obstacles.append(Obstacle("wall", (3,2)))
liste_obstacles.append(Obstacle("wall", (3,1)))
liste_obstacles.append(Obstacle("wall", (3,0)))
liste_obstacles.append(Obstacle("wall", (3,6)))
liste_obstacles.append(Obstacle("wall", (3,7)))
liste_obstacles.append(Obstacle("wall", (3,8)))
liste_obstacles.append(Obstacle("wall", (4,7)))
liste_obstacles.append(Obstacle("wall", (5,7)))
liste_obstacles.append(Obstacle("wall", (6,7)))
liste_obstacles.append(Obstacle("wall", (7,7)))
liste_obstacles.append(Obstacle("wall", (8,7)))

liste_obstacles.append(Obstacle("wall", (9,7)))
liste_obstacles.append(Obstacle("wall", (5,8)))
liste_obstacles.append(Obstacle("wall", (8,0)))
liste_obstacles.append(Obstacle("wall", (7,0)))
liste_obstacles.append(Obstacle("wall", (6,0)))
liste_obstacles.append(Obstacle("wall", (5,0)))
liste_obstacles.append(Obstacle("wall", (4,0)))
