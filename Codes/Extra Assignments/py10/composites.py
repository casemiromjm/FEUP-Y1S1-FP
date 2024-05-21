def prime(num:int):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_composites(n:int):
    # n is the upper bound of the interval [4, n]

    # if a num is not prime, it must be composite

    return (x for x in range(4, n+1) if not prime(x))