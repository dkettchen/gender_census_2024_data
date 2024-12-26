def is_genderless(input_str:str):
    """
    takes a string

    returns True if it denotes genderlessness (ie agender, genderless)
    including any mentions thereof that contain gender presence/alignment etc (ie "agender boy")

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "agender" not in lower_str and ("gender" not in lower_str or "less" not in lower_str):
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "(not the same as agender)",
        "when i talk about misogynists",
        "not agender",
        "genderless slang",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_neutral(input_str:str):
    """
    takes a string

    returns True if it denotes neutral gender (including aligned ones (ie gender neutral girl))

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "(neutral)",
        "[gender neutral]",
        "(gender neutral",
        "(gender-neutral)",
        "(guy being neutral)",

        "in a gender neutral way",
        "it's gender neutral",
        "but gender neutral",
        "in the gender neutral",
        "in a neutral",

        "opposite of a neutral way",
        "(instead of gender neutral)",
        "nor neutral",

        "chaotic",
        "lawful",
        "e o neutro", # prompt was english
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_demi(input_str:str):
    """
    takes a string

    returns True if it denotes demi or grey gender

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "demiromantic",
        "demisexual",
        "greyasexual",
    ]:
        if item in lower_str:
            result_bool = False

    if lower_str in ["grey", "gray"]: # too unspecific
        result_bool = False

    return result_bool