def lost_element(s1, s2):
    if len(s1) >= len(s2):
        missing_element = s1 - s2
    else:
        missing_element = s2 - s1

    return missing_element.pop()