from tkinter import *
import sys
import time
from PIL import ImageTk
from PIL import Image

from __init__ import *
exec(open("__init__.py").read())

from regles import *
exec(open("regles.py").read())

top = Tk()
C = Canvas(top,height = 640, width = 1200, background = "#f12344")

C.pack()
top.title("Anne is stone")

path = "clipped/"

image_anne = ImageTk.PhotoImage(Image.open(path+"anne.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_blue_anne = ImageTk.PhotoImage(Image.open(path+"blue_anne.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_wall = ImageTk.PhotoImage(Image.open(path+"wall2.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_grass = ImageTk.PhotoImage(Image.open(path+"grass2.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_bad_champi = ImageTk.PhotoImage(Image.open(path+"bad_champi.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_good_champi = ImageTk.PhotoImage(Image.open(path+"good_champi.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_auriane = ImageTk.PhotoImage(Image.open(path+"auriane.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_blue_auriane = ImageTk.PhotoImage(Image.open(path+"blue_auriane.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_blue_bad_champi = ImageTk.PhotoImage(Image.open(path+"blue_bad_champi.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_blue_wall = ImageTk.PhotoImage(Image.open(path+"blue_wall.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_DUH = ImageTk.PhotoImage(Image.open(path+"DUH.png").resize((1200,640), Image.ANTIALIAS), master = top)
image_good_champi_anne = ImageTk.PhotoImage(Image.open(path+"good_champi_anne.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_real_blue_grass = ImageTk.PhotoImage(Image.open(path+"blue_grass.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_victory = ImageTk.PhotoImage(Image.open(path+"victory.png").resize((1200,640), Image.ANTIALIAS), master = top)

def update_grille(l1,l2):
    nouv_grille = [[None for j in range(640//taille)] for i in range(1200//taille)]
    for i in range(len(l1)):
        nouv_grille[l1[i].position[0]][l1[i].position[1]] = ("bloc", i)
    for j in range(len(l2)):
        nouv_grille[l2[j].position[0]][l2[j].position[1]] = ("obs", j)
    return nouv_grille

def afficher_grille0(l1, l2):
    im1 = []
    im2 = []
    g = update_grille(l1, l2)
    liste_reg = nouvelles_regles(l1, im2)
    for blocs in l1:
        k = C.create_text(blocs.position[0]*taille+taille//2, blocs.position[1]*taille+taille//2, text = blocs.nom_affiche, font = ("Verdana",7))
        im1.append(k)
    for obstacles in l2:
        if obstacles.mot == "anne":
            if "anne is blue" in liste_regles:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_blue_anne)
            elif "anne is goodchampi" in liste_regles:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_good_champi_anne)
            else:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_anne)
        if obstacles.mot == "auriane":
            if "auriane is blue" in liste_regles:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_blue_auriane)
            else:
                 k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_auriane)
        if obstacles.mot == "grass":
            if "grass is blue" in liste_regles:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_real_blue_grass)
            else:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_grass)
        if obstacles.mot == "wall":
            if "wall is blue" in liste_regles:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_wall)
            else:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_wall)
        if obstacles.mot == "bad champi":
            if "badchampi is blue" in liste_regles:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_blue_bad_champi)
            else:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_bad_champi)
        if obstacles.mot == "good champi":
            k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_good_champi)
        im2.append(k)
    return g, im1, im2

def nouvelle_grille_is(obs, ind, im2):
    if obs.mot == "anne":
        if "anne is blue" in liste_regles:
            C.itemconfig(im2[ind], image = image_blue_anne)
        elif "anne is goodchampi" in liste_regles:
            C.itemconfig(im2[ind], image = image_good_champi_anne)
        else:
            C.itemconfig(im2[ind], image = image_anne)
    if obs.mot == "auriane":
        if "auriane is blue" in liste_regles:
            C.itemconfig(im2[ind], image = image_blue_auriane)
        else:
            C.itemconfig(im2[ind], image = image_auriane)
    if obs.mot == "grass":
        if "grass is blue" in liste_regles:
            C.itemconfig(im2[ind], image = image_real_blue_grass)
        else:
            C.itemconfig(im2[ind], image = image_grass)
    if obs.mot == "wall":
        if "wall is blue" in liste_regles:
            C.itemconfig(im2[ind], image = image_wall)
        else:
            C.itemconfig(im2[ind], image = image_wall)
    if obs.mot == "bad champi":
        if "badchampi is blue" in liste_regles:
            C.itemconfig(im2[ind], image = image_blue_bad_champi)
        else:
            C.itemconfig(im2[ind], image = image_bad_champi)
    if obs.mot == "good champi":
        C.itemconfig(im2[ind], image = image_good_champi)
    return im2


def afficher_grille(l1, l2, im1, im2, liste_obj, actualise):
    g = update_grille(l1, l2)
    if len(liste_obj) > 1:
        for i in range(len(l1)):
            diff_pos = (actualise*(l1[i].position[0]-liste_obj[-2][0][i].position[0]),actualise*(l1[i].position[1]-liste_obj[-2][0][i].position[1]))
            if diff_pos != (0,0):
                C.move(im1[i], diff_pos[0]*taille, diff_pos[1]*taille)
        for j in range(len(l2)):
            diff_pos = (actualise*(l2[j].position[0]-liste_obj[-2][1][j].position[0]),actualise*(l2[j].position[1]-liste_obj[-2][1][j].position[1]))
            if diff_pos != (0,0):
                C.move(im2[j], diff_pos[0]*taille, diff_pos[1]*taille)
    return g, im1, im2

def afficher_grille_rewind(l1, l2, im1, im2, liste_obj):
    g = update_grille(l1, l2)
    if len(liste_obj) > 1:
        for i in range(len(l1)):
            diff_pos = (l1[i].position[0]-liste_obj[-2][0][i].position[0],l1[i].position[1]-liste_obj[-2][0][i].position[1])
            if diff_pos != (0,0):
                C.move(im1[i], -diff_pos[0]*taille, -diff_pos[1]*taille)
        for j in range(len(l2)):
            diff_pos = (l2[j].position[0]-liste_obj[-2][1][j].position[0],l2[j].position[1]-liste_obj[-2][1][j].position[1])
            if diff_pos != (0,0):
                C.move(im2[j], -diff_pos[0]*taille, -diff_pos[1]*taille)
    return g, im1, im2