from functools import *

def map_filter_reduce(lst,f1,f2,f3): # returns int
    return reduce(f3, map(f2,filter(f1, lst)))
    
    