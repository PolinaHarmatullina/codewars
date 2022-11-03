def evaporator(content, evap_per_day, threshold):
    d = 0
    per0 = 100
    per = 1 - evap_per_day*0.01
    while per0 > threshold:
        per0 *= per
        d += 1
    return d