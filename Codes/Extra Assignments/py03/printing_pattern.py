n = int(input())
saved_n = n
rep = n

while rep > 0:
    for i in range(1,n+1):
        print(n, end=" ")
        n = n - 1
        i = i + 1
        if n == 0:
            print("")
    i = 1
    n = saved_n - 1
    rep = rep - 1
    saved_n = n