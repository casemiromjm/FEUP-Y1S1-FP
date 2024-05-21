import math
k = 0
somatory = 0

constant_factor = math.sqrt(8)/9801

for k in range(0,51):
    somatory_expression_num = (math.factorial(4*k)*(1103 + 26390*k))
    somatory_expression_den = ((math.factorial(k)**4)*(396**(4*k)))
    somatory_expression = somatory_expression_num / somatory_expression_den
    somatory = somatory + somatory_expression

pi_large = somatory * constant_factor
pi = 1 / pi_large

pi = round(pi,8)
print(pi)