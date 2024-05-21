def sum_numbers(number):
    acc = 0
    for i in range(1, number+1):
        acc = acc + i
    return acc

def var_numbers(number, precision = 2):
    average = sum_numbers(number) / number
    somatory = 0
    for i in range(1, number + 1):
        sqr = (i - average)**2
        somatory = somatory + sqr 
    var = somatory / number
    var = round(var, precision)
    return var