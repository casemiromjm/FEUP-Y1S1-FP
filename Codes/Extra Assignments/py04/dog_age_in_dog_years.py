def dogs(h_age):
    if 1 <= h_age <= 2:
        d_age = h_age * 10.5
    else:
        d_age = (2 * 10.5) + ((h_age - 2) * 4)
    return d_age