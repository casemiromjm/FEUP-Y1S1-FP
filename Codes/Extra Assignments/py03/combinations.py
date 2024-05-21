def factorial(value):
    fact = 1
    while value > 1:
        fact = fact * value
        value = value - 1
    return fact

def C(n, r):
    combination = (factorial(n))/(factorial(r) * (factorial(n-r)))
    return int(combination)