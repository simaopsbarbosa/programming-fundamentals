def max_path(tree):
    
    #check if int
    if type(tree) == int:
        return tree
        
    
    left = tree[0]
    right = tree[2]
    value = tree[1]
    
    maior = max(max_path(left), max_path(right))
    
    return value + maior
    
