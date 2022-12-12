def convex_hull_area(points):
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    if len(points) <= 2:
        return 0
    points = sorted(set(map(tuple, points)))
    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    res = upper[::-1][:-1] + lower[::-1][:-1]
    m = res.index(min(res, key=lambda p: (p[1], p[0])))
    ch = list(map(list, res[m:] + res[:m]))
    return round(abs(sum(cross((0, 0), a, b) / 2 for a, b in zip(ch, ch[1:] + ch[0:1]))), 2)