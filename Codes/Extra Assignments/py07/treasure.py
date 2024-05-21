def treasure(clues):
    pos = (0,0)
    while pos in clues:
        key = pos
        pos = clues[pos]
        del clues[key]
    return pos

print(treasure({(0, 0): (1, 0), (2, 1): (3, 5), (1, 0): (2, 1)}))