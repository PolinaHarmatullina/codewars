def pythagorean_triplet(n):
    for x in range(3, n):
        for y in range(x+1, n):
            z = (x*x + y*y)**0.5
            if z == int(z) and x*y*z == n:
                return [x, y, z]
            else:
                if x*y*z > n:
                    break