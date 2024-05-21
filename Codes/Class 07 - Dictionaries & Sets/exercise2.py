def roman_to_integer(astring):
    romansDecimal = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}    
    decimal = 0

    for i,roman in enumerate(astring):
        if i< (len(astring) - 1) and romansDecimal[astring[i+1]] > romansDecimal[roman]:
            decimal -= romansDecimal[roman]
        else:
            decimal += romansDecimal[roman]

    return decimal