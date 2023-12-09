def fib(n): # returns list
    list = []
    for i in range(n):
        if i == 0:
            list.append(0)
        elif i == 1:
            list.append(1)
        else:
            list.append(list[-1] + list[-2])
            
    return list