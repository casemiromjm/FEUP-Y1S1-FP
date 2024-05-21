def longest(filename):
    with open(filename) as f:
        lines = f.read()
        words = lines.split()
    
    words.sort(key= lambda x: len(x))

    return words[len(words) - 1]