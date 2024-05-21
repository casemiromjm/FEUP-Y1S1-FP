def count_connections(a,b,g):
    counter = 0
    for x,y in g:
        if a == x and b == y:
            counter += 1
    return counter

def multi(g):
    triplet = ()
    for a,b in g:
        connections = count_connections(a,b,g)
        if (a, connections, b) not in triplet:
            triplet = triplet + ((a, connections,b),)
    return triplet