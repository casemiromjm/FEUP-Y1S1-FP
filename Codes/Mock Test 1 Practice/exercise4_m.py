def sum_proper_divisors(number):
    sum_proper_divisors = 0
    for divisor in range(1, number+1):
        if number % divisor == 0 and divisor < number:
            sum_proper_divisors = sum_proper_divisors + divisor
                
    return sum_proper_divisors

def check_friendly(number_one, number_two):
    divisors_number_one = sum_proper_divisors(number_one)
    divisors_number_two = sum_proper_divisors(number_two)
    if divisors_number_one == number_two and divisors_number_two == number_one:
        return f"{number_one} and {number_two} are friendly"
    elif number_one == number_two:
        return f"identical numbers: {number_one}"
    elif divisors_number_one != number_two:
        return f"sum of divisors of {number_one} is not {number_two}"
    elif divisors_number_two != number_one:
        return f"sum of divisors of {number_two} is not {number_one}"