def is_crossdresser(input_str):
    """
    takes a string

    returns True if it denotes crossdressing

    otherwise returns False
    """
    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "drag queen born in a woman's body",
        "aspiring",
        "constantly performing drag",
        "performing any gender is me doing drag",
        "a drag queen dressed up as a dragking",
        "a drag queen inside of a man inside a woman",
        "a dragking dressed up as a dragqueen",
        "a girl in the way a drag queen's a girl",
        "in either direction",
        "dragon doing human drag",
        "dude in permanent drag",
        "everything is drag",
        "trans man in drag",
        "like a pantomime", # not a literal one then
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool
