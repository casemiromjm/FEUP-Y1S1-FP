num = int(input())
index = 1

def power():
    if num == index:
        print("%d ^ 2 == ")

for index in range(1, 11):
    res = num * index
    if num == index:
        print("%d ^ 2 = %d" % (num, res))
        break
    else:    
        print(f"{num} x {index} = {res}" )
    index = index + 1