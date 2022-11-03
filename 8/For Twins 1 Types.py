def type_validation(variable, _type): 
    typ = str(type(variable))
    if _type in typ:
        return True
    else: 
        return False