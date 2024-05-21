n = float(input())
precision = 1e-6

up_limit = n
down_limit = 0

midpoint = (up_limit + down_limit)/2

while up_limit - down_limit > precision:
    solution = midpoint * midpoint
    if solution == n:
        break
    elif solution < n:
        down_limit = midpoint
    else:
        up_limit = midpoint
    midpoint = (up_limit + down_limit)/2

print(round(midpoint, 5))