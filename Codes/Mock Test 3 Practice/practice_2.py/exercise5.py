def generate(word:str):
    words = []
    #if it ends with I, it should append U to the string
    if word[-1] == "I":
        words.append(word + "U")

    #if it starts with M, it should double the string after M
    if word[0] == "M":
        words.append(word + word[1:])
    
    #replace III with U (all possibilities)
    for i in range(2, len(word)):
        if word[i-2:i+1] == "III":
            words.append(word[:i-2] + "U" + word[i+1:])
    
    #remove UU (all possibilities)
    for i in range(1, len(word)):
        if word[i-1:i+1] == "UU":
            words.append(word[:i-1] + word[i+1:])

    words.sort()

    return words

# print(generate('MUI'))
# print(generate('MUUI'))
# print(generate('MIIIU'))
# print(generate('MIIIUUIII'))