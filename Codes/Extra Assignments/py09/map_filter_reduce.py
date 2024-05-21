import functools

def map_filter_reduce(lst:list, f1, f2, f3):
    filtered_lst = filter(f1, lst)
    mapped_lst = map(f2, filtered_lst)
    return functools.reduce(f3, mapped_lst)