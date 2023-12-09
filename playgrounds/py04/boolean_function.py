def validate(grade):
    while type(grade) != int and type(grade) != float:
        return False
    return (0 <= float(grade) <= 100)