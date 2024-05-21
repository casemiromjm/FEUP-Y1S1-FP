def generator(intlist:list):
    return (num for start, end in intlist for num in range(start, end+1))


print(generator([(1, 1), (3, 5), (10, 15)]))
print(generator([(0, 5), (10, 15), (100, 102)]))
print(generator([(0, 0), (2, 2)]))
print(generator([(-10, -5), (2, 10), (70, 72), (102, 105)]))