price = int(input())
received = int(input())

change = received - price

bill_50 = 0
bill_20 = 0
bill_10 = 0
bill_5 = 0


while change != 0:
    if change >= 50:
        bill_50 = change // 50
        change = change - 50*bill_50
    elif change >= 20:
        bill_20 = change // 20
        change = change - 20*bill_20
    elif change >= 10:
        bill_10 = change // 10
        change = change - 10*bill_10
    elif change >= 5:
        bill_5 = change // 5
        change = change - 5*bill_5

print(f"{bill_50} {bill_20} {bill_10} {bill_5}")