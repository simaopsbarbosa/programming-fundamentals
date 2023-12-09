def pjthagoreans(a:int,b:int): # returns list
    return [(i, j, z) for i in range(a,b) for j in range(a,b) for z in range(a,b) if i**2 + j**2 == z**2 and i < j and j< z]
    