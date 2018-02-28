# -*- coding: utf-8 -*-
"""
Obtenir les états menant à tout mort et executant le jeu de la vie sur chaque
état et en checkant si l'état va mener à tout mort
"""

import rules as rl
import numpy as np
import time

print("[Forward]")
height=input("Hauteur de la grille : ")
width=input("Largeur de la grille : ")
print("*****")
start_time = time.time()
r=rl.Rules(int(height),int(width)) # création d'un objet Rules
dead=[r.allDead()] # liste des états menant à tout mort
alive=[]
for cpt in range(2**(int(height)*int(width))): # génération des états au fur et à mesure
    end=False
    binCpt = bin(cpt) # conversion en binaire
    binCpt=binCpt[2:] # retrait de l'indicateur binaire
    while len(binCpt)<(int(height)*int(width)): # ajout de 0 à gauche
        binCpt='0'+binCpt
    state = np.fromiter(binCpt, np.int8).reshape(int(height),int(width)) # création matrice
    visited=[] # liste des états visités
    while not end:
        if any((state==x).all() for x in dead):
            dead+=visited
            end=True
        elif any((state==x).all() for x in (visited or alive)):
            alive+=visited
            end=True
        else:
            visited.append(state)
            state=r.next(state)
print("Proportion d'états menant à tout mort :")
print(len(dead),"/",2**(int(height)*int(width)))
print("--- %s seconds ---" % (time.time() - start_time))
