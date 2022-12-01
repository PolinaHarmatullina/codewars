def parse(data):
    res = []
    value = 0    
    for iter in data:
        if iter == "i":
            value += 1
        elif iter == "d":
            value -= 1
        elif iter == "s":
            value *= value
        elif iter == "o":
            res.append(value)
        else: 
            continue
    return res