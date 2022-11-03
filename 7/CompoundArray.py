def compound_array(a, b):
    ab = []
    for i in range(max(len(a),len(b))):
        if i < len(a):
            ab.append(a[i])
        if i < len(b):
            ab.append(b[i])
    return ab