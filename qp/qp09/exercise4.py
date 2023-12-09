import functools
def dec2int(alist:list):
    return functools.reduce(lambda x,y: x*10+y, alist)