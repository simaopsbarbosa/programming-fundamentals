def to_fahrenheit(t): # returns list
    return list(map(lambda x: round((9/5) * x + 32, 2), t))  