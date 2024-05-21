def collatz(n):
    sequence = f"{n}"
    while n != 1:
        if n % 2 == 0:
            term = int(n/2)
        else:
            term = (n*3) + 1
        n = term
        sequence = sequence + f",{term}"

    return sequence