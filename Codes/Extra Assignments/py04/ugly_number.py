def ugly(n):
    while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        if n % 2 == 0:
            n = n // 2
        elif n % 3 == 0:
            n = n // 3
        elif n % 5 == 0:
            n = n // 5
    if n == 1:
        return True
    else:
        return False