def rotate_list(l):
    l_copy = l.copy()
    for i in range(len(l)):
        l_copy[i-3] = l[i]
    return l_copy