import math

def digits_average(n):
    n_str = str(n)

    digits = []
    for d in n_str:
        digits.append(d)

    while len(digits) > 1:
        pairs = zip(digits, digits[1:])
        digits = list(map(lambda pair: math.ceil((int(pair[0]) + int(pair[1]))/2), pairs))

    return digits[0]