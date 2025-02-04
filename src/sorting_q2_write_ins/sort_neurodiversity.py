def is_autistic(input_str:str):
    """
    takes a string

    returns True if it denotes autism 
    (currently redundant as all collected items pass)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    if "au" not in lower_str:
        return False

    result_bool = True
    
    # excluding stuff
    for item in [

    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_neurodivergent(input_str:str):
    """
    takes a string

    returns True if it denotes other neurodiversity (than autism)
    (currently redundant as all collected items pass)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [

    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_plural(input_str:str): #DID
    """
    takes a string

    returns True if it denotes dissociative identity disorder (DID)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "hacked the system",
        "colonial-modern gender system",
        "many-gendered",
        "many genders and no gender",
        "many hats",
        "many conflicting flavours",
    ]:
        if item in lower_str:
            result_bool = False

    if lower_str == "many":
        result_bool = False

    return result_bool