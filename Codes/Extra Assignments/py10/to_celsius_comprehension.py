def to_celsius_comprehension(t:list):                         # comprehension version
    # t is a list of temperatures in fahrenheint and it has to be converted to celsius

    return [ round(((temp - 32) * 5/9), 1) for temp in t ]