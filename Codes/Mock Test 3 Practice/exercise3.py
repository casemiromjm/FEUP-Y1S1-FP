def lfsr(n:str):
    original_n = n

    n_length = len(n)

    pseudo_random_num = n[n_length - 1] #comeca com o ultimo digito de n
    prepend = xor(n[n_length - 1], n[n_length - 2])

    n = n[:n_length - 1] #tira o ultimo digito de n
    n = prepend + n #novo n

    while n != original_n:
        pseudo_random_num += n[n_length - 1] #acrescenta o ultimo digito do novo n

        prepend = xor(n[n_length - 1], n[n_length - 2])
        n = n[:n_length - 1] #tira o ultimo digito de n 
        n = prepend + n #atualiza n

    return pseudo_random_num

def xor(dig1, dig2):
    if dig1 != dig2:
        return "1"
    return "0"

# print(lfsr('100'))
# print(lfsr('10'))
# print(lfsr('1010'))
# print(lfsr('10101'))