
def find_me(f, limits:tuple, iter=0): # returns int

    # 1 ---> bigger
    # -1 ---> smaller
    # 0 ---> found
    
    middle = (limits[0] + limits[1]) // 2
    value = f(middle)

    if value < 0:
        limits = (limits[0], middle -1)
    elif value > 0:
        limits = (middle + 1, limits[1])
    elif value == 0:
        return iter + 1
    iter += 1
    return find_me(f,limits, iter)