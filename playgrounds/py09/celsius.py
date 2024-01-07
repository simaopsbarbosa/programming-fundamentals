def to_celsius(t): # returns list
    return list(map(lambda x: round((x - 32) / 1.8, 1), t))   
