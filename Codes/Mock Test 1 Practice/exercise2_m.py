pe1 = int(input())
pe2 = int(input())
pe3 = int(input())
pe4 = int(input())

if pe3 < 40:
    if pe4 < 40:
        print("RFF")
    else:
        pe = max(pe3, pe4)
        sum = pe1 + pe2 + pe - min(pe1, pe2, pe)
        average = sum/2
        print(average)
else:
    pe = max(pe3, pe4)
    sum = pe1 + pe2 + pe - min(pe1, pe2, pe)
    average = sum/2
    print(average)