n = int(input())

decomp1000 = (n // 1000)*1000
print(decomp1000)

n = n - decomp1000

decomp100 = (n // 100)*100
print(decomp100)

n = n - decomp100

decomp10 = (n // 10)*10
print(decomp10)

n = n - decomp10

decomp1 = n // 1
print(decomp1)