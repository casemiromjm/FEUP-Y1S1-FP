def individual_digits(number):
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number = number // 10
    return digits

def validate_cc(number):
    card_digits = individual_digits(number)
    for i in range(0, len(card_digits)):
        if i % 2 == 0:
            card_digits[i] = card_digits[i] * 2
        else:
            card_digits[i] = card_digits[i]
    card_digits2 = individual_digits(card_digits)
    
    sum_digits = sum(card_digits2)
    return sum_digits

print(validate_cc(4028743156781887))

# NÃO ESTÁ FUNCIONANDO