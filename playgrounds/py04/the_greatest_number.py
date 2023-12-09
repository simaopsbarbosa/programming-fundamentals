def greatest(num):
    res = [int(x) for x in str(num)]
    res.sort(reverse=True)
    number = 0
    for i in res:
        number = number * 10 + i
    return number