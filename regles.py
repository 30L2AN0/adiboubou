from __init__ import *
exec(open("__init__.py").read())

global liste_obstacles, liste_blocs, liste_regles, taille, grille, liste_liste_objets, liste_noun, liste_adj

liste_noun = ["good champi", "auriane", "anne", "bad champi", "wall", "grass"]
liste_adj = ["open", "shut", "greener", "stop", "push"]

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
    liste_obstacles, im2 = appliquer_nouvelles_regles(nouvelle_liste_regles, liste_obstacles, im2)
    return nouvelle_liste_regles, im2

def appliquer_nouvelles_regles(l, l2, im2):
    for i in range(4):
        for regle in l:
            x = regle.split(" ")
            for i in range(len(x)):
                if x[i] == "is":
                    if " ".join(x[:i]) in liste_noun and " ".join(x[i+1:]) in liste_noun:
                        for ind in range(len(l2)):
                            if " ".join(x[:i]) == l2[ind].mot:
                                l2[ind].mot = " ".join(x[i+1:])
                                im2 = nouvelle_grille_is(l2[ind], ind, im2)
    return l2, im2


def pushable(ob, l):
    for regle in l:
        if regle.startswith(ob.mot) and regle.endswith("is push"):
            return True
        if regle.startswith(ob.mot) and regle.endswith("is you"):
            return True
    #ajouter d'autres conditions plus tard
    return False

def prochain_bloc_mort(k, l, l2):
    if k != None:
        element, indice = k
        if element == "obs":
            for condition in l:
                if condition.startswith(l2[indice].mot) and condition.endswith("is death"):
                    return True
    return False

def condition_melt_hot(g, l, l2, i1, i2, t):
    if i1+t[0] < 30 and i1+t[0] >= 0 and i2+t[1] < 16 and i2+t[1] >= 0:
        if g[i1][i2] != None and g[i1+t[0]][i2+t[1]] != None:
            if g[i1][i2][0] == "obs" and g[i1+t[0]][i2+t[1]][0] == "obs":
                obs1 = l2[g[i1][i2][1]]
                obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
                for regle1 in l:
                    for regle2 in l:
                        if regle1.startswith(obs1.mot) and regle1.endswith("is hot") and regle2.startswith(obs2.mot) and regle2.endswith("is melt") or regle1.startswith(obs2.mot) and regle1.endswith("is hot") and regle2.startswith(obs1.mot) and regle2.endswith("is melt"):
                            return True
    return False

def indice_melt_hot(g, l, l2, i1, i2, t):
    obs1 = l2[g[i1][i2][1]]
    obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
    for regle1 in l:
        for regle2 in l:
            if regle1.startswith(obs1.mot) and regle1.endswith("is hot") and regle2.startswith(obs2.mot) and regle2.endswith("is melt"):
                return i1+t[0], i2+t[1]
    return i1, i2


def prochain_bloc_win(k, l, l2):
    if k != None:
        element, indice = k
        if element == "obs":
            for condition in l:
                if condition.startswith(l2[indice].mot) and condition.endswith("is win"):
                    return True
    return False

def condition_weak(g, l, l2, i1, i2, t):
    if i1+t[0] < 30 and i1+t[0] >= 0 and i2+t[1] < 16 and i2+t[1] >= 0:
        if g[i1][i2] != None and g[i1+t[0]][i2+t[1]] != None:
            if g[i1][i2][0] == "obs" and g[i1+t[0]][i2+t[1]][0] == "obs":
                obs1 = l2[g[i1][i2][1]]
                obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
                for regle1 in l:
                    if pushable(obs1, l) and regle1.startswith(obs1.mot) and regle1.endswith("is weak") and not pushable(obs2, l):
                            return True
    return False

def condition_open_shut(g, l, l2, i1, i2, t):
    if i1+t[0] < 30 and i1+t[0] >= 0 and i2+t[1] < 16 and i2+t[1] >= 0:
        if g[i1][i2] != None and g[i1+t[0]][i2+t[1]] != None:
            if g[i1][i2][0] == "obs" and g[i1+t[0]][i2+t[1]][0] == "obs":
                obs1 = l2[g[i1][i2][1]]
                obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
                for regle1 in l:
                    for regle2 in l:
                        if regle1.startswith(obs1.mot) and regle1.endswith("is shut") and regle2.startswith(obs2.mot) and regle2.endswith("is open") or regle1.startswith(obs2.mot) and regle1.endswith("is shut") and regle2.startswith(obs1.mot) and regle2.endswith("is open"):
                            return True
    return False

def condition_weak_text(g, l, l1, l2, i1, i2, t):
    if i1+t[0] < 30 and i1+t[0] >= 0 and i2+t[1] < 16 and i2+t[1] >= 0:
        if g[i1][i2] != None and g[i1+t[0]][i2+t[1]] != None:
            if g[i1][i2][0] == "bloc" and g[i1+t[0]][i2+t[1]][0] == "obs":
                obs1 = l1[g[i1][i2][1]]
                obs2 = l2[g[i1+t[0]][i2+t[1]][1]]
                for regle1 in l:
                    if regle1 == "text is weak" and not pushable(obs2, l):
                            return True
    return False

def check_deplacement(t, l, l1, l2, g, liste_obj):
    actu = False
    liste_you = []
    for regle in l:
        if regle.endswith("is you"):
            liste_you.append(regle[:-7])
    for obstacle in l2:
        if obstacle.mot in liste_you and obstacle.position[0]+t[0] < 30 and obstacle.position[0]+t[0] >= 0 and obstacle.position[1]+t[1] < 16 and obstacle.position[1]+t[1] >= 0:
            if g[obstacle.position[0]+t[0]][obstacle.position[1]+t[1]] == None:
                obstacle.set((obstacle.position[0]+t[0],obstacle.position[1]+t[1]))
                actu = True
            elif prochain_bloc_mort(g[obstacle.position[0]+t[0]][obstacle.position[1]+t[1]], l, l2):
                l2[g[obstacle.position[0]][obstacle.position[1]][1]].set((-1,-1))
                actu = True
            elif prochain_bloc_win(g[obstacle.position[0]+t[0]][obstacle.position[1]+t[1]], l, l2):
                l2[g[obstacle.position[0]][obstacle.position[1]][1]].set((-1,-1))
                actu = True
                C.create_image(0,0, anchor = NW, image = image_victory)
            else:
                ind1, ind2 = obstacle.position
                liste_apres = []
                while ind1 < 30 and ind1 >= 0 and ind2 < 16 and ind2 >= 0 and g[ind1][ind2] != None and not condition_open_shut(g, l, l2, ind1, ind2, t) and not condition_weak(g, l, l2, ind1, ind2, t) and not condition_melt_hot(g, l, l2, ind1, ind2, t) and not condition_weak_text(g, l, l1, l2, ind1, ind2, t):
                    liste_apres.append((ind1,ind2))
                    ind1 += t[0]
                    ind2 += t[1]
                if condition_open_shut(g, l, l2, ind1, ind2, t) or condition_weak(g, l, l2, ind1, ind2, t) or condition_melt_hot(g, l, l2, ind1, ind2, t) or condition_weak_text(g, l, l1, l2, ind1, ind2, t):
                    liste_apres.append((ind1,ind2))
                if ind1 < 30 and ind1 >= 0 and ind2 < 16 and ind2 >= 0:
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
                                if element[0] == "obs" and ((not l2[element[1]].mot in liste_you) or l2[element[1]] == obstacle):
                                    if condition_open_shut(g, l, l2, ind1, ind2, t):
                                        l2[g[ind1+t[0]][ind2+t[1]][1]].position = (-1,-1)
                                        l2[g[ind1][ind2][1]].position = (-1,-1)
                                    elif condition_weak(g, l, l2, ind1, ind2, t):
                                        l2[g[ind1][ind2][1]].position = (-1,-1)
                                    elif condition_melt_hot(g, l, l2, ind1, ind2, t):
                                        a1, a2 = indice_melt_hot(g, l, l2, ind1, ind2, t)
                                        l2[g[a1][a2][1]].position = (-1,-1)
                                        if a1 != ind1 or a2 != ind2:
                                            l2[element[1]].set((l2[element[1]].position[0]+t[0],l2[element[1]].position[1]+t[1]))
                                    else:
                                        l2[element[1]].set((l2[element[1]].position[0]+t[0],l2[element[1]].position[1]+t[1]))
                                if element[0] == "bloc":
                                    if condition_weak_text(g, l, l1, l2, ind1, ind2, t):
                                        l1[g[ind1][ind2][1]].position = (-1,-1)
                                    else:
                                        l1[element[1]].set((l1[element[1]].position[0]+t[0],l1[element[1]].position[1]+t[1]))
                        actu = True
    if actu:
        liste_obj.append((copy_blocs(l1), copy_obstacles(l2)))
        return 1
    return 0



def checker_regles(l):
    regle_you = []
    for regle in l:
        if regle.endswith("is you"):
            regle_you.append(regle[:-7])
    if regle_you == []:
        return False
    if "bad champi is stop" in l:
        C.create_image(0,0, anchor = NW, image = image_victory)
        return False
    if "grass is greener" in l:
        C.create_image(0,0, anchor = NW, image = image_DUH)
        return False
    return True

