def sparse_dot_product(dict1, dict2):
    inner_product = 0
    for key in dict1:
        if key in dict2:
            inner_product += dict1[key]*dict2[key]

    return inner_product