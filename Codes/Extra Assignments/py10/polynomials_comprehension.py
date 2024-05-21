def evaluate(a:list, x:int):
    return sum([ coef*(x**i) for i, coef in enumerate(a) ])