def to_celsius(t:list):                         # map version
    # t is a list of temperatures in fahrenheint and it has to be converted to celsius

    return list(map(lambda temp: round(((temp - 32) * 5/9), 1), t) )