def lfsr(n):
    original_n = n
    pseudo_random_num = ""

    #add last digit to prm
    pseudo_random_num += n[len(n) - 1]

    #change n by removing it last number and prepending a new one
    to_prepend = xor(n[len(n) - 1], n[len(n) - 2])
    n = n[:len(n) - 1]
    n = to_prepend + n

    #repeat the process until n is repeated

    while n != original_n:
        pseudo_random_num += n[len(n) - 1]
        to_prepend = xor(n[len(n) - 1], n[len(n) - 2])
        n = n[:len(n) - 1]
        n = to_prepend + n
    
    return pseudo_random_num

def xor(dig1, dig2):
    if dig1 != dig2:
        return "1"
    else:
        return "0"