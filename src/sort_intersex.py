#TODO
def is_intersex(input_str:str):
    """
    takes a string

    returns True if it denotes someone intersex

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "mental",
        "in a ",
        "herm ",
        "sacred", # you don't get to decide that
    ]:
        if item in lower_str:
            result_bool = False

    if lower_str == "herm":
        result_bool = False

    return result_bool
