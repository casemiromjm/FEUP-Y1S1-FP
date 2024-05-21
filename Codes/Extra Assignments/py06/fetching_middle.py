def fetch_middle(llist):
    centralElements = []
    for i in llist:
        if len(i) % 2 != 0:
            centralElements.append(i[len(i) // 2])
        else:
            centralElements.append((i[len(i)//2 - 1] + i[len(i)//2])/2)

    return centralElements