# binary search
# 3 ponteiros (esq, meio, dir)
# usar recursao

def find_me(f, limits):
    n = sum(limits) // 2
    if f(n) == 0:          # numero certo
        return 1
    if f(n) == 1:                                      # pegar um numero maior do q o testado
        return 1 + find_me(f, (n+1, limits[1]))       # fazer 1 + find, soma 1 a cada iterecao
    else:
        return 1 + find_me(f, (limits[0], n-1))