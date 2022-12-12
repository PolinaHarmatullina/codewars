def count_divisors(n):
    r = int(n**(1/2))
    return 2*sum(n // i for i in range(1, r+1)) - r*r