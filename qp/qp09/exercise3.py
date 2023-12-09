def x_union(list1, list2): # returns list 
    map1 = tuple(map(lambda x: x[0], list1))
    map2 = tuple(map(lambda x: x[0], list2))
    res = list(filter(lambda x: x[0] not in map2, list1)) + list(filter(lambda x: x[0] not in map1, list2))
    return res