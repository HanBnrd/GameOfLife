# -*- coding: utf-8 -*-
"""
Classe contenant les règles du jeu de la vie
"""

import itertools
import numpy as np

class Rules:

    def __init__(self,h=4,w=4):
        self.height=h # hauteur grille
        self.width=w # largeur grille


    def allDead(self):
        """
        Fonction retournant l'état tout mort pour une grille h*w
        """
        return np.zeros((self.height,self.width)) # matrix h*w of zeros

    def isDead(self,state):
        return np.array_equal(state,self.allDead())

    def getAll(self):
        """
        Fonction retournant une liste de tous les états possibles
        pour une grille h*w
        """
        allStates=[]
        # Generate all the combinations as string tuples of length h*w
        seq = itertools.product((True,False), repeat=self.height*self.width)
        for s in seq:
            # Convert to numpy array and reshape to h*w
            arr = np.fromiter(s, np.int8).reshape(self.height,self.width)
            allStates.append(arr)
        return allStates

    def neighbors(self,h,w):
    	"""
    	Returns an array of tuples with all neighbors of the given cell
    	"""
    	return [
    	    (h-1 if h-1 >= 0 else self.height-1, w-1 if w-1 >= 0 else self.width-1),
    	    (h-1 if h-1 >= 0 else self.height-1, w),
    	    (h-1 if h-1 >= 0 else self.height-1, w+1 if w+1 < self.width else 0),
    	    (h+1 if h+1 < self.height else 0, w-1 if w-1 >= 0 else self.width-1),
    	    (h+1 if h+1 < self.height else 0, w),
    	    (h+1 if h+1 < self.height else 0, w+1 if w+1 < self.width else 0),
    	    (h, w-1 if w-1 >= 0 else self.width-1),
    	    (h, w+1 if w+1 < self.width else 0),
    	]

    def next(self,state):
        """
        Fonction retournant l'état successeur de state avec les règles de Conway
        """
        nextState=state.copy()
        for h in range(len(state)):
            for w in range(len(state[h])):
                # Get all the neighbors
                valsOfNeighbors = []
                for neighbor in self.neighbors(h,w):
                    valsOfNeighbors.append(state[neighbor])
                # Live square dies if it has > 3 or < 2 live neighbors
                if state[h][w] == 1 and (valsOfNeighbors.count(1) > 3 or valsOfNeighbors.count(1) < 2):
                    nextState[h][w] = 0
                # Empty square comes to life if it has three live neighbors
                elif state[h][w] == 0 and valsOfNeighbors.count(1) == 3:
                    nextState[h][w] = 1
                elif state[h][w] != 1 and state[h][w] != 0:
                    raise Exception('Grid can only contain 0 or 1')
                # # Cell is alive if 3 or 4 neighbors
                # if valsOfNeighbors.count(1) == 3 or valsOfNeighbors.count(1) == 4:
                #     nextState[h][w] = 1
                # # Cell is dead otherwise
                # else:
                #     nextState[h][w] = 0
        return nextState
