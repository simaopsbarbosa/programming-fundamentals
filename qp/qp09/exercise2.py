def variance(alist:list): # returns float
    return round(sum(list(map(lambda x : (x - sum(alist) / len(alist)) ** 2, alist))) / len(alist), 3)
