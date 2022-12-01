def is_valid_set(quantities, shapes, colours, patterns):
    if len(set(quantities)) != 2 and len(set(shapes)) != 2 and len(set(colours)) != 2 and len(set(patterns)) != 2:
        return True
    else:
        return False