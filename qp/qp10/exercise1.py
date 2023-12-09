def square_odds(values:str): # returns string
    list = values.split(",")
    res = [int(i)**2 for i in list if int(i) % 2 != 0]
    return ",".join(str(v) for v in res)