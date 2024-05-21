def deriv(f):
    h = 0.001
    def df(x):
        value = (f(x+h)-f(x))/h
        value = round(value,3)
        return value
    return df