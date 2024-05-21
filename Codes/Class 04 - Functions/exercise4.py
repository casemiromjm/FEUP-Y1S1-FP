def mastermind(g1,g2,g3,c1,c2,c3):
    points = 0
    if g1 == c1:
        points += 3
        g1 = "g"
        c1 = "c"
    if g2 == c2:
        points += 3
        g2 = "g"
        c2 = "c"
    if g3 == c3:
        points += 3
        g2 = "g"
        c2 = "c"
    if g1 == c2 or g1 == c3:
        points += 1
        g1 = "g"
        c2 = "c"
        c3 = "c"
    if g2 == c1 or g2 == c3:
        points += 1
        g2 = "g"
        c1 = "c"
        c3 = "c"
    if g3 == c1 or g3 == c2:
        points += 1
        g3 = "g"
        c1 = "c"
        c2 = "c"
    return points