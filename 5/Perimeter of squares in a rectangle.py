def perimeter(n):
    number = [0, 1]
    for i in range(2, n+2):
        number.append(number[i-1] + number[i-2])        
    num = sum(number)*4
    return num