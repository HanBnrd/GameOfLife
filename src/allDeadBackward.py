# -*- coding: utf-8 -*-
"""
Obtenir tous les états menant à tout mort en partant de l'état tout mort et
en remontant aux états qui mènent à cet état, et en remontant aux états qui
mènent à ces états ...
"""

import rules as rl
import time

print("[Backward]")
height=input("Hauteur de la grille : ")
width=input("Largeur de la grille : ")
print("*****")
start_time = time.time()
r=rl.Rules(int(height),int(width)) # création d'un objet Rules
end=False
result=[r.allDead()] # liste des états menant à tout mort initialisée avec tout mort
while not end:
    end=True
    for state in r.getAll():
        if any((state == x).all() for x in result):
            continue
        elif any((r.next(state) == x).all() for x in result):
            result.append(state)
            end=False
print("Proportion d'états menant à tout mort :")
print(len(result),"/",2**(int(height)*int(width)))
print("--- %s seconds ---" % (time.time() - start_time))
