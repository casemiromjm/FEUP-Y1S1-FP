def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    for div in range(2, number):
        if number % div == 0:
            return False
    return True

def next_prime(number):
    number = number + 1
    while True:
        if is_prime(number):
            return number
        number = number + 1