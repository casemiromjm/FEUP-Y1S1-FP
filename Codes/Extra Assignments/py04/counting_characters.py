def count_chars(string, character):
    counter = 0
    for char in string:
        if char == character:
            counter = counter + 1
    if counter > 0:
        return counter
    else:
        return -1