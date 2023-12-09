def juggler(n,p):
    
    # base case
    if p == 0:
        return n
    
    # prior term
    p = juggler(n, p-1)
    
    
    # next term
    if p % 2 == 0:
        return int(p ** (1/2))
    else:
        return int(p ** (3/2))
    
print(juggler(3, 3))