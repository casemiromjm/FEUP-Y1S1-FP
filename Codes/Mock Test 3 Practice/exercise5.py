def generate(word:str):
    words_list = []

    if word.endswith("I"):
        words_list.append(word + "U")
    if word.startswith("M"):
        words_list.append(word + word[1:])
    if "III" in word:
        index_substring = word.find("III")
        while index_substring != -1:
            words_list.append(word[:index_substring] + "U" + word[index_substring + 3:])
            index_substring = word.find("III", index_substring +3)
    if "UU" in word:
        index_substring = word.find("UU")
        while index_substring != -1:
            words_list.append(word[:index_substring] + word[index_substring + 2:])
            index_substring = word.find("UU", index_substring+2)

    return sorted(words_list)

# print(generate('MUI'))
# print(generate('MUUI'))
# print(generate('MIIIU'))
# print(generate('MIIIUUIII'))