def sum_digits_rec(n):
    
    # stopping condition
    if len(str(n)) == 1:
        return int(n)
    
    # next term
    return int(str(n)[len(str(n)) - 1]) + sum_digits_rec(str(n)[:-1]) 
    
print(sum_digits_rec(100))