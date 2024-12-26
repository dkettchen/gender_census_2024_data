def is_androgynous(input_str:str):
    """
    takes a string

    returns True if it denotes an alignment with androgynous expression

    otherwise returns False
    """
    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True

    # excluding stuff
    for item in [
        "androgyne",
        "androgyny",
        "androygyne",
        "andromorph",
    ]:
        if item in lower_str:
            result_bool = False

    for item in [
        "(french)",
        "/", # androgyne / androgynous cases
    ]:
        if item in lower_str:
            result_bool = True

    return result_bool

def is_androgyne(input_str:str):
    """
    takes a string

    returns True if the androgyne label is contained

    otherwise returns False
    """
    # making case insensitive
    lower_str = input_str.lower()

    if is_androgynous(input_str) and "/" not in input_str:
        return False

    result_bool = True

    # excluding stuff
    for item in [
        "androgyny",
        "andromorph",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool