def map(pos, steps):
    movesList = steps.split("-")
    for move in movesList:
        if move == "up":
            pos = (pos[0], pos[1] + 1)
        elif move == "down":
            pos = (pos[0], pos[1] - 1)
        elif move == "left":
            pos = (pos[0] - 1, pos[1])
        else:
            pos = (pos[0] + 1, pos[1])
    return pos