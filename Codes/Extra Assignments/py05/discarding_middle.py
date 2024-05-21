def discard_middle(s):
    stringLength = len(s)

    if stringLength <= 3:
        return ""
    
    newString = s[0] + s[1] + s[stringLength - 2] + s[stringLength - 1]
    return newString