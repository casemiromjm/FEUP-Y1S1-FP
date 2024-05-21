num1 = int(input())
num2 = int(input())
mixed_num = 0

while num1 > 0 and num2 > 0:
    last_digit1 = num1 % 10
    last_digit2 = num2 % 10
    mixed_num = mixed_num*10 + last_digit1
    mixed_num = mixed_num*10 + last_digit2
    num1 = num1 // 10
    num2 = num2 // 10

print(mixed_num)