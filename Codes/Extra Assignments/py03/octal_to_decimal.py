num_octal = int(input())

valid_number = True
n = 0
num_decimal = 0

while num_octal > 0:
    algarism_octal = num_octal % 10
    if algarism_octal > 7:
        valid_number = False
        break
    num_octal = num_octal // 10
    algarism_decimal = (8 ** n)*algarism_octal
    num_decimal = num_decimal + algarism_decimal
    n = n + 1

if valid_number:
    print(num_decimal)
else:
    print("Not a valid number.")