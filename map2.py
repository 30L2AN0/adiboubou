from __init__ import *

exec(open("__init__.py").read())

global liste_obstacles, liste_blocs, liste_regles, taille, grille, liste_liste_objets


# ANNE
liste_blocs.append(Bloc("noun", "ANNE", "anne", (17, 12)))
# AURIANE
liste_blocs.append(Bloc("noun", "AURIANE", "auriane", (16, 8)))
# GOOD CHAMPI
liste_blocs.append(Bloc("noun", "GOOD\nCHAMPI", "good champi", (5, 12)))
# BAD CHAMPI
liste_blocs.append(Bloc("noun", "BAD\nCHAMPI", "bad champi", (2, 7)))
# WALL
liste_blocs.append(Bloc("noun", "WALL", "wall", (11, 14)))
# GRASS
liste_blocs.append(Bloc("noun", "GRASS", "grass", (14, 4)))
# DOOR
liste_blocs.append(Bloc("noun", "DOOR", "door", (0, 1)))
# TEXT
liste_blocs.append(Bloc("noun", "TEXT", "text", (0, 0)))
liste_blocs.append(Bloc("noun", "TEXT", "text", (17, 7)))




# IS
liste_blocs.append(Bloc("verb", "IS", "is", (1, 0)))
liste_blocs.append(Bloc("verb", "IS", "is", (1, 1)))
liste_blocs.append(Bloc("verb", "IS", "is", (15, 4)))
liste_blocs.append(Bloc("verb", "IS", "is", (3, 7)))
liste_blocs.append(Bloc("verb", "IS", "is", (17, 8)))
liste_blocs.append(Bloc("verb", "IS", "is", (18, 12)))
liste_blocs.append(Bloc("verb", "IS", "is", (6, 13)))
liste_blocs.append(Bloc("verb", "IS", "is", (12, 14)))
# AND
#A REGLER
liste_blocs.append(Bloc("and", "AND", "and", (5, 7)))


# YOU
liste_blocs.append(Bloc("adj", "YOU", "you", (19, 12)))
# PUSH
liste_blocs.append(Bloc("adj", "PUSH", "push", (18, 8)))
liste_blocs.append(Bloc("adj", "STOP", "stop", (13, 14)))
#HOT
liste_blocs.append(Bloc("adj", "HOT", "hot", (17, 9)))
#DEATH
liste_blocs.append(Bloc("adj", "DEATH", "death", (2, 0)))
liste_blocs.append(Bloc("adj", "DEATH", "death", (16, 4)))
liste_blocs.append(Bloc("adj", "DEATH", "death", (4, 7)))
# MELT
liste_blocs.append(Bloc("adj", "MELT", "melt", (6, 7)))
#WEAK
liste_blocs.append(Bloc("adj", "WEAK", "weak", (12, 11)))
# OPEN
liste_blocs.append(Bloc("adj", "OPEN", "open", (7, 13)))
# SHUT
liste_blocs.append(Bloc("adj", "SHUT", "shut", (2, 1)))
# MELT
liste_blocs.append(Bloc("adj", "MELT", "melt", (6, 7)))
# BLUE
liste_blocs.append(Bloc("adj", "BLUE", "blue", (20, 10)))
# GREENER
liste_blocs.append(Bloc("adj", "GREENER", "greener", (22, 2)))







# Anne
liste_obstacles.append(Obstacle("anne", (14, 9)))

# Auriane
liste_obstacles.append(Obstacle("auriane", (7, 10)))

# Good champi
liste_obstacles.append(Obstacle("good champi", (14, 11)))

# Bad champi
liste_obstacles.append(Obstacle("bad champi", (14, 10)))

# Wall
liste_obstacles.append(Obstacle("wall", (5, 2)))
liste_obstacles.append(Obstacle("wall", (6, 2)))
liste_obstacles.append(Obstacle("wall", (8, 2)))
liste_obstacles.append(Obstacle("wall", (9, 2)))
liste_obstacles.append(Obstacle("wall", (4, 3)))
liste_obstacles.append(Obstacle("wall", (5, 3)))
liste_obstacles.append(Obstacle("wall", (9, 3)))
liste_obstacles.append(Obstacle("wall", (10, 3)))
liste_obstacles.append(Obstacle("wall", (13, 3)))
liste_obstacles.append(Obstacle("wall", (14, 3)))
liste_obstacles.append(Obstacle("wall", (15, 3)))
liste_obstacles.append(Obstacle("wall", (16, 3)))
liste_obstacles.append(Obstacle("wall", (17, 3)))
liste_obstacles.append(Obstacle("wall", (18, 3)))
liste_obstacles.append(Obstacle("wall", (4, 4)))
liste_obstacles.append(Obstacle("wall", (10, 4)))
liste_obstacles.append(Obstacle("wall", (11, 4)))
liste_obstacles.append(Obstacle("wall", (12, 4)))
liste_obstacles.append(Obstacle("wall", (13, 4)))
liste_obstacles.append(Obstacle("wall", (18, 4)))
liste_obstacles.append(Obstacle("wall", (19, 4)))
liste_obstacles.append(Obstacle("wall", (20, 4)))
liste_obstacles.append(Obstacle("wall", (4, 5)))
liste_obstacles.append(Obstacle("wall", (5, 5)))
liste_obstacles.append(Obstacle("wall", (11, 5)))
liste_obstacles.append(Obstacle("wall", (12, 5)))
liste_obstacles.append(Obstacle("wall", (20, 5)))
liste_obstacles.append(Obstacle("wall", (21, 5)))
liste_obstacles.append(Obstacle("wall", (5, 6)))
liste_obstacles.append(Obstacle("wall", (6, 6)))
liste_obstacles.append(Obstacle("wall", (7, 6)))
liste_obstacles.append(Obstacle("wall", (11, 6)))
liste_obstacles.append(Obstacle("wall", (14, 6)))
liste_obstacles.append(Obstacle("wall", (21, 6)))
liste_obstacles.append(Obstacle("wall", (22, 6)))
liste_obstacles.append(Obstacle("wall", (7, 7)))
liste_obstacles.append(Obstacle("wall", (22, 7)))
liste_obstacles.append(Obstacle("wall", (5, 8)))
liste_obstacles.append(Obstacle("wall", (6, 8)))
liste_obstacles.append(Obstacle("wall", (7, 8)))
liste_obstacles.append(Obstacle("wall", (8, 8)))
liste_obstacles.append(Obstacle("wall", (10, 8)))
liste_obstacles.append(Obstacle("wall", (22, 8)))
liste_obstacles.append(Obstacle("wall", (4, 9)))
liste_obstacles.append(Obstacle("wall", (5, 9)))
liste_obstacles.append(Obstacle("wall", (8, 9)))
liste_obstacles.append(Obstacle("wall", (9, 9)))
liste_obstacles.append(Obstacle("wall", (10, 9)))
liste_obstacles.append(Obstacle("wall", (22, 9)))
liste_obstacles.append(Obstacle("wall", (3, 10)))
liste_obstacles.append(Obstacle("wall", (4, 10)))
liste_obstacles.append(Obstacle("wall", (10, 10)))
liste_obstacles.append(Obstacle("wall", (11, 10)))
liste_obstacles.append(Obstacle("wall", (22, 10)))
liste_obstacles.append(Obstacle("wall", (3, 11)))
liste_obstacles.append(Obstacle("wall", (10, 11)))
liste_obstacles.append(Obstacle("wall", (11, 11)))
liste_obstacles.append(Obstacle("wall", (22, 11)))
liste_obstacles.append(Obstacle("wall", (3, 12)))
liste_obstacles.append(Obstacle("wall", (4, 12)))
liste_obstacles.append(Obstacle("wall", (9, 12)))
liste_obstacles.append(Obstacle("wall", (10, 12)))
liste_obstacles.append(Obstacle("wall", (11, 12)))
liste_obstacles.append(Obstacle("wall", (12, 12)))
liste_obstacles.append(Obstacle("wall", (20, 12)))
liste_obstacles.append(Obstacle("wall", (21, 12)))
liste_obstacles.append(Obstacle("wall", (22, 12)))
liste_obstacles.append(Obstacle("wall", (4, 13)))
liste_obstacles.append(Obstacle("wall", (8, 13)))
liste_obstacles.append(Obstacle("wall", (9, 13)))
liste_obstacles.append(Obstacle("wall", (12, 13)))
liste_obstacles.append(Obstacle("wall", (13, 13)))
liste_obstacles.append(Obstacle("wall", (14, 13)))
liste_obstacles.append(Obstacle("wall", (15, 13)))
liste_obstacles.append(Obstacle("wall", (17, 13)))
liste_obstacles.append(Obstacle("wall", (18, 13)))
liste_obstacles.append(Obstacle("wall", (19, 13)))
liste_obstacles.append(Obstacle("wall", (20, 13)))
liste_obstacles.append(Obstacle("wall", (4, 14)))
liste_obstacles.append(Obstacle("wall", (5, 14)))
liste_obstacles.append(Obstacle("wall", (6, 14)))
liste_obstacles.append(Obstacle("wall", (7, 14)))
liste_obstacles.append(Obstacle("wall", (8, 14)))
liste_obstacles.append(Obstacle("wall", (15, 14)))
liste_obstacles.append(Obstacle("wall", (16, 14)))
liste_obstacles.append(Obstacle("wall", (17, 14)))

# Grass

liste_obstacles.append(Obstacle("grass", (11, 7)))
liste_obstacles.append(Obstacle("grass", (5, 11)))


#blocs de test
liste_blocs.append(Bloc("verb", "IS", "is", (12, 0)))
liste_blocs.append(Bloc("noun", "ANNE", "anne", (11, 0)))
liste_blocs.append(Bloc("adj", "BLUE", "blue", (13, 0)))