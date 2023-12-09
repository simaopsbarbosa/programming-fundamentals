import math

def solver(a,b,c):
    binomio = (b ** 2) - 4 * a * c
    # casos possiveis
    #  a == 0
    # impossivel --> sqrt < 0 
    #  1 sol --> sqrt == 0
    #  2 sol

    if a == 0:
        res = (c * (-1)) / b
    elif binomio < 0:
        res = []
    elif binomio == 0:
        res = [(-b + math.sqrt(binomio)) / (2*a)]
    else: 
        solution1 = (-b + math.sqrt(binomio)) / (2*a)
        solution2 = (-b - math.sqrt(binomio)) / (2*a)
        res = [solution1, solution2]
        res.sort()

    return res