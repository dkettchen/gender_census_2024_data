def is_person(input_str:str):
    """
    takes a string

    returns True if it denotes personhood

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "3rd",
        "third",
        "not a person",
        "human",
        "persona",
        "other people",
        "people perceive",
        "impersonat",
        "what people expect",
        "by the people around me",
        "cis people",
        "with cool people",
        "people lover",
        "people think",
        "personifi",
        "not a people",
        "people will",
        "for people",
        "barely even a person",
        "to trans people",
        "people call",
        "other person",
        "as a cis person",
        "of a trans person",
        "pisses people off",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_human(input_str:str):
    """
    takes a string

    returns True if it denotes humanity

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "in a human suit",
        "beyond human comprehension",
        "non-human",
        "nonhuman",
        "non human",
        "person",
        "people",
        "alterhuman", # gender wiki tells me this is explicitly someone who doesn't id as human smh
        "in human form",
        "barely",
        "beyond",
        "inhuman",
        "to humanity",
        "dehumanix",
        "demihuman",
        "humanoid",
        "cat",
        "but also not",
        "ish",
        "but to the left",
        "do not use human",
        "not human",
        "not entirely",
        "not really",
        "possibly",
        "post",
        "human skin",
        "transhuman",
        "unhuman",
        "shape of a human",
        "human understanding",
        "doing human drag",
        "a human body",
        "gender is a human construct for humans",
        "half human",
        "probably",
        "shaped",
        "humanity",
        "not a human",
        "non'-human cunt",
        "nonehuman",
        "not quite",
        "not very",
        "not-quite",
        "the body of a human",
        "human meat suit",

        

    ]:
        if item in lower_str:
            result_bool = False

    return result_bool
