def array_erasing(lst):
    count = 0
    while lst:
        group_num, groups = 0, {}
        i = 0
        while i < len(lst) - 1:
            if lst[i] == lst[i+1]:
                s = i
                while i < len(lst) - 1 and lst[i] == lst[i+1]:
                    i += 1
                groups[group_num] = (s, i)
            group_num += 1
            i += 1

        med = group_num//2
        count += 1

        if groups:
            to_remove = min(groups, key=lambda x: abs(med-x))
            start, end = groups[to_remove]
            lst = lst[:start] + lst[end+1:]
        else:
            lst = lst[:med] + lst[med+1:]
    return count