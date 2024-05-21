def x_union(list1, list2):
    #a letra do tuplo é a parte importante
    lt1 = filter(lambda pair: pair[0] not in map(lambda pair: pair[0], list2), list1)
    lt2 = filter(lambda pair: pair[0] not in map(lambda pair: pair[0], list1), list2)

    unique_pairs = list(lt1) + list(lt2)
    return unique_pairs