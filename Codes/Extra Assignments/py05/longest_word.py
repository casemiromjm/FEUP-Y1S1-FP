def longest(s):
    string = s.split()
    longestString = string[0]

    for word in string:
        if len(word) > len(longestString):
            longestString = word

    return len(longestString)