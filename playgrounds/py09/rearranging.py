def rearrange(l: list): # return list
    return [x for x in l if x<=0] + [x for x in l if x>0]
    