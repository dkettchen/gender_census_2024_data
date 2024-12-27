def is_he(input_str:str, data_case=None):
    """
    takes a string and an optional data_case that can be "male-aligned"

    returns True if it involves he pronouns (as part of the label/phrase, 
    not just as part of the sentence in general)
    and does not claim she pronouns (ie we're excluding stuff like she/he)
    but including multi set users as long as she is not involved (ie he/they, he/they/it)

    if data_case="male-aligned", it also excludes any female- or conflicted aligned cases 
    (ie he/him lesbian, he/him girl)

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

    # if it's only "his", bc that isn't abt one's own pronouns
    if lower_str == "his":
        result_bool = False

    # if we want to exclude the conflicted/female ones
    if data_case == "male_aligned": 
        for item in [
            "sbian",
            "girl",
            "woman",
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

def is_she(input_str:str, data_case=None):
    """
    takes a string

    returns True if it involves she pronouns (as part of the label/phrase, 
    not just as part of the sentence in general) excluding he users, but 
    including multi set users as long as he is not included (ie she/they)

    if data_case="female-aligned", it also excludes any male- or conflicted aligned cases 
    (ie she/her twink)

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

    # excluding just she/he to not catch she/her
    if lower_str == "she/he":
        result_bool = False

    # if we want to exclude the conflicted/female ones
    if data_case == "female_aligned": 
        for item in [
            "twink",
            "boy",
            "shemale",
            "she's the man",
            "bear",
        ]:
            if item in lower_str:
                result_bool = False

    return result_bool

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
        "of them",
        "anything but they/them",
        "they don't",
        "they are",
        "they broke the mould when they made me",
        "they will",
        "they'll",
        "they're",
        "saw them self as",
        "to them",
        "i hardly know... them",
        "to like they",
        "if they turned",
        "their own",
        "you want them",
        "their beliefs",
        "i am their",
        "they call me",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool
