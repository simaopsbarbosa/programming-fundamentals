# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:29:06 2023

@author: simao
"""

def mastermind(g1, g2, g3, c1, c2, c3):

    points = 0
    
    if g1 == c1:
        points += 3
    elif (g1 == c2 or g1 == c3) and g1 != g2 != g3:
        points += 1
    if g2 == c2:
        points += 3
    elif (g2 == c1 or g2 == c3 )and g2 != g3:
        points += 1
    if g3 == c3:
        points += 3
    elif g3 == c1 or g3 == c2:
        points += 1
    return(points)
