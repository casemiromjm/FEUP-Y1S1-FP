import functools

def bounding_box(pts):
    x_max = functools.reduce(lambda x1,x2: x1 if x1 >= x2 else x2 , map(lambda pair: pair[0], pts))
    x_min = functools.reduce(lambda x1,x2: x1 if x1 < x2 else x2 , map(lambda pair: pair[0], pts))
    y_max = functools.reduce(lambda y1,y2: y1 if y1 >= y2 else y2 , map(lambda pair: pair[1], pts))
    y_min = functools.reduce(lambda y1,y2: y1 if y1 < y2 else y2 , map(lambda pair: pair[1], pts))

    return (x_min, y_min, x_max, y_max)