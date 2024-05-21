def switch_dict(adict):
    newDict = {}
    for key,value in adict.items():
        if value not in newDict:
            newDict[value] = [key]
        else:
            newDict[value].append(key)
    
    return newDict