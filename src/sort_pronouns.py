def is_he(input_str:str):
    """
    takes a string

    returns True if it involves he pronouns (as part of the label/phrase, 
    not just as part of the sentence in general)
    and does not claim she pronouns (ie we're excluding stuff like she/he)
    but including female he users (ie he/him woman, he/him lesbian) and multi set users
    as long as she is not involved (ie he/they, he/they/it)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "boat",
        "can i dodge the question",
        "if he were a really butch woman",
        "she, but",
        "she but",
        "she in the same way",
        "she/her in a he/him way", # y'all just stopped trying to make sense at some point smh
        "she/her in a he/him kinda way",
        "absence of man",
        "f slur", 
        "sum total of my life",
        "broke the mould",
        "they/them causing",
        "he's my cat",
        "to be his", # stop being horny on main this is a serious survey
        "when janet from the",
        "a she sometimes he",
        "he in the streets, she in the sheets",
        "he's my girl/she's my boy",
        "she/he but he in a not boy way",
        "idk what's happening there, but i prefer they/them",

        "don't call me he/him",
        "anything but he",
    ]:
        if item in lower_str:
            result_bool = False

    # reincluding
    for item in [
        "yknow how boats get called she? that but he/they"
    ]:
        if item in lower_str:
            result_bool = True

    return result_bool
#TODO
def is_she(input_str:str):
    """
    takes a string

    returns True if it involves she pronouns (as part of the label/phrase, 
    not just as part of the sentence in general)

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
#TODO
def is_they(input_str:str):
    """
    takes a string

    returns True if it involves they pronouns (as part of the label/phrase, 
    not just as part of the sentence in general)

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
