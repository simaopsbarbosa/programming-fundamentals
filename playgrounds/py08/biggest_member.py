def biggest_member(atuple):
    bigger = atuple
    
    for element in atuple:
        if type(element) == tuple:
            atuple2 = biggest_member(element)
            if len(atuple2) > len(bigger):
                bigger = atuple2

    return bigger