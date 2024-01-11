def reciprocals(alist):
    res = []
    for num in alist:
        try:
            1 / num
        except:
            continue
        else:
            res.append(1/num)
             
    return res