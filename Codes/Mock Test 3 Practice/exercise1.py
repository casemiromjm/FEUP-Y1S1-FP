def days_until_christmas(date):
    (d, m , y) = date

    days_of_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

    if m == 12 and d <= 25:
        return 25 - d
    if m == 12 and d > 25:
        return 31 - d + 359
    if m != 12:
        days = 25 + (days_of_month[m] - d)
        
        for month in range(m+1, 12):
            days += days_of_month[month]
        
        return days

# print(days_until_christmas((18, 12, 2022)))
# print(days_until_christmas((25, 12, 2022)))
# print(days_until_christmas((26, 12, 2022)))
# print(days_until_christmas((10, 1, 2023)))