import math

def juggler(n,p):
    if p == 0:
        return n
    else:
        if juggler(n,p-1) % 2 == 0:
            return math.floor((juggler(n,p-1)**(1/2)))
        else:
            return math.floor((juggler(n,p-1)**(3/2)))