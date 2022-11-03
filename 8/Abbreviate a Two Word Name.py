def abbrev_name(name):
    name_arr = name.split()
    first_name = name_arr[0][:1].title()
    last_name = name_arr[1][:1].title()
    return first_name+'.'+last_name