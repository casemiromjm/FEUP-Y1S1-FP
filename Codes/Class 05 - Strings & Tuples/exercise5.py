def triplet(tup):
    i = tup
    for w in range (len(i)):
            num1 = i[w]
            for x in range(len(i)):                
                num2 = i[x]
                for y in range(x, len(i)):
                    num3 = i[y]
                    if (num1 + num2 + num3) == 0 and w != x and w != y and x!= y:
                        return (num1, num2, num3)
    return ()


