def change(amount):
    avaliableCoins = [200, 100, 50, 20, 10, 5, 2, 1]
    changeCoins = []
    while amount > 0:
        for i in avaliableCoins:
            coins = amount // i
            if coins >= 1:
                for j in range(coins):
                    changeCoins.append(i)
                amount = amount - i*coins

    return changeCoins