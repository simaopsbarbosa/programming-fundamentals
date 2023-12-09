import math

def comprehensions(i:int ,j:int): # returns tuple
    list1 = [i for i in range(i,j+1) if str(i)[-1] == "3" or str(i)[-1] == "8"]
    tuple1 = tuple(round(math.sqrt(i),2) for i in range(i,j+1))
    asciiDict = {i: chr(i) for i in range(128)}
    dict1 = {i: asciiDict.get(i) for i in range(i, j+1)}
    return (list1 ,tuple1 , dict1)