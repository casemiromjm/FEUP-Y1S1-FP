import math

def solver(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return []
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    if x1 == x2:
        return [x1]
    else:
        solution = [x1,x2]
        solution.sort()
        return solution