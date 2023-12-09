# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 21:03:10 2023

@author: simao
"""

def deriv(f):
    def df(x):
        return round((f(x + 0.001) - f(x)) / 0.001 , 3)
    return df