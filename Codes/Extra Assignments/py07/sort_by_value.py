def sort_by_value(dict):
    dict_copied = dict.copy()
    sorted_dict = []

    for color, hex_code in dict.items():
        tempTuple = (color, hex_code)
        sorted_dict.append(tempTuple)
    
    sorted_dict.sort(key = lambda tup: tup[1])
    
    return sorted_dict