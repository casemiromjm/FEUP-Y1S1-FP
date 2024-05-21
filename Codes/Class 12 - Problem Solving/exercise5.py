def cows_bulls(seed_value):
    import random

    random.seed(seed_value)

    def cow(guess):
        num = str(random.randint(0, 9999))
        guess = str(guess)
        guess = list(guess)
        num = list(num)
        cows = 0
        bulls = 0
        check = 0
        while check == 0:
            check = 1
            for i in range(len(num)):
                if num[i] == guess[i]:
                    cows += 1
                    guess.pop(i)
                    num.pop(i)
                    check = 0
                    break
        for i in list(set(guess)):
            if i in num:
                bulls += 1
        return (cows, bulls)

    return cow
