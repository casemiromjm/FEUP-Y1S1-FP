lower = int(input())
upper = int(input())

def is_prime(num):
    if num <= 1:
        return False
    
    for div in range(2, num):
        if num % div == 0:
            return False
    
    return True

primes = []

for num in range(lower, upper + 1):
    if is_prime(num):
        primes.append(str(num))

print(f"Prime numbers between {lower} and {upper} are: {' '.join(primes)}")