from __init__ import *

exec(open("__init__.py").read())

global liste_obstacles, liste_blocs, liste_regles, taille, grille, liste_liste_objets


# ANNE
liste_blocs.append(Bloc("noun", "ANNE", "anne", (19, 12)))
# AURIANE
liste_blocs.append(Bloc("noun", "AURIANE", "auriane", (18, 8)))
# GOOD CHAMPI
liste_blocs.append(Bloc("noun", "  GOOD\nCHAMPI", "good champi", (7, 12)))
liste_blocs.append(Bloc("noun", "  GOOD\nCHAMPI", "good champi", (27, 0)))
# BAD CHAMPI
liste_blocs.append(Bloc("noun", "   BAD\nCHAMPI", "bad champi", (5, 7)))
# WALL
liste_blocs.append(Bloc("noun", "WALL", "wall", (13, 14)))
# GRASS
liste_blocs.append(Bloc("noun", "GRASS", "grass", (16, 4)))
# TEXT
liste_blocs.append(Bloc("noun", "TEXT", "text", (19, 7)))
# DOOR
liste_blocs.append(Bloc("noun", "DOOR", "door", (0, 0)))




# IS
liste_blocs.append(Bloc("verb", "IS", "is", (1, 0)))
liste_blocs.append(Bloc("verb", "IS", "is", (17, 4)))
liste_blocs.append(Bloc("verb", "IS", "is", (6, 7)))
liste_blocs.append(Bloc("verb", "IS", "is", (19, 8)))
liste_blocs.append(Bloc("verb", "IS", "is", (20, 12)))
liste_blocs.append(Bloc("verb", "IS", "is", (8, 13)))
liste_blocs.append(Bloc("verb", "IS", "is", (14, 14)))
liste_blocs.append(Bloc("verb", "IS", "is", (5, 8)))
liste_blocs.append(Bloc("verb", "IS", "is", (28, 0)))

# YOU
liste_blocs.append(Bloc("adj", "YOU", "you", (21, 12)))
# PUSH
liste_blocs.append(Bloc("adj", "PUSH", "push", (19, 9)))
liste_blocs.append(Bloc("adj", "PUSH", "push", (29, 0)))
# STOP
liste_blocs.append(Bloc("adj", "STOP", "stop", (15, 14)))
# SHUT
liste_blocs.append(Bloc("adj", "SHUT", "shut", (2, 0)))
# HOT
liste_blocs.append(Bloc("adj", "HOT", "hot", (20, 8)))
# DEATH
liste_blocs.append(Bloc("adj", "DEFEAT", "death", (18, 4)))
liste_blocs.append(Bloc("adj", "DEFEAT", "death", (7, 7)))
# MELT
liste_blocs.append(Bloc("adj", "MELT", "melt", (5, 9)))
# WEAK
liste_blocs.append(Bloc("adj", "WEAK", "weak", (14, 11)))
# BLUE
liste_blocs.append(Bloc("adj", "BLUE", "blue", (22, 10)))
# GREENER
liste_blocs.append(Bloc("adj", "GREENER", "greener", (26, 4)))
# OPEN
liste_blocs.append(Bloc("adj", "OPEN", "open", (9, 13)))






# Anne
liste_obstacles.append(Obstacle("anne", (16, 9)))

# Auriane
liste_obstacles.append(Obstacle("auriane", (9, 10)))

# Good champi
liste_obstacles.append(Obstacle("good champi", (9, 4)))

# Bad champi
liste_obstacles.append(Obstacle("bad champi", (12, 7)))

# Wall
liste_obstacles.append(Obstacle("wall", (7, 2)))
liste_obstacles.append(Obstacle("wall", (8, 2)))
liste_obstacles.append(Obstacle("wall", (10, 2)))
liste_obstacles.append(Obstacle("wall", (11, 2)))
liste_obstacles.append(Obstacle("wall", (6, 3)))
liste_obstacles.append(Obstacle("wall", (7, 3)))
liste_obstacles.append(Obstacle("wall", (11, 3)))
liste_obstacles.append(Obstacle("wall", (12, 3)))
liste_obstacles.append(Obstacle("wall", (15, 3)))
liste_obstacles.append(Obstacle("wall", (16, 3)))
liste_obstacles.append(Obstacle("wall", (17, 3)))
liste_obstacles.append(Obstacle("wall", (18, 3)))
liste_obstacles.append(Obstacle("wall", (19, 3)))
liste_obstacles.append(Obstacle("wall", (20, 3)))
liste_obstacles.append(Obstacle("wall", (6, 4)))
liste_obstacles.append(Obstacle("wall", (12, 4)))
liste_obstacles.append(Obstacle("wall", (13, 4)))
liste_obstacles.append(Obstacle("wall", (14, 4)))
liste_obstacles.append(Obstacle("wall", (15, 4)))
liste_obstacles.append(Obstacle("wall", (20, 4)))
liste_obstacles.append(Obstacle("wall", (21, 4)))
liste_obstacles.append(Obstacle("wall", (22, 4)))
liste_obstacles.append(Obstacle("wall", (6, 5)))
liste_obstacles.append(Obstacle("wall", (7, 5)))
liste_obstacles.append(Obstacle("wall", (13, 5)))
liste_obstacles.append(Obstacle("wall", (14, 5)))
liste_obstacles.append(Obstacle("wall", (22, 5)))
liste_obstacles.append(Obstacle("wall", (23, 5)))
liste_obstacles.append(Obstacle("wall", (7, 6)))
liste_obstacles.append(Obstacle("wall", (8, 6)))
liste_obstacles.append(Obstacle("wall", (9, 6)))
liste_obstacles.append(Obstacle("wall", (13, 6)))
liste_obstacles.append(Obstacle("wall", (22, 6)))
liste_obstacles.append(Obstacle("wall", (23, 6)))
liste_obstacles.append(Obstacle("wall", (9, 7)))
liste_obstacles.append(Obstacle("wall", (23, 7)))
liste_obstacles.append(Obstacle("wall", (7, 8)))
liste_obstacles.append(Obstacle("wall", (8, 8)))
liste_obstacles.append(Obstacle("wall", (9, 8)))
liste_obstacles.append(Obstacle("wall", (10, 8)))
liste_obstacles.append(Obstacle("wall", (12, 8)))
liste_obstacles.append(Obstacle("wall", (24, 8)))
liste_obstacles.append(Obstacle("wall", (6, 9)))
liste_obstacles.append(Obstacle("wall", (7, 9)))
liste_obstacles.append(Obstacle("wall", (10, 9)))
liste_obstacles.append(Obstacle("wall", (11, 9)))
liste_obstacles.append(Obstacle("wall", (12, 9)))
liste_obstacles.append(Obstacle("wall", (24, 9)))
liste_obstacles.append(Obstacle("wall", (5, 10)))
liste_obstacles.append(Obstacle("wall", (6, 10)))
liste_obstacles.append(Obstacle("wall", (12, 10)))
liste_obstacles.append(Obstacle("wall", (24, 10)))
liste_obstacles.append(Obstacle("wall", (5, 11)))
liste_obstacles.append(Obstacle("wall", (12, 11)))
liste_obstacles.append(Obstacle("wall", (13, 11)))
liste_obstacles.append(Obstacle("wall", (24, 11)))
liste_obstacles.append(Obstacle("wall", (5, 12)))
liste_obstacles.append(Obstacle("wall", (6, 12)))
liste_obstacles.append(Obstacle("wall", (11, 12)))
liste_obstacles.append(Obstacle("wall", (12, 12)))
liste_obstacles.append(Obstacle("wall", (13, 12)))
liste_obstacles.append(Obstacle("wall", (14, 12)))
liste_obstacles.append(Obstacle("wall", (22, 12)))
liste_obstacles.append(Obstacle("wall", (23, 12)))
liste_obstacles.append(Obstacle("wall", (24, 12)))
liste_obstacles.append(Obstacle("wall", (6, 13)))
liste_obstacles.append(Obstacle("wall", (10, 13)))
liste_obstacles.append(Obstacle("wall", (11, 13)))
liste_obstacles.append(Obstacle("wall", (14, 13)))
liste_obstacles.append(Obstacle("wall", (15, 13)))
liste_obstacles.append(Obstacle("wall", (16, 13)))
liste_obstacles.append(Obstacle("wall", (17, 13)))
liste_obstacles.append(Obstacle("wall", (19, 13)))
liste_obstacles.append(Obstacle("wall", (20, 13)))
liste_obstacles.append(Obstacle("wall", (21, 13)))
liste_obstacles.append(Obstacle("wall", (22, 13)))
liste_obstacles.append(Obstacle("wall", (6, 14)))
liste_obstacles.append(Obstacle("wall", (7, 14)))
liste_obstacles.append(Obstacle("wall", (8, 14)))
liste_obstacles.append(Obstacle("wall", (9, 14)))
liste_obstacles.append(Obstacle("wall", (10, 14)))
liste_obstacles.append(Obstacle("wall", (17, 14)))
liste_obstacles.append(Obstacle("wall", (18, 14)))
liste_obstacles.append(Obstacle("wall", (19, 14)))


# Grass
liste_obstacles.append(Obstacle("grass", (13, 7)))
liste_obstacles.append(Obstacle("grass", (7, 11)))

# Door
liste_obstacles.append(Obstacle("door", (9, 2)))