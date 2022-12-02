def count_cash(a, p):
    a = [x[:] for x in a]
    x, y = p
    for x0 in range(x - 1, -1, -1):
        a[x0][y] += a[x0+1][y]
    for y0 in range(y + 1, len(a[0])):
        a[x][y0] += a[x][y0-1]
    for x0 in range(x - 1, -1, -1):
        for y0 in range(y + 1, len(a[0])):
            a[x0][y0] += max(a[x0+1][y0], a[x0][y0-1])
    return a[0][-1]