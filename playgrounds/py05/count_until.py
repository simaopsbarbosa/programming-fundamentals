def count_until(tup): # return int
    for i in range(len(tup)):
        if type(tup[i]) == tuple:
            return i
    
    return -1