def snail(column, day, night):
    m = 0
    d = 0
    while True:
        m += day
        if m >= column:
            return d+1
        else:
            m -= night
            d += 1