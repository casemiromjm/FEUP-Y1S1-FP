def comprehensions(i, j):
    list_3or8 = [n for n in range(i, j+1) if n % 10 in (3,8)] #list of numbers in interval [i,j] that ends in 3 or 8
    tuple_sqrRoot = tuple(map(lambda x: round(x, 2), map(lambda x: x**0.5, range(i,j+1)))) #tuple with the square root, rounded to 2 decimals, of numbers in that interval
    dict_ascii = {n:chr(n) for n in range(i, j+1)} #A dictionary where the key is a number and the value is the corresponding character from the ASCII table, of numbers in that interval.

    return list_3or8, tuple_sqrRoot, dict_ascii