import functools

def dec2int(alist):
    alist = [0] + alist
    num = functools.reduce(lambda n, d: n*10 + d, alist)
    return num