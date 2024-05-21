def local_minima(alist):
    minimums = []
    for i in range(len(alist) - 2):
        sublist = alist.copy()
        sublist = sublist[i:i+3]
        mininum = min(sublist)
        if sublist.count(mininum) == 1:
            minimums.append(mininum)
    return minimums