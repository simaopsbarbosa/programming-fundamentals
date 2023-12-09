def gcd_rec(n1,n2):
    
    # stopping condition
    if n2 == 0:
        return n1
    
    # next cycle
    resto = n1 % n2
    return gcd_rec(n2, resto)
    
print(gcd_rec(48,18))
    
    