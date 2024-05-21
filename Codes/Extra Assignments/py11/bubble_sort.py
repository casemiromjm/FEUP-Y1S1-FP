def bubble_sort(alist:list):
    n = len(alist)

    for _ in range(n):
        for i in range(n-1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    
    return alist


print(bubble_sort([5, 1, 2, 8, 2.5]))
print(bubble_sort([192, 12378, 12, -113, 12.5, 10]))
print(bubble_sort(['Joaquina', 'Alexandra', 'Delfina', 'Emílio', 'Eduardo', 'Correia', 'João', 'Lopes']))