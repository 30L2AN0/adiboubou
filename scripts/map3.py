from __init__ import *

exec(open("__init__.py").read())

global liste_obstacles, liste_blocs, liste_regles, taille, grille, liste_liste_objets


# ANNE
liste_blocs.append(Bloc("noun", "ANNE", "anne", (10, 2)))
# GRASS
liste_blocs.append(Bloc("noun", "GRASS", "grass", (5, 4)))
liste_blocs.append(Bloc("noun", "GRASS", "grass", (5, 8)))
# GOOD CHAMPI
liste_blocs.append(Bloc("noun", "  GOOD\nCHAMPI", "good champi", (14, 10)))
# BAD CHAMPI
liste_blocs.append(Bloc("noun", "    BAD\nCHAMPI", "bad champi", (16, 2)))
# WALL
liste_blocs.append(Bloc("noun", "WALL", "wall", (25, 5)))



# IS
liste_blocs.append(Bloc("verb", "IS", "is", (10, 3)))
liste_blocs.append(Bloc("verb", "IS", "is", (5, 5)))
liste_blocs.append(Bloc("verb", "IS", "is", (25, 6)))
liste_blocs.append(Bloc("verb", "IS", "is", (16, 3)))
liste_blocs.append(Bloc("verb", "IS", "is", (6, 8)))
liste_blocs.append(Bloc("verb", "IS", "is", (15, 11)))


# YOU
liste_blocs.append(Bloc("adj", "YOU", "you", (10, 4)))
# PUSH
liste_blocs.append(Bloc("adj", "PUSH", "push", (5, 6)))
# STOP
liste_blocs.append(Bloc("adj", "STOP", "stop", (25, 7)))
# SHUT
liste_blocs.append(Bloc("adj", "SHUT", "shut", (16, 4)))
# OPEN
liste_blocs.append(Bloc("adj", "OPEN", "open", (7, 8)))
# WIN
liste_blocs.append(Bloc("adj", "WIN", "win", (15, 12)))

# Anne
liste_obstacles.append(Obstacle("anne", (13, 6)))

# Good champi
liste_obstacles.append(Obstacle("good champi", (23, 6)))

# Bad champi
liste_obstacles.append(Obstacle("bad champi", (20, 6)))

# Wall
liste_obstacles.append(Obstacle("wall", (21, 3)))
liste_obstacles.append(Obstacle("wall", (22, 3)))
liste_obstacles.append(Obstacle("wall", (23, 3)))
liste_obstacles.append(Obstacle("wall", (24, 3)))
liste_obstacles.append(Obstacle("wall", (25, 3)))
liste_obstacles.append(Obstacle("wall", (21, 3)))
liste_obstacles.append(Obstacle("wall", (20, 3)))
liste_obstacles.append(Obstacle("wall", (20, 4)))
liste_obstacles.append(Obstacle("wall", (20, 5)))
liste_obstacles.append(Obstacle("wall", (20, 7)))
liste_obstacles.append(Obstacle("wall", (20, 8)))
liste_obstacles.append(Obstacle("wall", (26, 9)))
liste_obstacles.append(Obstacle("wall", (20, 9)))
liste_obstacles.append(Obstacle("wall", (21, 9)))
liste_obstacles.append(Obstacle("wall", (22, 9)))
liste_obstacles.append(Obstacle("wall", (23, 9)))
liste_obstacles.append(Obstacle("wall", (24, 9)))
liste_obstacles.append(Obstacle("wall", (25, 9)))
liste_obstacles.append(Obstacle("wall", (26, 5)))
liste_obstacles.append(Obstacle("wall", (26, 6)))
liste_obstacles.append(Obstacle("wall", (26, 7)))
liste_obstacles.append(Obstacle("wall", (26, 8)))
liste_obstacles.append(Obstacle("wall", (26, 4)))
liste_obstacles.append(Obstacle("wall", (26, 3)))

# Wall
liste_obstacles.append(Obstacle("wall", (4, 3)))
liste_obstacles.append(Obstacle("wall", (4, 4)))
liste_obstacles.append(Obstacle("wall", (4, 5)))
liste_obstacles.append(Obstacle("wall", (4, 6)))
liste_obstacles.append(Obstacle("wall", (4, 7)))
liste_obstacles.append(Obstacle("wall", (4, 8)))
liste_obstacles.append(Obstacle("wall", (4, 9)))
liste_obstacles.append(Obstacle("wall", (5, 3)))
liste_obstacles.append(Obstacle("wall", (6, 3)))
liste_obstacles.append(Obstacle("wall", (5, 9)))
liste_obstacles.append(Obstacle("wall", (6, 9)))
liste_obstacles.append(Obstacle("wall", (7, 9)))
liste_obstacles.append(Obstacle("wall", (6, 7)))
liste_obstacles.append(Obstacle("wall", (7, 7)))
liste_obstacles.append(Obstacle("wall", (8, 7)))
liste_obstacles.append(Obstacle("wall", (8, 8)))
liste_obstacles.append(Obstacle("wall", (8, 9)))
liste_obstacles.append(Obstacle("wall", (7, 5)))


liste_obstacles.append(Obstacle("wall", (12, 8)))
liste_obstacles.append(Obstacle("wall", (12, 9)))
liste_obstacles.append(Obstacle("wall", (12, 10)))
liste_obstacles.append(Obstacle("wall", (12, 11)))
liste_obstacles.append(Obstacle("wall", (12, 12)))
liste_obstacles.append(Obstacle("wall", (12, 13)))
liste_obstacles.append(Obstacle("wall", (13, 13)))
liste_obstacles.append(Obstacle("wall", (13, 12)))
liste_obstacles.append(Obstacle("wall", (13, 11)))
liste_obstacles.append(Obstacle("wall", (14, 13)))
liste_obstacles.append(Obstacle("wall", (15, 13)))
liste_obstacles.append(Obstacle("wall", (16, 13)))
liste_obstacles.append(Obstacle("wall", (16, 12)))
liste_obstacles.append(Obstacle("wall", (16, 11)))
liste_obstacles.append(Obstacle("wall", (16, 10)))
liste_obstacles.append(Obstacle("wall", (16, 9)))
liste_obstacles.append(Obstacle("wall", (15, 9)))
liste_obstacles.append(Obstacle("wall", (14, 9)))



# Grass

liste_obstacles.append(Obstacle("grass", (13, 8)))

