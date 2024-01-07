def evaluate(a: list,x:int):
    res = [n * (x** a.index(n)) for n in a]
    return sum(res)