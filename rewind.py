from __init__ import *
exec(open("__init__.py").read())

def copy_blocs(l):
    return [bloc.copy() for bloc in l]

def copy_obstacles(l):
    return [obs.copy() for obs in l]

def rewind(liste_obj, l1, l2):
    if len(liste_obj)>1:
        n = len(liste_obj)-1
        del liste_obj[n]
    return copy_blocs(liste_liste_objets[-1][0]), copy_obstacles(liste_liste_objets[-1][1])
