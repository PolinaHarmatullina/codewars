def solve(grid):
    n0 = len(grid)
    n = n0 & ~1
    rs = [0] * n
    cs = [0] * n
    for ir in range(n):
        for ic in range(n):
            if grid[ir][ic]:
                rs[ir] ^= 1
                cs[ic] ^= 1
    res = [(ic, ir)
        for ir in range(n)
        for ic in range(n)
        if not rs[ir] ^ cs[ic] ^ grid[ir][ic]]
    if n0 % 2 == 1 and not grid[n][n]:
        res.append((n, n))
    return res