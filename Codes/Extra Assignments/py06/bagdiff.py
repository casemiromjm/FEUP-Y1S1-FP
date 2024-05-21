def bagdiff(xs, ys):
    for i in range(len(ys)):
        if ys[i] in xs:
            xs.remove(int(ys[i]))
    return xs