import functools
def bounding_box(pts:list) -> tuple:
    x = list(map(lambda x: x[0], pts))
    y = list(map(lambda y: y[1], pts))
    return (functools.reduce(lambda i,j: i if i<j else j, x), functools.reduce(lambda i,j: i if i<j else j, y),functools.reduce(lambda i,j: i if i>j else j, x),functools.reduce(lambda i,j: i if i>j else j, y))