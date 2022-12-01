def my_first_interpreter(code):
    value = 0
    res = ''
    for i in code:
        if i == '+':
            value += 1
            if value > 255:
                value = 0
        elif i == '.':
            res += chr(value)
    return res