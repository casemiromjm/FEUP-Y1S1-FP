def reciprocals(alist:list):
    # reciprocal of n is 1/n

    reciprocal = []

    for i in alist:
        try:
            r = 1 / i
        except:
            pass
        else:
            reciprocal.append(r)
    
    return reciprocal