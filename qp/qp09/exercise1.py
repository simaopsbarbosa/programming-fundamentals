def differences(alist: list): # returns list
    return list(map(lambda p : p[1] - p[0], list(zip(alist, alist[1:]))))
