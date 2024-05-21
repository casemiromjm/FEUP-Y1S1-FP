def bisect(f, n):
    lower, upper = 0, 1

    for _ in range(n): # repeticoes ja definidas
        mid = (lower + upper) / 2
        if (f(lower) < 0 and f(mid) < 0) or (f(lower) > 0 and f(mid) > 0): # f(lower)*f(mid) > 0
            lower = mid
        else:
            upper = mid

    return round(mid, 5)