def time_diff(time1, time2):
    #time is a tuple (hh,mm)

    h1 = time1[0]
    m1 = time1[1]
    h2 = time2[0]
    m2 = time2[1]

    m1 = m1 + h1*60
    m2 = m2 + h2*60

    diff = abs(m1 - m2)

    hour_diff = diff // 60
    min_diff = diff % 60

    return (hour_diff, min_diff)