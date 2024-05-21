def to_fahrenheit_comprehension(t:list):
    return [ round( (temp * (9/5)) + 32, 2) for temp in t ]