def shorten(suffixes:list, base:int):
    def shortening(num):
        if type(num) is not str or not num.isdigit():
            return str(num)
        
        num = int(num)

        i = 0
        while num // (base ** i) != 0:
            i += 1

        return f"{num // (base**(i-1) )} {suffixes[i-1]}"
    return shortening


print(shorten(['', 'K', 'M'], 1000)('12456789'))
print(shorten(['', 'K', 'M'], 1000)(['dummy', 'list']))
print(shorten(['B', 'KiB', 'MiB', 'GiB', 'TiB'], 1024)('32'))