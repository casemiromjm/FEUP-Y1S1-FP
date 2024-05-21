import math

def approx_cos(x, n):
    somatory = 0
    for i in range(0, n):
        approx = (((-1)**i)  / (math.factorial(2*i))) * (x**(2*i))
        somatory = somatory + approx
    
    return round(somatory, 5)