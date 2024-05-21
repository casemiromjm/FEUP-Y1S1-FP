def max_path(tree):
    if type(tree) == int:
        return tree
    else:
        (left, value, right) = tree
        return value + max(max_path(left), max_path(right))