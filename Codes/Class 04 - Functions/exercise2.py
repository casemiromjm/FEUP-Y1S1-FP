def adigits(a, b, c):
    hundred = min(a,b,c)
    unit = max(a,b,c)
    tens = (a+b+c) - (hundred + unit)
    num = 100*hundred + 10*tens + unit
    return num