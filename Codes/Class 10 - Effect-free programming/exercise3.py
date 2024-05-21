def pythagoreans(a,b):
    triples = [(x, y, z) for x in range(a, b) for y in range(x, b) for z in range(y, b) if x*x + y*y == z*z]
    return triples