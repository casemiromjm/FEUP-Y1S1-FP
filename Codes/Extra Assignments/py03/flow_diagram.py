l = int(input())
s = int(input())

r = l

if r > s:
    pass
else:
    l = r
    r = s
    s = l

if s > r:
    pass
else:
    while s <= r:
        r = r - s

if r == 0:
    print(s)
else:
    while r != 0:
        l = r
        r = s
        s = l
        while s <= r:
             r = r - s
    print(s)