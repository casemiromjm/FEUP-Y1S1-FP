def biggest_number(atuple):
    ans = atuple
    for item in atuple:
        if type(item) == tuple:
            tempTuple = biggest_number(item)
            if len(tempTuple) > len(ans):
                ans = tempTuple
    return ans

print(biggest_number((5, (2, 3, 1))))