from tkinter import *
import sys
from PIL import ImageTk
from PIL import Image

top = Tk()
C = Canvas(top,height = 1024, width = 2048, background = "#ff7e4c")

C.pack()
top.title("Anne is stone")

class Bloc:
    def __init__(self, adj, nom, verbe, mot, obstacle, position):
        self.adjectif = adj
        self.nom = nom
        self.verbe = verbe
        self.mot = mot
        self.obstacle = obstacle
        self.position = position

class Obstacle:
    def __init__(self, badchampi, goodchampi, anne, grass, wall, mot, position):
        self.badchampi = badchampi
        self.goodchampi = goodchampi
        self.anne = anne
        self.grass = grass
        self.wall = wall
        self.mot = mot
        self.position = position

#Création des blocs, obstacles

global path
global anne_position
global liste_obstacles
global liste_blocs
global liste_regles
global taille
global grille

taille = 60

grille = [[None for j in range(1024//taille)] for i in range(2048//taille)]

path = "clipped/"

image_anne = ImageTk.PhotoImage(Image.open(path+"anne.png").resize((taille,taille), Image.ANTIALIAS))
image_auriane = ImageTk.PhotoImage(Image.open(path+"auriane.png").resize((taille,taille), Image.ANTIALIAS))
image_good_champi = ImageTk.PhotoImage(Image.open(path+"good_champi.png").resize((taille,taille), Image.ANTIALIAS))
image_bad_champi = ImageTk.PhotoImage(Image.open(path+"bad_champi.png").resize((taille,taille), Image.ANTIALIAS))
image_wall = ImageTk.PhotoImage(Image.open(path+"wall.png").resize((taille,taille), Image.ANTIALIAS))
image_grass = ImageTk.PhotoImage(Image.open(path+"grass.png").resize((taille,taille), Image.ANTIALIAS))
image_door = ImageTk.PhotoImage(Image.open(path+"door.png").resize((taille,taille), Image.ANTIALIAS))

liste_blocs = []
liste_obstacles = []
liste_regles = []


# First map

"""
#blocs

#bloc = Bloc(False, False, True, "IS", "is", (2,2))
#liste_blocs.append(bloc)
#bloc = Bloc(False, False, True, "IS", "is", (3,1))
#liste_blocs.append(bloc)
bloc = Bloc(True, False, False, "STOP", "stop", (25,7))
liste_blocs.append(bloc)
#bloc = Bloc(False, True, False, "    BAD\nCHAMPIS", "badchampi", (2,1))
#liste_blocs.append(bloc)
#bloc = Bloc(False, True, False, "   GOOD\nCHAMPIS", "goodchampi", (2,3))
#liste_blocs.append(bloc)

liste_blocs.append(Bloc(False, True, False, "ANNE", "anne", (5,4)))
liste_blocs.append(Bloc(False, True, False, "YOU", "you", (7,4)))
liste_blocs.append(Bloc(False, False, True, "IS", "is", (6,4)))
liste_blocs.append(Bloc(False, True, False, "WALL", "wall", (0,0)))
liste_blocs.append(Bloc(False, False, True, "IS", "is", (0,1)))
liste_blocs.append(Bloc(False, True, False, "STOP", "stop", (0,2)))
liste_blocs.append(Bloc(False, True, False, "   BAD\nCHAMPI", "stop", (4,8)))
liste_blocs.append(Bloc(False, False, True, "IS", "is", (4,9)))
liste_blocs.append(Bloc(True, False, False, "PUSH", "push", (4,10)))



#obstacles
liste_obstacles.append(Obstacle(False, False, True, False, False, "anne", (11,2)))
liste_obstacles.append(Obstacle(False, False, False, True, False, "grass", (0,3)))
liste_obstacles.append(Obstacle(False, False, False, True, False, "grass", (1,0)))
liste_obstacles.append(Obstacle(False, False, False, True, False, "grass", (1,1)))
liste_obstacles.append(Obstacle(False, False, False, True, False, "grass", (1,2)))
liste_obstacles.append(Obstacle(False, False, False, True, False, "grass", (1,3)))


for j in range(15):
    for i in range(22-j//2, 25-j//2):
        liste_obstacles.append(Obstacle(False, False, False, True, False, "grass", (i,j)))

liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (13,0)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (13,1)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (13,2)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (13,3)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (13,4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (12,4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (11,4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (10,4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (9,4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (9,3)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (9,5)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (8,5)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (9,1)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (9,0)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (10,0)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (11,0)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (12,0)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (4,5)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (3,5)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (3,4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (3,3)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (3,2)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (3,1)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (3,0)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (3,6)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (3,7)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (3,8)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (4,7)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (5,7)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (6,7)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (7,7)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (8,7)))

liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (9,7)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (10,7)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (5,8)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (8,0)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (7,0)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (6,0)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (5,0)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (4,0)))
"""

##### Second map #####


### Blocs


## Nouns

# ANNE
liste_blocs.append(Bloc(False, True, False, "ANNE", "anne", (17, 12)))
# AURIANE
liste_blocs.append(Bloc(False, True, False, "AURIANE", "auriane", (16, 8)))
# GOOD CHAMPI
liste_blocs.append(Bloc(False, True, False, "GOOD\nCHAMPI", "good champi", (5, 12)))
# BAD CHAMPI
liste_blocs.append(Bloc(False, True, False, "BAD\nCHAMPI", "bad champi", (2, 7)))
# WALL                                         
liste_blocs.append(Bloc(False, True, False, "WALL", "wall", (11, 14)))
# GRASS                                        
liste_blocs.append(Bloc(False, True, False, "GRASS", "grass", (14, 4)))
# DOOR
liste_blocs.append(Bloc(False, True, False, "DOOR", "door", (0, 1)))
# TEXT                                         
liste_blocs.append(Bloc(False, True, False, "TEXT", "text", (0, 0)))
liste_blocs.append(Bloc(False, True, False, "TEXT", "text", (17, 7)))
                                               
                                               
## Verbs                                       
                                               
# IS                                           
liste_blocs.append(Bloc(False, False, True, "IS", "is", (1, 0)))
liste_blocs.append(Bloc(False, False, True, "IS", "is", (1, 1)))
liste_blocs.append(Bloc(False, False, True, "IS", "is", (15, 4)))
liste_blocs.append(Bloc(False, False, True, "IS", "is", (3, 7)))
liste_blocs.append(Bloc(False, False, True, "IS", "is", (17, 8)))
liste_blocs.append(Bloc(False, False, True, "IS", "is", (18, 12)))
liste_blocs.append(Bloc(False, False, True, "IS", "is", (6, 13)))
liste_blocs.append(Bloc(False, False, True, "IS", "is", (12, 14)))
# AND
liste_blocs.append(Bloc(False, False, True, "AND", "and", (5, 7)))


## Adjectives

# YOU
liste_blocs.append(Bloc(True, False, False, "YOU", "you", (19, 12)))
# PUSH                                         
liste_blocs.append(Bloc(True, False, False, "PUSH", "push", (18, 8)))
liste_blocs.append(Bloc(True, False, False, "STOP", "stop", (13, 14)))
#HOT
liste_blocs.append(Bloc(True, False, False, "HOT", "hot", (17, 9)))
#DEATH
liste_blocs.append(Bloc(True, False, False, "DEATH", "death", (2, 0)))
liste_blocs.append(Bloc(True, False, False, "DEATH", "death", (16, 4)))
liste_blocs.append(Bloc(True, False, False, "DEATH", "death", (4, 7)))
# MELT
liste_blocs.append(Bloc(True, False, False, "MELT", "melt", (6, 7)))
#WEAK
liste_blocs.append(Bloc(True, False, False, "WEAK", "weak", (12, 11)))
# OPEN
liste_blocs.append(Bloc(True, False, False, "OPEN", "open", (7, 13)))
# CLOSE
liste_blocs.append(Bloc(True, False, False, "CLOSE", "close", (2, 1)))
# MELT
liste_blocs.append(Bloc(True, False, False, "MELT", "melt", (6, 7)))
# BLUE
liste_blocs.append(Bloc(True, False, False, "BLUE", "blue", (20, 10)))
# GREENER
liste_blocs.append(Bloc(True, False, False, "GREENER", "greener", (22, 2)))




### Obstacles


# Anne
liste_obstacles.append(Obstacle(False, False, True, False, False, "anne", (14, 9)))

# Auriane
#liste_obstacles.append(Obstacle(False, False, False, True, False, False, "auriane", (7, 10)))

# Good champi
liste_obstacles.append(Obstacle(False, True, False, False, False, "good champi", (14, 9))) # marche pô

# Bad champi
liste_obstacles.append(Obstacle(True, False, False, False, False, "bad champi", (14, 9))) # marche pô

# Wall
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (5, 2)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (6, 2)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (8, 2)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (9, 2)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (4, 3)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (5, 3)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (9, 3)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (10, 3)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (13, 3)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (14, 3)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (15, 3)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (16, 3)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (17, 3)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (18, 3)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (4, 4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (10, 4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (11, 4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (12, 4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (13, 4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (18, 4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (19, 4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (20, 4)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (4, 5)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (5, 5)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (11, 5)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (12, 5)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (20, 5)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (21, 5)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (5, 6)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (6, 6)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (7, 6)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (11, 6)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (14, 6)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (21, 6)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (22, 6)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (7, 7)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (22, 7)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (5, 8)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (6, 8)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (7, 8)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (8, 8)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (10, 8)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (22, 8)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (4, 9)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (5, 9)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (8, 9)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (9, 9)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (10, 9)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (22, 9)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (3, 10)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (4, 10)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (10, 10)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (11, 10)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (22, 10)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (3, 11)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (10, 11)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (11, 11)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (22, 11)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (3, 12)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (4, 12)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (9, 12)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (10, 12)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (11, 12)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (12, 12)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (20, 12)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (21, 12)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (22, 12)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (4, 13)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (8, 13)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (9, 13)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (12, 13)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (13, 13)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (14, 13)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (15, 13)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (17, 13)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (18, 13)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (19, 13)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (20, 13)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (4, 14)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (5, 14)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (6, 14)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (7, 14)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (8, 14)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (15, 14)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (16, 14)))
liste_obstacles.append(Obstacle(False, False, False, False, True, "wall", (17, 14)))

# Grass

liste_obstacles.append(Obstacle(False, False, False, True, False, "wall", (11, 7)))
liste_obstacles.append(Obstacle(False, False, False, True, False, "wall", (5, 11)))






for i in range(len(liste_blocs)):
    grille[liste_blocs[i].position[0]][liste_blocs[i].position[1]] = ("bloc", i)
for j in range(len(liste_obstacles)):
    grille[liste_obstacles[j].position[0]][liste_obstacles[j].position[1]] = ("obstacle", j)
print(grille)
def afficher_grille():
    C.delete("all")
    for blocs in liste_blocs:
        C.create_rectangle(blocs.position[0]*taille, blocs.position[1]*taille, (blocs.position[0]+1)*taille, (blocs.position[1]+1) *taille, fill = "", outline = "")
        C.create_text(blocs.position[0]*taille+taille//2, blocs.position[1]*taille+taille//2, text = blocs.mot, font = ("Arial",8))
    for obstacles in liste_obstacles:
        if obstacles.anne:
            C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_anne)
        if obstacles.grass:
            C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_grass)
        if obstacles.wall:
            C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_wall)

def distance(X,Y):
    return abs(X[0]-Y[0])+2*abs(X[1]-Y[1])

def nouvelles_regles():
    liste_regles = []
    n = len(liste_blocs)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                p1 = liste_blocs[i].position
                p2 = liste_blocs[j].position
                p3 = liste_blocs[k].position
                liste_distances = [distance(p1,p2), distance(p1,p3), distance(p2,p3)]
                if liste_distances == [2,2,4] and p2[1] < p3[1]:
                    if liste_blocs[j].nom and liste_blocs[i].verbe and (not liste_blocs[k].verbe):
                        liste_regles.append(liste_blocs[j].obstacle+" "+liste_blocs[i].obstacle+" "+liste_blocs[k].obstacle)
                if liste_distances == [2,4,2] and p1[1] < p3[1]:
                    if liste_blocs[i].nom and liste_blocs[j].verbe and (not liste_blocs[k].verbe):
                        liste_regles.append(liste_blocs[i].obstacle+" "+liste_blocs[j].obstacle+" "+liste_blocs[k].obstacle)
                if liste_distances == [4,2,2] and p1[1] < p2[1]:
                    if liste_blocs[i].nom and liste_blocs[k].verbe and (not liste_blocs[j].verbe):
                        liste_regles.append(liste_blocs[i].obstacle+" "+liste_blocs[k].obstacle+" "+liste_blocs[j].obstacle)
                if liste_distances == [2,2,4] and p2[1] > p3[1]:
                    if liste_blocs[k].nom and liste_blocs[i].verbe and (not liste_blocs[j].verbe):
                        liste_regles.append(liste_blocs[k].obstacle+" "+liste_blocs[i].obstacle+" "+liste_blocs[j].obstacle)
                if liste_distances == [2,4,2] and p1[1] > p3[1]:
                    if liste_blocs[k].nom and liste_blocs[j].verbe and (not liste_blocs[i].verbe):
                        liste_regles.append(liste_blocs[k].obstacle+" "+liste_blocs[j].obstacle+" "+liste_blocs[i].obstacle)
                if liste_distances == [4,2,2] and p1[1] > p2[1]:
                    if liste_blocs[j].nom and liste_blocs[k].verbe and (not liste_blocs[i].verbe):
                        liste_regles.append(liste_blocs[j].obstacle+" "+liste_blocs[k].obstacle+" "+liste_blocs[i].obstacle)

                if liste_distances == [1,1,2] and p2[0] < p3[0]:
                    if liste_blocs[j].nom and liste_blocs[i].verbe and (not liste_blocs[k].verbe):
                        liste_regles.append(liste_blocs[j].obstacle+" "+liste_blocs[i].obstacle+" "+liste_blocs[k].obstacle)
                if liste_distances == [1,2,1] and p1[0] < p3[0]:
                    if liste_blocs[i].nom and liste_blocs[j].verbe and (not liste_blocs[k].verbe):
                        liste_regles.append(liste_blocs[i].obstacle+" "+liste_blocs[j].obstacle+" "+liste_blocs[k].obstacle)
                if liste_distances == [2,1,1] and p1[0] < p2[0]:
                    if liste_blocs[i].nom and liste_blocs[k].verbe and (not liste_blocs[j].verbe):
                        liste_regles.append(liste_blocs[i].obstacle+" "+liste_blocs[k].obstacle+" "+liste_blocs[j].obstacle)
                if liste_distances == [1,1,2] and p2[0] > p3[0]:
                    if liste_blocs[k].nom and liste_blocs[i].verbe and (not liste_blocs[j].verbe):
                        liste_regles.append(liste_blocs[k].obstacle+" "+liste_blocs[i].obstacle+" "+liste_blocs[j].obstacle)
                if liste_distances == [1,2,1] and p1[0] > p3[0]:
                    if liste_blocs[k].nom and liste_blocs[j].verbe and (not liste_blocs[i].verbe):
                        liste_regles.append(liste_blocs[k].obstacle+" "+liste_blocs[j].obstacle+" "+liste_blocs[i].obstacle)
                if liste_distances == [2,1,1] and p1[0] > p2[0]:
                    if liste_blocs[j].nom and liste_blocs[k].verbe and (not liste_blocs[i].verbe):
                        liste_regles.append(liste_blocs[j].obstacle+" "+liste_blocs[k].obstacle+" "+liste_blocs[i].obstacle)
    #print(liste_regles)

def check_deplacement(t):
    for obstacle in liste_obstacles:
        if obstacle.mot == "anne":
            if grille[obstacle.position[0]+t[0]][obstacle.position[1]+t[1]] == None:
                obstacle.position = (obstacle.position[0]+t[0],obstacle.position[1]+t[1])
            else :
                grille[obstacle.position[0]+t[0]][obstacle.position[1]+t[1]] = (type, nombre)

def gauche(event):
    check_deplacement([-1,0])
    #global grille
    #grille = decale_gauche(addition_gauche(decale_gauche(grille)))
    #if compte_zeros(grille) == 0:
    #    sys.exit()nouvelles_regles()
    nouvelles_regles()
    afficher_grille()

def droite(event):
    check_deplacement([1,0])
    afficher_grille()

def haut(event):
    check_deplacement([0,-1])
    afficher_grille()

def bas(event):
    check_deplacement([0,1])
    afficher_grille()

top.bind("<Left>", gauche)
top.bind("<Right>", droite)
top.bind("<Up>", haut)
top.bind("<Down>", bas)

afficher_grille()

top.mainloop()