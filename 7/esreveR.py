def reverse(lst):
    relst = list()
    for i in range(len(lst)-1,-1,-1):
        relst.append(lst[i])    
    return relst