num = int(input())
divisor = 1
sum = 0

def divisor_check():
    if num % divisor == 0:
        return divisor
    else:
        return 0

while divisor <= num:
    sum = divisor_check() + sum
    divisor = divisor + 1

print(sum)