import math

def pascal(n):
    row = ""
    for line in range(0, n):
        for column in range(0, line +1):
            value = math.factorial(line)/(math.factorial(column)*math.factorial(line-column))
            value = int(value)
            if line == column:
                value = str(value) + "\n"
            else:
                value = str(value) + " "
            row = row + value
    return row