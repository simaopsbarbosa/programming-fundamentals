def evaluate(a: list,x: int): #returns integer
    return sum(list(map(lambda i: i * (x ** a.index(i)), a)))
    
    