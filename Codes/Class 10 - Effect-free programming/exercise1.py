def square_odds(values):
    #return ",".join([str(int(n)**2) for n in values.split(",") if int(n)%2 != 0])
    values_list = values.split(",")
    squares = [int(n)**2 for n in values_list if int(n)%2 != 0]

    return ",".join(str(i) for i in squares)