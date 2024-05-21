""" calculate the amount of money that will be available after a certain period of time """

P = int(input())
""" P is the principal amount """

r = float(input())
""" r is the annual interest rate """

n = int(input())
""" n is the number of times that interest is compounded per year """

t = 2
""" t is the number of years the money is invested for """

A = P*((1 + r/n)**(n*t))
A = round(A,3)

print(A)