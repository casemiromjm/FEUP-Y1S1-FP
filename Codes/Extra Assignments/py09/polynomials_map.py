def evaluate(a, x):
    indexes = [ i for i in range(len(a)) ]

    return sum(map(lambda i, coef: coef*(x**i), indexes, a))

#podia usar .index ou usar enumerate e usar tuplo