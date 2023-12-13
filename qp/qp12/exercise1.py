import itertools


def collision(obj1: dict, obj2: dict):  # returns bool if colliding
    '''
    aux function that checks if 2 objects are NOT colliding
    '''

    x_col = (obj2.get('x1') < obj1.get('x1') and obj2.get('x2') < obj1.get('x1')) or (
        obj2.get('x1') > obj1.get('x2') and obj2.get('x2') > obj1.get('x2'))  # true if no collision

    y_col = (obj2.get('y1') < obj1.get('y1') and obj2.get('y2') < obj1.get('y1')) or (
        obj2.get('y1') > obj1.get('y2') and obj2.get('y2') > obj1.get('y2'))  # true if no collision

    if not x_col and not y_col:
        return True  # collision
    else:
        return False  # no collision


def number_of_collisions(objects: list):  # returns int (number of collisions)
    '''
    checks collision between every pair of objects
    '''
    count = 0
    tuples = list(itertools.combinations(objects, 2))
    for i in range(len(tuples)):
        if collision(tuples[i][0], tuples[i][1]):
            count += 1

    return count
