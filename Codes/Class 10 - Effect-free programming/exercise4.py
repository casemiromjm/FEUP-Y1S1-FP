def union_with(combine, dict1:dict, dict2:dict):
    #keys in dict1 not in dict2
    #keys in dict2 not in dict1
    #combine

    dict1_notdict2 = {key:value for key, value in dict1.items() if key not in dict2}
    dict2_notdict1 = {key:value for key, value in dict2.items() if key not in dict1}
    dict_union = {key:combine(dict1[key], dict2[key]) for key in dict1 if key in dict2}
    
    return {**dict1_notdict2, **dict2_notdict1, **dict_union } #dict1_notdict2 | dict2_notdict1 | dict_union in python 3.9+