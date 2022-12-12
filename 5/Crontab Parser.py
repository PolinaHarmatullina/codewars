def parse(crontab):
    out = []
    d = {0:("minute         ",0,59),
            1:("hour           ",0,23), 
            2:("day of month   ",1,31),
            3:("month          ",1,12),
            4:("day of week    ",0,6)}
    for k,v in {"JAN":"1", "FEB":"2", "MAR":"3", "APR":"4",
                "MAY":"5", "JUN":"6", "JUL":"7", "AUG":"8",
                "SEP":"9", "OCT":"10", "NOV":"11", "DEC":"12",
                "SUN":"0", "MON":"1", "TUE":"2", "WED":"3",
                "THU":"4", "FRI":"5", "SAT":"6"}.items():
        crontab = crontab.replace(k, v)
    elts = crontab.split()
    for i in range(5):
        numbers = set()
        print(elts[i])
        field, mn,mx = d[i]
        for comb in elts[i].split(","):
            if "/" in comb:
                step = int(comb.split("/")[1])
                comb = comb.split("/")[0]
            else:
                step = 1
            if comb == "*":
                numbers.update(range(mn,mx+1,step))
            elif "-" in comb:
                numbers.update(range(int(comb.split("-")[0]),int(comb.split("-")[1])+1,step))
            else:
                numbers.add(int(comb))
        out.append(field+" ".join(map(str,sorted(numbers))))
    return "\n".join(out)