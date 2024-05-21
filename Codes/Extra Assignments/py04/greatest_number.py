def greatest(num):
    num_str = str(num)

    digits = []
    for i in num_str:
        digits.append(i)
    
    digits.sort(reverse=True)

    greatest_num = ""
    for i in digits:
        greatest_num += i

    return int(greatest_num)