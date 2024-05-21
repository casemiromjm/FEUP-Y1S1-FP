def change(money):
    money_cents = money * 100 #money in cents
    coins_dict = {2.0: 0, 1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    coins = [200, 100, 50, 20, 10, 5, 2, 1] # coin value * 100
    
    for coin in coins:
        coins_dict[coin/100] = (money_cents // coin)
        money_cents = money_cents % coin
    
    return coins_dict