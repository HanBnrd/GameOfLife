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
result=[] # liste des états menant à tout mort
for state in r.getAll():
    end=False
    temp=state
    visited=[] # liste des états visités
    while not end:
        if np.array_equal(temp,r.allDead()):
            result.append(state)
            end=True
        elif any((temp==x).all() for x in visited):
            end=True
        else:
            visited.append(temp)
            temp=r.next(temp)
print("Proportion d'états menant à tout mort :")
print(len(result),"/",2**(int(height)*int(width)))
print("--- %s seconds ---" % (time.time() - start_time))
