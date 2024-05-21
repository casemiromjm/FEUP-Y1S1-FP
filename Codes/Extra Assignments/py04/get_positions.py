def get_positions(sentence, word_list):
    strings = sentence.split(" ")
    str1 = strings[0]
    str2 = strings[1]
    if str1 in word_list and str2 in word_list:
        position_str1 = str(word_list.index(str1))
        position_str2 = str(word_list.index(str2))
        return position_str1 + " " + position_str2
    else:
        return ""