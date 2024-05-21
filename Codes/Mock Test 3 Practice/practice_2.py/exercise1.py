def days_until_christmas(date):
    d, m , y = date

    missing_days = 0

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
    
    while d != 25 or m != 12:
        if d <= 25:
            missing_days += (25 - d)
            d = 25
        if d > 25:
            missing_days += (days_of_month[m] - d + 25)
            m += 1
            d = 25
            if m > 12:
                m = 1
                y += 1
        if m != 12:
            for month in range(m, 12):
                missing_days += (days_of_month[month])
            m = 12
    
    return missing_days

# print(days_until_christmas((18, 12, 2022)))
# print(days_until_christmas((25, 12, 2022)))
# print(days_until_christmas((26, 12, 2022)))
# print(days_until_christmas((10, 1, 2023)))