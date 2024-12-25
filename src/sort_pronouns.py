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

    # input checking
    if "he" not in lower_str and "him" not in lower_str and "his" not in lower_str:
        return False

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
        "she",

        "don't call me he/him",
        "anything but he",
    ]:
        if item in lower_str:
            result_bool = False

    # reincluding
    for item in [
        "yknow how boats get called she? that but he/they",
        "she was a hell",
    ]:
        if item in lower_str:
            result_bool = True

    return result_bool

def is_she(input_str:str):
    """
    takes a string

    returns True if it involves she pronouns (as part of the label/phrase, 
    not just as part of the sentence in general) excluding he users, but 
    including non-female she users and multi set users as long as he is not 
    included (ie she/they)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "she" not in lower_str and "her" not in lower_str:
        return False

    if is_he(input_str): # we've excluded all she users from the is_he func
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "boy in the way a boat",
        "not she",
        "she/her in a he/him way",
        "she/her in a he/him kinda way",
        "not too she",
        "he in the streets, she in the sheets",
        "he's my girl/she's my boy",
        "a guy in the way",
        "legally a she, illegally a dude",
        "not a she/her",
        "wow what an ugly woman, she looks like a man",
        "a she sometimes he",
    ]:
        if item in lower_str:
            result_bool = False

    if lower_str == "she/he":
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


#TODO somehow add the useable he & she ones of these to their male/female alignment
    # another function to separate them out? into male/female- aligned & conflicted aligned?
    # or make these functions conflict excluding?