# male & female passing/presenting ✅
def is_present_passing(input_str:str, data_case:str):
    """
    takes an input string and a data case string (data_case="male|female")

    returns true or false based on whether the string implies 
    the person passes or presents as male or female
    """

    # making case insensitive
    lower_str = input_str.lower()

    # we're not excluding any prior categories there may be overlap

    result_bool = False

    # things that qualify it if included (to get rid of most other stuff)
    for item in [
        "passing", 
        "present", 
        "see", 
        "perceive", 
        "look",
        "reason",
        "convenie",
        "rather",
        "soci",
        "shape",
        "dress",
        "legal",
        "government",
        "impersona",
        "bod",
        "deflaut",
        "default",
        "sumed", # assumed, presumed
        "outwardly",
        "form",
        "on tv",
        "read",
        "the outside",
        "woman as in i just work here",
        "inertia",
        "habit",


    ]:
        if item in lower_str:
            result_bool = True

    # excluding general stuff
    if result_bool:
        for item in [
            # can't make up their mind, useless to this
            "female/male",
            "woman/man",

            "a dress",
            "dress like a teenage boy",
            "dress boy",
            "dressed as",
            "crossdress",
            "like dresses",

            "dogs as boys",
            "dissociated",
            "government work",
            "socialised",
            "socialized",
            "woman when its funny, man when it's convenient",
            "woman who wears a dress (in a manly way)",
            "wow what an ugly woman, she looks like a man",
            "seem like a guy",
            "femme presenting",
            "masc-presenting",
            "social ",
            "misshapen",
            "partner",
            "society",
            "see how it fits",
            "in a trans woman's body",  # neither trans man nor cis woman in a trans woman's body 
                                        # are valid under my label police rule smh

            # implies not achieved presentation/passing
            "prefers to be perceived",
            "at least see me",
            "i'd prefer",
            "need to be perceived",
            "will have a man's body",
        ]:
            if item in lower_str:
                result_bool = False

    # excluding gender specifics
    if result_bool and data_case == "male":
        for item in [
            "ciswoman",
            "looks female",
            "looks like a girl",
            "legally a she",
            "legally girl",
            "female passing",
            "female presenting",
            "female-shape",
            "female shape",
            "girl shape",
            "girl-shape",
            "girl of",
            "girl out of",
            "cis/girl",
            "trapped in a woman's body",
            "as a girl",
            "shape of a girl",
            "socially female",
            "woman passing",
            "a girl when",
            "female by",
            "female impersona",
            "girl-passing",
            "legally female",
            "cis woman",
            "socially a girl",
            "socially a woman",
            "as a woman",
            "woman-shape",
            "woman by",
            "woman of",
            "woman shape",
            "woman when",
            "woman-look",
            "a woman's body",
            "a female body",
            "body is a woman",
            "girl's body",
            "boy stuck in a",
            "female bodied",
            "afab",
            "anxiety and dread but in a boy way",
            "assigned female",
            "sumed female",
            "former",
            "gender non conforming",
            "gender non-conforming",
            "gender noncomforming",
            "gender nonconforming",
            "non-conforming",
            "girl on the outside",
            "dont want be read",
            "female form",
            "play a girl on tv",
            "woman as in i just work here",
            "girl by default",
            "habitual girl",
            "other persons read me as female",
            "performatively female",
            "presumed woman for lack of a better option",
        ]:
            if item in lower_str:
                result_bool = False

    elif result_bool and data_case == "female":

        # stuff that qualifies if contains
        for item in [
            "ciswoman",
            "looks female",
            "looks like a girl",
            "legally a she",
            "legally girl",
            "female passing",
            "female presenting",
            "female-shape",
            "female shape",
            "girl shape",
            "girl-shape",
            "girl of",
            "girl out of",
            "cis/girl",
            "trapped in a woman's body",
            "as a girl",
            "shape of a girl",
            "socially female",
            "woman passing",
            "a girl when",
            "female by",
            "female impersona",
            "girl-passing",
            "cis woman",
            "socially a girl",
            "socially a woman",
            "as a woman",
            "woman-shape",
            "woman by",
            "woman of",
            "woman shape",
            "woman when",
            "woman-look",
            "a woman's body",
            "body is a woman",
            "girl's body",
            "boy stuck in a",
            "female bodied",
            "woman as in i just work here",
            "deflaut",
        ]:
            if item in lower_str:
                return True
            
        for item in [
            "cisman",
            "looks male",
            "looks like a boy",
            "legally a he",
            "legally boy",
            "male passing",
            "male presenting",
            "male-shape",
            "male shape",
            "boy shape",
            "boy-shape",
            "boy of",
            "boy out of",
            "cis/boy",
            "trapped in a man's body",
            "as a boy",
            "shape of a boy",
            "socially male",
            "man passing",
            "a boy when",
            "male by",
            "male impersona",
            "boy-passing",
            "legally male",
            "cis man",
            "socially a boy",
            "socially a man",
            "as a man",
            "man-shape",
            "man by",
            "man of",
            "man shape",
            "man when",
            "man-look",
            "a man for legal reasons",
            "perceived as male",
            "male for the sake of convenience",
            "man out of convenience",
            "shape of a man",
            "guy-shape",
            "male (sometimes/for legal identification)",
            "male for the sake of convenience",
            "male is my government gender",
            "male-passing",
            "man for convenience's sake",
            "dude, just impersonating",
            "a man's body",
            "male body",
            "afab",
            "in a boy way",
            "former",
            "gender non conforming",
            "gender non-conforming",
            "gender noncomforming",
            "gender nonconforming",
            "non-conforming",
            "man-form",
            "not a boy, but i play one on tv",
            "dont want be read", # implies potential retrospective (ie I no longer get read as female 
            # but also still do not want to be read as female)
            "legally female", # could refer to an outdated sex marker

        ]:
            if item in lower_str:
                result_bool = False

    return result_bool

