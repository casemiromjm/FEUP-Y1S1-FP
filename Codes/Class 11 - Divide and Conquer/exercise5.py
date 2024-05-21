def longest_prefix(words:list):
    if len(words) == 1:
        return words[0]
    else:
        prefix = ""

        letters_shortest = [l for l in min(words)]
        words_copy = words.copy()
        
        while min(words) in words_copy:
            words_copy.remove(min(words))

        letter_in_word = True
        while True:
            for i in range(len(letters_shortest)):
                for word in words_copy:
                    if letters_shortest[i] == word[i]:
                        letter_in_word = True
                    else:
                        letter_in_word = False
                        return prefix
                if letter_in_word:
                    prefix = prefix + letters_shortest[i]
            return prefix
        
        # o pensamento está correto, mas corri a lista de palavras em todas as vezes. bastava comparar 1 string de cada vez, faria a mesma coisa e seria mais eficiente

def longest_prefix_simplified(words:list): # usando comparacao de strings
    if len(words) == 1:
        return words[0]
    else:
        prefix = words[0]

        for word in words[1:]:
            for i in range(len(prefix)):
                if i == len(word):
                    break
                if prefix[i] != word[i]:
                    prefix = prefix[:i]
                    break
                
        return prefix