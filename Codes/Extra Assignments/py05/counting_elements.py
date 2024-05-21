def count_until(tup):
    if tup == ():
        return -1
    
    nonTupCounter = 0
    for index, i in enumerate(tup):
        if type(i) == tuple:
            return index
        else:
            nonTupCounter += 1
        if nonTupCounter != 0 and index == len(tup) -1:
            return -1