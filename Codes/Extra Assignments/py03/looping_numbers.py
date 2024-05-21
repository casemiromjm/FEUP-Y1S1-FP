n = int(input())
looping = True

if n // 10 == 0:
        looping = True

else:
    while n > 9:
        last_digit = n % 10
        second_last_digit = (n // 10 ) % 10
        n = n // 10
        if n < 10:
             looping = True
        if abs(second_last_digit - last_digit) not in (1,9):
             looping = False
             break
        else:
             looping = True

if looping == True:
     print("Looping number")
else:
     print("Not a looping number")