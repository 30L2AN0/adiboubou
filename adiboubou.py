from tkinter import *
import sys
from PIL import ImageTk
from PIL import Image

top = Tk()
C = Canvas(top,height = 600, width = 1200, background = "#ff7e4c")

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

global anne_position
global liste_obstacles
global liste_blocs
global liste_regles
global taille
global grille

taille = 40

grille = [[None for j in range(600//taille)] for i in range(1200//taille)]

image_anne = ImageTk.PhotoImage(Image.open("anne.png").resize((taille,taille), Image.ANTIALIAS))
image_wall = ImageTk.PhotoImage(Image.open("mur.png").resize((taille,taille), Image.ANTIALIAS))
image_grass = ImageTk.PhotoImage(Image.open("grass.png").resize((taille,taille), Image.ANTIALIAS))

liste_blocs = []
liste_obstacles = []
liste_regles = []


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