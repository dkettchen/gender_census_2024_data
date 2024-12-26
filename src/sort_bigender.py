def is_genderfull(input_str:str):
    """
    takes a string

    returns True if it denotes bigender, trigender, pangender, or genderfull identities 
    (including contradictions like both being genderfull & genderless)
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