n = int(input())

sum_divisor = 0
while n > 1:
    if n % 3 == 0 or n % 5 == 0:
        sum_divisor = sum_divisor + n
    n = n - 1

print(sum_divisor)