#programmer pull, move, et régler problème couleur

from __init__ import *
exec(open("__init__.py").read())

global liste_obstacles, liste_blocs, liste_regles, taille, grille, liste_liste_objets, liste_noun, liste_adj, liste_bleus

liste_noun = ["auriane", "anne", "good champi", "bad champi", "wall", "grass", "door"]
liste_adj = ["open", "shut", "greener", "stop", "push", "blue", "sink", "melt", "hot"]

def distance(X,Y):
    return abs(X[0]-Y[0])+2*abs(X[1]-Y[1])

def distance_normale(X,Y):
    return abs(X[0]-Y[0])+abs(X[1]-Y[1])

def nouvelles_regles(l, im2):
    global liste_noun, liste_adj, liste_obstacles
    nouvelle_liste_regles = []
    regle_tautologique = []
    n = len(l)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                p1 = l[i].position
                p2 = l[j].position
                p3 = l[k].position
                liste_distances = [distance(p1,p2), distance(p1,p3), distance(p2,p3)]
                liste_dist = [distance_normale(p1,p2), distance_normale(p1,p3), distance_normale(p2,p3)]
                liste_dist.sort()
                if liste_dist == [1,1,2]:
                    if liste_distances == [2,2,4] and p2[1] < p3[1]:
                        if l[j].type == "noun" and l[i].type == "verb" and (not l[k].type == "verb"):
                            nouvelle_liste_regles.append(l[j].mot+" "+l[i].mot+" "+l[k].mot)
                    if liste_distances == [2,4,2] and p1[1] < p3[1]:
                        if l[i].type == "noun" and l[j].type == "verb" and (not l[k].type == "verb"):
                            nouvelle_liste_regles.append(l[i].mot+" "+l[j].mot+" "+l[k].mot)
                    if liste_distances == [4,2,2] and p1[1] < p2[1]:
                        if l[i].type == "noun" and l[k].type == "verb" and (not l[j].type == "verb"):
                            nouvelle_liste_regles.append(l[i].mot+" "+l[k].mot+" "+l[j].mot)
                    if liste_distances == [2,2,4] and p2[1] > p3[1]:
                        if l[k].type == "noun" and l[i].type == "verb" and (not l[j].type == "verb"):
                            nouvelle_liste_regles.append(l[k].mot+" "+l[i].mot+" "+l[j].mot)
                    if liste_distances == [2,4,2] and p1[1] > p3[1]:
                        if l[k].type == "noun" and l[j].type == "verb" and (not l[i].type == "verb"):
                            nouvelle_liste_regles.append(l[k].mot+" "+l[j].mot+" "+l[i].mot)
                    if liste_distances == [4,2,2] and p1[1] > p2[1]:
                        if l[j].type == "noun" and l[k].type == "verb" and (not l[i].type == "verb"):
                            nouvelle_liste_regles.append(l[j].mot+" "+l[k].mot+" "+l[i].mot)
                    if liste_distances == [1,1,2] and p2[0] < p3[0]:
                        if l[j].type == "noun" and l[i].type == "verb" and (not l[k].type == "verb"):
                            nouvelle_liste_regles.append(l[j].mot+" "+l[i].mot+" "+l[k].mot)
                    if liste_distances == [1,2,1] and p1[0] < p3[0]:
                        if l[i].type == "noun" and l[j].type == "verb" and (not l[k].type == "verb"):
                            nouvelle_liste_regles.append(l[i].mot+" "+l[j].mot+" "+l[k].mot)
                    if liste_distances == [2,1,1] and p1[0] < p2[0]:
                        if l[i].type == "noun" and l[k].type == "verb" and (not l[j].type == "verb"):
                            nouvelle_liste_regles.append(l[i].mot+" "+l[k].mot+" "+l[j].mot)
                    if liste_distances == [1,1,2] and p2[0] > p3[0]:
                        if l[k].type == "noun" and l[i].type == "verb" and (not l[j].type == "verb"):
                            nouvelle_liste_regles.append(l[k].mot+" "+l[i].mot+" "+l[j].mot)
                    if liste_distances == [1,2,1] and p1[0] > p3[0]:
                        if l[k].type == "noun" and l[j].type == "verb" and (not l[i].type == "verb"):
                            nouvelle_liste_regles.append(l[k].mot+" "+l[j].mot+" "+l[i].mot)
                    if liste_distances == [2,1,1] and p1[0] > p2[0]:
                        if l[j].type == "noun" and l[k].type == "verb" and (not l[i].type == "verb"):
                            nouvelle_liste_regles.append(l[j].mot+" "+l[k].mot+" "+l[i].mot)
    for regle in nouvelle_liste_regles:
        x = regle.split(" ")
        for i in range(len(x)):
            if x[i] == "is" and x[:i] == x[i+1:]:
                regle_tautologique.append(regle)
    for regle in nouvelle_liste_regles:
        for regle_toto in regle_tautologique:
            if regle_toto != regle:
                x = regle.split(" ")
                y = regle_toto.split(" ")
                for i in range(len(x)):
                    if x[i] == "is":
                        for j in range(len(y)):
                            if y[i] == "is":
                                if y[:i] == x[:i] and " ".join(x[i+1:]) in liste_noun:
                                    if regle in nouvelle_liste_regles:
                                        nouvelle_liste_regles.remove(regle)
    l, liste_obstacles, im2 = appliquer_nouvelles_regles(nouvelle_liste_regles, l, liste_obstacles, im2)
    return l, nouvelle_liste_regles, im2


def appliquer_nouvelles_regles(l, l1, l2, im2):
    global images_blocs
    if len(im2) > 0:
        for regle in l:
            x = regle.split(" ")
            for i in range(len(x)):
                if x[i] == "is":
                    if " ".join(x[:i]) in liste_noun and " ".join(x[i+1:]) in liste_noun:
                        for ind in range(len(l2)):
                            if " ".join(x[:i]) == l2[ind].mot:
                                l2[ind].mot = " ".join(x[i+1:])
                                im2 = nouvelle_grille_is(l, l2[ind], ind, im2)
                    if " ".join(x[i+1:]) == "blue":
                        for ind in range(len(l2)):
                            if " ".join(x[:i]) == l2[ind].mot:
                                im2 = nouvelle_grille_is(l, l2[ind], ind, im2)
                    if " ".join(x[:i]) in liste_noun and " ".join(x[i+1:]) == "text":
                        for obs in l2:
                            if " ".join(x[:i]) == obs.mot:
                                l1.append(Bloc("noun", obs.mot, obs.position))
                                images_blocs.append(ajout_affichage_bloc(l1[-1]))
                                obs.position = (-1,-1)
                                obs.mot = "rien"
    return l1, l2, im2


def pushable(ob, l):
    for regle in l:
        if regle.startswith(ob.mot) and regle.endswith("is push"):
            return True
        if regle.startswith(ob.mot) and regle.endswith("is you"):
            return True
    return False

# DEATH
def prochain_bloc_mort(k, l, l2):
    if k != None:
        element, indice = k
        if element == "obs":
            for condition in l:
                if condition.startswith(l2[indice].mot) and condition.endswith("is death"):
                    return True
        if element == "bloc":
            if "text is death" in l:
                return True
    return False

# MELT/HOT
def condition_melt_hot(g, l, l2, i1, i2, t):
    if i1+t[0] < largeur//taille and i1+t[0] >= 0 and i2+t[1] < hauteur//taille and i2+t[1] >= 0:
        if g[i1][i2] != None and g[i1+t[0]][i2+t[1]] != None:
            if g[i1][i2][0] == "obs" and g[i1+t[0]][i2+t[1]][0] == "obs":
                obs1 = l2[g[i1][i2][1]]
                obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
                for regle1 in l:
                    for regle2 in l:
                        if regle1.startswith(obs1.mot) and regle1.endswith("is hot") and regle2.startswith(obs2.mot) and regle2.endswith("is melt") or regle1.startswith(obs2.mot) and regle1.endswith("is hot") and regle2.startswith(obs1.mot) and regle2.endswith("is melt"):
                            return True
            if g[i1][i2][0] == "bloc" and g[i1+t[0]][i2+t[1]][0] == "obs":
                obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
                if "text is hot" in l:
                    for regle in l:
                        if regle.startswith(obs2.mot) and regle.endswith("is melt"):
                            return True
                if "text is melt" in l:
                    for regle in l:
                        if regle.startswith(obs2.mot) and regle.endswith("is hot"):
                            return True

            if g[i1][i2][0] == "obs" and g[i1+t[0]][i2+t[1]][0] == "bloc":
                obs1 = l2[g[i1][i2][1]]
                if "text is hot" in l:
                    for regle in l:
                        if regle.startswith(obs1.mot) and regle.endswith("is melt"):
                            return True
                if "text is melt" in l:
                    for regle in l:
                        if regle.startswith(obs1.mot) and regle.endswith("is hot"):
                            return True
            if g[i1][i2][0] == "bloc" and g[i1+t[0]][i2+t[1]][0] == "bloc":
                if "text is melt" in l and "text is hot" in l:
                    return True
    return False

def indice_melt_hot(g, l, l1, l2, i1, i2, t):
    if g[i1][i2][0] == "obs" and g[i1+t[0]][i2+t[1]][0] == "obs":
        obs1 = l2[g[i1][i2][1]]
        obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
        for regle1 in l:
            for regle2 in l:
                if regle1.startswith(obs1.mot) and regle1.endswith("is hot") and regle2.startswith(obs2.mot) and regle2.endswith("is melt"):
                    return i1+t[0], i2+t[1]
    if g[i1][i2][0] == "bloc" and g[i1+t[0]][i2+t[1]][0] == "obs":
        obs1 = l1[g[i1][i2][1]]
        obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
        if "text is hot" in l:
            return i1+t[0], i2+t[1]
    if g[i1][i2][0] == "obs" and g[i1+t[0]][i2+t[1]][0] == "bloc":
        obs1 = l2[g[i1][i2][1]]
        obs2 = l1[g[i1+t[0]][i2+t[1]][1]]
        if "text is melt" in l:
            return i1+t[0], i2+t[1]
    return i1, i2

# WIN
def prochain_bloc_win(k, l, l2):
    if k != None:
        element, indice = k
        if element == "obs":
            for condition in l:
                if condition.startswith(l2[indice].mot) and condition.endswith("is win"):
                    return True
        if element == "bloc":
            if "text is win" in l:
                    return True
    return False

# WEAK
def condition_weak(g, l, l2, i1, i2, t):
    if i1+t[0] < largeur//taille and i1+t[0] >= 0 and i2+t[1] < hauteur//taille and i2+t[1] >= 0:
        if g[i1][i2] != None and g[i1+t[0]][i2+t[1]] != None:
            if g[i1][i2][0] == "obs" and g[i1+t[0]][i2+t[1]][0] == "obs":
                obs1 = l2[g[i1][i2][1]]
                obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
                for regle1 in l:
                    if pushable(obs1, l) and regle1.startswith(obs1.mot) and regle1.endswith("is weak") and not pushable(obs2, l):
                        return True
    else:
        if g[i1][i2] != None:
            obs1 = l2[g[i1][i2][1]]
            for regle1 in l:
                if pushable(obs1, l) and regle1.startswith(obs1.mot) and regle1.endswith("is weak"):
                    return True
    return False

def condition_weak_text(g, l, l1, l2, i1, i2, t):
    if i1+t[0] < largeur//taille and i1+t[0] >= 0 and i2+t[1] < hauteur//taille and i2+t[1] >= 0:
        if g[i1][i2] != None and g[i1+t[0]][i2+t[1]] != None:
            if g[i1][i2][0] == "bloc" and g[i1+t[0]][i2+t[1]][0] == "obs":
                obs1 = l1[g[i1][i2][1]]
                obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
                for regle1 in l:
                    if regle1 == "text is weak" and not pushable(obs2, l):
                        return True
    else:
        if g[i1][i2] != None:
            if g[i1][i2][0] == "bloc":
                for regle1 in l:
                    if regle1 == "text is weak":
                        return True
    return False

# OPEN/SHUT
def condition_open_shut(g, l, l2, i1, i2, t):
    if i1+t[0] < largeur//taille and i1+t[0] >= 0 and i2+t[1] < hauteur//taille and i2+t[1] >= 0:
        if g[i1][i2] != None and g[i1+t[0]][i2+t[1]] != None:
            if g[i1][i2][0] == "obs" and g[i1+t[0]][i2+t[1]][0] == "obs":
                obs1 = l2[g[i1][i2][1]]
                obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
                for regle1 in l:
                    for regle2 in l:
                        if regle1.startswith(obs1.mot) and regle1.endswith("is shut") and regle2.startswith(obs2.mot) and regle2.endswith("is open") or regle1.startswith(obs2.mot) and regle1.endswith("is shut") and regle2.startswith(obs1.mot) and regle2.endswith("is open"):
                            return True
    return False

# SINK
def condition_sink(g, l, l2, i1, i2, t):
    if i1+t[0] < largeur//taille and i1+t[0] >= 0 and i2+t[1] < hauteur//taille and i2+t[1] >= 0:
        if g[i1][i2] != None and g[i1+t[0]][i2+t[1]] != None:
            if g[i1][i2][0] == "obs" and g[i1+t[0]][i2+t[1]][0] == "obs":
                obs1 = l2[g[i1][i2][1]]
                obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
                for regle in l:
                        if (regle.startswith(obs1.mot) or regle.startswith(obs2.mot)) and regle.endswith("is sink"):
                            return True
            if g[i1][i2][0] == "bloc" and g[i1+t[0]][i2+t[1]][0] == "obs":
                obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
                #on ne peut pas être le texte donc moins de cas à traiter
                for regle in l:
                    if regle.startswith(obs2.mot) and regle.endswith("is sink"):
                        return True
            if g[i1][i2][0] == "obs" and g[i1+t[0]][i2+t[1]][0] == "bloc":
                obs1 = l2[g[i1][i2][1]]
                if "text is sink" in l:
                    return True
                for regle in l:
                    if regle.startswith(obs1.mot) and regle.endswith("is sink"):
                        return True
    return False

def check_deplacement(t, l, l1, l2, g, liste_obj):
    actu = False
    liste_you = []
    deja_bouge_bloc = [False for i in range(len(l1))]
    deja_bouge_obs = [False for i in range(len(l2))]
    for regle in l:
        if regle.endswith("is you"):
            liste_you.append(regle[:-7])
    for obstacle in range(len(l2)):
        if l2[obstacle].mot in liste_you and l2[obstacle].position[0]+t[0] < largeur//taille and l2[obstacle].position[0]+t[0] >= 0 and l2[obstacle].position[1]+t[1] < hauteur//taille and l2[obstacle].position[1]+t[1] >= 0:
            if g[l2[obstacle].position[0]+t[0]][l2[obstacle].position[1]+t[1]] == None and not deja_bouge_obs[obstacle]:
                deja_bouge_obs[obstacle] = True
                l2[obstacle].set((l2[obstacle].position[0]+t[0], l2[obstacle].position[1]+t[1]))
                actu = True
            elif prochain_bloc_mort(g[l2[obstacle].position[0]+t[0]][l2[obstacle].position[1]+t[1]], l, l2):
                l2[obstacle].set((-1,-1))
                actu = True
            elif prochain_bloc_win(g[l2[obstacle].position[0]+t[0]][l2[obstacle].position[1]+t[1]], l, l2):
                l2[obstacle].set((-1,-1))
                actu = True
                C.create_image(0,0, anchor = NW, image = image_victory)
            else:
                ind1, ind2 = l2[obstacle].position
                liste_apres = []
                while ind1 < largeur//taille and ind1 >= 0 and ind2 < hauteur//taille and ind2 >= 0 and g[ind1][ind2] != None and not condition_open_shut(g, l, l2, ind1, ind2, t) and not condition_weak(g, l, l2, ind1, ind2, t) and not condition_melt_hot(g, l, l2, ind1, ind2, t) and not condition_weak_text(g, l, l1, l2, ind1, ind2, t) and not condition_sink(g, l, l2, ind1, ind2, t):
                    liste_apres.append((ind1,ind2))
                    ind1 += t[0]
                    ind2 += t[1]
                if condition_open_shut(g, l, l2, ind1, ind2, t) or condition_weak(g, l, l2, ind1, ind2, t) or condition_melt_hot(g, l, l2, ind1, ind2, t) or condition_weak_text(g, l, l1, l2, ind1, ind2, t) or condition_sink(g, l, l2, ind1, ind2, t):
                    liste_apres.append((ind1,ind2))
                if ind1 < largeur//taille and ind1 >= 0 and ind2 < hauteur//taille and ind2 >= 0:
                    poussable = True
                    for tup_indice in liste_apres:
                        ind1, ind2 = tup_indice
                        element = g[ind1][ind2]
                        if element != None:
                            if element[0] == "obs":
                                if not pushable(l2[element[1]], l):
                                    poussable = False
                    if poussable:
                        for tup_ind in reversed(liste_apres):
                            ind1, ind2 = tup_ind
                            element = g[ind1][ind2]
                            if element != None:
                                if element[0] == "obs" and not deja_bouge_obs[element[1]]:
                                    if condition_open_shut(g, l, l2, ind1, ind2, t):
                                        l2[g[ind1+t[0]][ind2+t[1]][1]].position = (-1,-1)
                                        l2[g[ind1][ind2][1]].position = (-1,-1)
                                    elif condition_weak(g, l, l2, ind1, ind2, t):
                                        l2[g[ind1][ind2][1]].position = (-1,-1)
                                    elif condition_melt_hot(g, l, l2, ind1, ind2, t):
                                        a1, a2 = indice_melt_hot(g, l, l1, l2, ind1, ind2, t)
                                        if g[a1][a2][0] == "obs":
                                            l2[g[a1][a2][1]].position = (-1,-1)
                                        else:
                                            l1[g[a1][a2][1]].position = (-1,-1)
                                        if a1 != ind1 or a2 != ind2:
                                            l2[element[1]].set((l2[element[1]].position[0]+t[0],l2[element[1]].position[1]+t[1]))
                                    elif condition_sink(g, l, l2, ind1, ind2, t):
                                        l2[g[ind1][ind2][1]].position = (-1,-1)
                                        if g[ind1+t[0]][ind2+t[1]][0] == "obs":
                                            l2[g[ind1+t[0]][ind2+t[1]][1]].position = (-1,-1)
                                        else:
                                            l1[g[ind1+t[0]][ind2+t[1]][1]].position = (-1,-1)
                                    else:
                                        l2[element[1]].set((l2[element[1]].position[0]+t[0],l2[element[1]].position[1]+t[1]))
                                        deja_bouge_obs[element[1]] = True
                                if element[0] == "bloc" and not deja_bouge_bloc[element[1]]:
                                    if condition_weak_text(g, l, l1, l2, ind1, ind2, t):
                                        l1[g[ind1][ind2][1]].position = (-1,-1)
                                    elif condition_melt_hot(g, l, l2, ind1, ind2, t):
                                        a1, a2 = indice_melt_hot(g, l, l1, l2, ind1, ind2, t)
                                        if g[a1][a2][0] == "obs":
                                            l2[g[a1][a2][1]].position = (-1,-1)
                                        else:
                                            l1[g[a1][a2][1]].position = (-1,-1)
                                        if a1 != ind1 or a2 != ind2:
                                            l1[element[1]].set((l1[element[1]].position[0]+t[0],l1[element[1]].position[1]+t[1]))
                                    elif condition_sink(g, l, l2, ind1, ind2, t):
                                        l1[g[ind1][ind2][1]].position = (-1,-1)
                                        if g[ind1+t[0]][ind2+t[1]][0] == "obs":
                                            l2[g[ind1+t[0]][ind2+t[1]][1]].position = (-1,-1)
                                        else:
                                            l1[g[ind1+t[0]][ind2+t[1]][1]].position = (-1,-1)
                                    else:
                                        l1[element[1]].set((l1[element[1]].position[0]+t[0],l1[element[1]].position[1]+t[1]))
                                        deja_bouge_bloc[element[1]] = True
                        actu = True
    if actu:
        return 1
    return 0



def checker_regles(l, im):
    regle_you = []
    for regle in l:
        if regle.endswith("is you"):
            regle_you.append(regle[:-7])
    if regle_you == []:
        return False
    if "bad champi is stop" in l and len(im) == 0:
        k = C.create_image(0,0, anchor = NW, image = image_victory)
        images_autres.append(k)
    if "bad champi is stop" in l:
        return False
    if "grass is greener" in l and len(im) == 0:
        k = C.create_image(0,0, anchor = NW, image = image_DUH)
        images_autres.append(k)
    if "grass is greener" in l:
        return False
    for k in im:
        C.delete(k)
        im.remove(k)
    im = []
    return True

