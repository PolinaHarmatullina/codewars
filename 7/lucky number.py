def is_lucky(n):
    sum = 0
    if n == 0:
        return True
    else:
        for iter in (int(a) for a in str(n)):
            sum += iter
        if sum % 9 == 0:
            return True
        else:
            return False