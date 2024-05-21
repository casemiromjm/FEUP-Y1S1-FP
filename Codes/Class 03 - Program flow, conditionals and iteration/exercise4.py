dimension = int(input())
center = dimension // 2
center_1 = center - 1
is_dimension_even = dimension % 2 == 0


for j in range(dimension):
    line = ""
    for i in range(dimension):
        if is_dimension_even and (i >= center_1 and i <= center) and (j >= center_1 and j <= center):
            line = line + "0"
        elif i == center and j == center:
            line = line + "0"
        else:
            line = line + "#"
    print(line)