def strip_comments(string, markers):
    list = string.split("\n")
    res = []
    for line in list:
        for marker in markers:
            if marker in line:
                line = line[:line.find(marker)].rstrip()
        res.append(line)
    return "\n".join(res)