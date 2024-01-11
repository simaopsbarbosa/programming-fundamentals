def count_exceptions(f, n1, n2):
    counter = 0
    for x in range(n1,n2+1):
        try:
            f(x)
        except:
            counter += 1
    return coutner