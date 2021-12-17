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
C = Canvas(top,height = 680, width = 1200)

C.pack()
top.title("Anne is stone")

images_path = "images/"
normal_texts_path = "texts/normal/"
inverted_texts_path = "texts/inverted/"
backgrounds_path = "backgrounds/"

# images_champi_background = ImageTk.PhotoImage(Image.open(images_path+"champi_background4.jpg").resize((1200, 680), Image.ANTIALIAS), master = top)
# background_fall_brown = ImageTk.PhotoImage(Image.open(backgrounds_path+"brown_from_fall.png").resize((1200, 680), Image.ANTIALIAS), master = top)
# fall_background = ImageTk.PhotoImage(Image.open(backgrounds_path+"fall-baba_is_you.png").resize((1200, 680), Image.ANTIALIAS), master = top)
clipped_fall_background = ImageTk.PhotoImage(Image.open(backgrounds_path+"clipped_fall-baba_is_you.png").resize((1200, 680), Image.ANTIALIAS), master = top)
C.create_image(0, 0, anchor = NW, image = clipped_fall_background)

image_anne = ImageTk.PhotoImage(Image.open(images_path+"anne.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_blue_anne = ImageTk.PhotoImage(Image.open(images_path+"blue_anne.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_good_champi_anne = ImageTk.PhotoImage(Image.open(images_path+"good_champi_anne.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_auriane = ImageTk.PhotoImage(Image.open(images_path+"auriane.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_blue_auriane = ImageTk.PhotoImage(Image.open(images_path+"blue_auriane.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_bad_champi = ImageTk.PhotoImage(Image.open(images_path+"bad_champi.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_blue_bad_champi = ImageTk.PhotoImage(Image.open(images_path+"blue_bad_champi.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_good_champi = ImageTk.PhotoImage(Image.open(images_path+"good_champi.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_blue_good_champi = ImageTk.PhotoImage(Image.open(images_path+"blue_good_champi.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_grass = ImageTk.PhotoImage(Image.open(images_path+"grass.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_blue_grass = ImageTk.PhotoImage(Image.open(images_path+"blue_grass.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_wall = ImageTk.PhotoImage(Image.open(images_path+"wall.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_blue_wall = ImageTk.PhotoImage(Image.open(images_path+"blue_wall.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_door = ImageTk.PhotoImage(Image.open(images_path+"door.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_blue_door = ImageTk.PhotoImage(Image.open(images_path+"blue_door.png").resize((taille,taille), Image.ANTIALIAS), master = top)
image_DUH = ImageTk.PhotoImage(Image.open(images_path+"DUH.png").resize((1200,680), Image.ANTIALIAS), master = top)
image_victory = ImageTk.PhotoImage(Image.open(images_path+"victory.png").resize((1200,680), Image.ANTIALIAS), master = top)

text_anne = ImageTk.PhotoImage(Image.open(normal_texts_path+"anne.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_wall = ImageTk.PhotoImage(Image.open(normal_texts_path+"wall.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_grass = ImageTk.PhotoImage(Image.open(normal_texts_path+"grass.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_bad_champi = ImageTk.PhotoImage(Image.open(normal_texts_path+"bad_champi.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_good_champi = ImageTk.PhotoImage(Image.open(normal_texts_path+"good_champi.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_aurianne = ImageTk.PhotoImage(Image.open(normal_texts_path+"aurianne.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_door = ImageTk.PhotoImage(Image.open(normal_texts_path+"door.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_text = ImageTk.PhotoImage(Image.open(normal_texts_path+"text.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_is = ImageTk.PhotoImage(Image.open(normal_texts_path+"is.png").resize((taille,taille), Image.ANTIALIAS), master = top)

text_open = ImageTk.PhotoImage(Image.open(inverted_texts_path+"open.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_hot = ImageTk.PhotoImage(Image.open(inverted_texts_path+"hot.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_stop = ImageTk.PhotoImage(Image.open(inverted_texts_path+"stop.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_death = ImageTk.PhotoImage(Image.open(inverted_texts_path+"death.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_shut = ImageTk.PhotoImage(Image.open(inverted_texts_path+"shut.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_melt = ImageTk.PhotoImage(Image.open(inverted_texts_path+"melt.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_win = ImageTk.PhotoImage(Image.open(inverted_texts_path+"win.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_greener = ImageTk.PhotoImage(Image.open(inverted_texts_path+"greener.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_blue = ImageTk.PhotoImage(Image.open(inverted_texts_path+"blue.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_push = ImageTk.PhotoImage(Image.open(inverted_texts_path+"push.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_weak = ImageTk.PhotoImage(Image.open(inverted_texts_path+"weak.png").resize((taille,taille), Image.ANTIALIAS), master = top)
text_you = ImageTk.PhotoImage(Image.open(inverted_texts_path+"you.png").resize((taille,taille), Image.ANTIALIAS), master = top)

def update_grille(l1,l2):
    nouv_grille = [[None for j in range(680//taille)] for i in range(1200//taille)]
    for i in range(len(l1)):
        nouv_grille[l1[i].position[0]][l1[i].position[1]] = ("bloc", i)
    for j in range(len(l2)):
        nouv_grille[l2[j].position[0]][l2[j].position[1]] = ("obs", j)
    return nouv_grille

def afficher_grille0(l1, l2):
    global liste_regles
    im1 = []
    im2 = []
    g = update_grille(l1, l2)
    liste_reg = nouvelles_regles(l1, im2)
    for bloc in l1:
        if bloc.mot == "anne":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_anne)
        elif bloc.mot == "wall":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_wall)
        elif bloc.mot == "grass":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_grass)
        elif bloc.mot == "bad champi":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_bad_champi)
        elif bloc.mot == "good champi":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_good_champi)
        elif bloc.mot == "auriane":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_aurianne)
        elif bloc.mot == "door":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_door)
        elif bloc.mot == "open":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_open)
        elif bloc.mot == "hot":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_hot)
        elif bloc.mot == "stop":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_stop)
        elif bloc.mot == "text":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_text)
        elif bloc.mot == "is":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_is)
        elif bloc.mot == "death":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_death)
        elif bloc.mot == "shut":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_shut)
        elif bloc.mot == "melt":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_melt)
        elif bloc.mot == "win":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_win)
        elif bloc.mot == "greener":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_greener)
        elif bloc.mot == "blue":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_blue)
        elif bloc.mot == "push":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_push)
        elif bloc.mot == "weak":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_weak)
        elif bloc.mot == "you":
            k = C.create_image(bloc.position[0]*taille+1, bloc.position[1]*taille+1, anchor = NW, image = text_you)
        else:
            k = C.create_text(bloc.position[0]*taille+taille//2, bloc.position[1]*taille+taille//2, text = bloc.nom_affiche, font = ("Verdana",7))
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
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_blue_grass)
            else:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_grass)
        if obstacles.mot == "wall":
            if "wall is blue" in liste_regles:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_blue_wall)
            else:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_wall)
        if obstacles.mot == "bad champi":
            if "bad champi is blue" in liste_regles:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_blue_bad_champi)
            else:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_bad_champi)
        if obstacles.mot == "good champi":
            if "good champi is blue" in liste_regles:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_blue_good_champi)
            else:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_good_champi)
        if obstacles.mot == "door":
            if "door is blue" in liste_regles:
                    k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_blue_door)
            else:
                k = C.create_image(obstacles.position[0]*taille+1, obstacles.position[1]*taille+1, anchor = NW, image = image_door)
        im2.append(k)
    return g, im1, im2

def nouvelle_grille_is(l, obs, ind, im2):
    if obs.mot == "anne":
        if "anne is blue" in l:
            C.itemconfig(im2[ind], image = image_blue_anne)
        elif "anne is goodchampi" in l:
            C.itemconfig(im2[ind], image = image_good_champi_anne)
        else:
            C.itemconfig(im2[ind], image = image_anne)
    if obs.mot == "auriane":
        if "auriane is blue" in l:
            C.itemconfig(im2[ind], image = image_blue_auriane)
        else:
            C.itemconfig(im2[ind], image = image_auriane)
    if obs.mot == "grass":
        if "grass is blue" in l:
            C.itemconfig(im2[ind], image = image_blue_grass)
        else:
            C.itemconfig(im2[ind], image = image_grass)
    if obs.mot == "wall":
        if "wall is blue" in l:
            C.itemconfig(im2[ind], image = image_blue_wall)
        else:
            C.itemconfig(im2[ind], image = image_wall)
    if obs.mot == "bad champi":
        if "bad champi is blue" in l:
            C.itemconfig(im2[ind], image = image_blue_bad_champi)
        else:
            C.itemconfig(im2[ind], image = image_bad_champi)
    if obs.mot == "good champi":
        if "good champi is blue" in l:
            C.itemconfig(im2[ind], image = image_blue_good_champi)
        else:
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
        list_l1 = liste_obj[-2][0]
        list_l2 = liste_obj[-2][1]
        l, im2 = nouvelles_regles(list_l1, im2)
        for i in range(len(l1)):
            diff_pos = (l1[i].position[0]-liste_obj[-2][0][i].position[0],l1[i].position[1]-liste_obj[-2][0][i].position[1])
            if diff_pos != (0,0):
                C.move(im1[i], -diff_pos[0]*taille, -diff_pos[1]*taille)
        for j in range(len(l2)):
            diff_pos = (l2[j].position[0]-liste_obj[-2][1][j].position[0],l2[j].position[1]-liste_obj[-2][1][j].position[1])
            if diff_pos != (0,0):
                C.move(im2[j], -diff_pos[0]*taille, -diff_pos[1]*taille)
            if list_l2[j].mot == "anne":
                if "anne is blue" in l:
                    C.itemconfig(im2[j], image = image_blue_anne)
                elif "anne is goodchampi" in l:
                    C.itemconfig(im2[j], image = image_good_champi_anne)
                else:
                    C.itemconfig(im2[j], image = image_anne)
            if list_l2[j].mot == "auriane":
                if "auriane is blue" in l:
                    C.itemconfig(im2[j], image = image_blue_auriane)
                else:
                    C.itemconfig(im2[j], image = image_auriane)
            if list_l2[j].mot == "grass":
                if "grass is blue" in l:
                    C.itemconfig(im2[j], image = image_blue_grass)
                else:
                    C.itemconfig(im2[j], image = image_grass)
            if list_l2[j].mot == "wall":
                if "wall is blue" in l:
                    C.itemconfig(im2[j], image = image_blue_wall)
                else:
                    C.itemconfig(im2[j], image = image_wall)
            if list_l2[j].mot == "bad champi":
                if "bad champi is blue" in l:
                    C.itemconfig(im2[j], image = image_blue_bad_champi)
                else:
                    C.itemconfig(im2[j], image = image_bad_champi)
            if list_l2[j].mot == "good champi":
                if "good champi is blue" in l:
                    C.itemconfig(im2[j], image = image_blue_good_champi)
                else:
                    C.itemconfig(im2[j], image = image_good_champi)
            if list_l2[j].mot == "door":
                if "door is blue" in l:
                    C.itemconfig(im2[j], image = image_blue_door)
                else:
                    C.itemconfig(im2[j], image = image_door)
    return g, im1, im2