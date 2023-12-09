# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:41:46 2023

@author: simao
"""

import math

def round_half_up(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n * multiplier + 0.5) / multiplier

print(round_half_up(16.4))