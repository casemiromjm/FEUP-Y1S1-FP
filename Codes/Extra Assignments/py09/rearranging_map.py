def rearrange(l:list):
    non_po = list( filter(lambda x: x <= 0, l) )
    po = list( filter(lambda x: x > 0, l) )

    return non_po + po