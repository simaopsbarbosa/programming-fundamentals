def permutations(string:str) -> list:
    
    if len(string) <2 : return [string]
    res = []
    
    for i,letter in enumerate(string):   
                              
        l_less = string[:i] + string[i+1:]              
        permuts = permutations(l_less)
          
        for p in permuts:
            res.append(letter + p)     

    return res