def repeated_letter(s):
    letters = []
    for i in s:
        if s.count(i) > 1:
            letters.append(i)
        if letters.count(i) > 1:
            letters.remove(i)

    if not letters:
            return None
    
    letters.reverse()
    indexes = []
    for j in range(len(letters)):
        index = letters.index(letters[j])
        indexes.append(index)
    
    return letters[min(indexes)]

print(repeated_letter("tweet"))