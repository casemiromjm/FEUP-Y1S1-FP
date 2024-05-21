def to_fahrenheit(t:list):                  #map version
    # t is a list of temperatures in fahrenheint and it has to be converted to celsius

    return list(map(lambda temp: round( (temp * (9/5)) + 32, 2), t) )