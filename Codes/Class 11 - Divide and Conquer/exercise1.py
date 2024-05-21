def merge(xs, ys):
    result = []
    i = j = 0
    while i < len(xs) and j < len(ys):
        if xs[i] < ys[j]:
            result.append(xs[i])
            i += 1
        else:
            result.append(ys[j])
            j += 1

    # Add the remaining elements from both lists, if any
    result.extend(xs[i:])
    result.extend(ys[j:])

    return result

def msort(xs):              #usar recursividade nesse caso
    if len(xs) <= 1:
        return xs
    else:
        mid = len(xs) // 2
        xs_left = msort(xs[:mid])
        xs_right = msort(xs[mid:])
        return merge(xs_left, xs_right)