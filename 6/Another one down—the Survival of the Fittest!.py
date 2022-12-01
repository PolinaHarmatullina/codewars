def remove_smallest(n, arr):
    if n <= 0:
        return arr
    if n > len(arr):
        return []
    arr2 = arr.copy()
    while len(arr) - n < len(arr2):
        min2 = min(arr2)
        for i in arr:
            if i == min2:
                arr2.remove(i)
                if len(arr) - n == len(arr2):
                    break
    return arr2