def division(a,b: int): 
    if b == 0:
        return "can't divide by 0!"
    
    try:
        a/b
    except:
        return "unsupported operand type(s) for division"
    else: 
        return f"{a}/{b} = {round(a/b, 1)}"