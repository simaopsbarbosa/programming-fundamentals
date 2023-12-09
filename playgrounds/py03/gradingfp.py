# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:25:02 2023

@author: simao
"""

import math

def round_half_up(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n * multiplier + 0.5) / multiplier

LE = int(input())
RE = int(input())
PE = int(input())
TE = int(input())

grade = round_half_up((LE + RE + 13 * PE + 5 * TE) / 100)

if LE < 0 or LE > 100 or RE < 0 or RE > 100 or PE < 0 or PE > 100 or TE < 0 or TE > 100:
    print("Input error")
elif PE < 40 or TE < 40:
    print("RFF")
else:
    print(int(grade))