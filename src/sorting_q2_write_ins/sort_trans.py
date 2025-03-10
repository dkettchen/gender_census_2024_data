def is_trans(input_str:str):
    """
    takes a string

    returns True if it denotes trans gender (including intersex trans people)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "transv",
        "faggot with the girls and a tranny with the boys",
        "trans man and a butch woman",
        "transfem transmasc",
        "afab transfem",
        "mab transmasc",
        "afab trans woman",
        "cetran",
        "detrans",
        "cis girl trans guy",
        "cistrans",
        "cis or trans",
        "cis nor trans",
        "trans nor cis",
        "trans or cis",
        "don't want to transition", # idk
        "i made a transition f to" # "i don't care" if you don't care then Imma say that doesn't count
        "i'm sure i'm not a trans man",
        "maybe", # questioning can take care of these
        "not cis not trans",
        "not exactly",
        "transmisogyny",
        "trans both ways",
        "trans masc in an amab way",
        "trans-cendent",
        "transkenous",
        "mascfem",
        "transn't",
        "transoutherine",
        "transspecies",
        "transtidal",
        "transxen", # idk what these mean so rip
        "a transfem trapped in a transmasc body",
        "amab trans boy",
        "double trans", # =.=
        "(without the trans)",
        "who's not actually",
        "to trans people",
        "if a transmasc guy was also transfem",
        "multitrans", # idk what this means
        "non-transition",
        "the trans/cis binary",
        "the cis/trans binary",
        "not a trans woman",
        "not binary trans",
        "but not trans",
        "not trans, but a secret third thing",
        "not quite trans'",
        "not trans but",
        "sometimes cis",
        "cisgender and transgender",
        "trans girl (but in the afab way)", # no such thing dear pls get help
        "trans man in a trans woman's body",
        "trans-inclusive",
        "femasc",
        "femmasc",
        "feminist",
        "transfeminine in a transmasculine way",
        "transfemneumasc",
        "czech", # I am not googling czech slurs to verify them
        "transman and ciswoman",
        "transmasc but transfem in a way",
        "transmasc puppygirl",
        "transmasc transfem",
        "transmasc transgirl",
        "transmasc woman",
        "transmasculine woman",
        "transmulti",
        "transtransfem",
        "transwarp",
        "trantran",
        "trans-cis",
        "world's first cisgender trans woman",
        "of a trans person",
        "(mtf)tm", # more detransitioners
        "ftmtf",
        "mtftm",
        "f2m2f2m2f",
        "ftmgirl",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_transmasc(input_str:str):
    """
    takes a string

    returns True if it denotes ftm (trans man), ftx (afab nb), or xtm (intersex trans man)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    if not is_trans(input_str):
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "woman",
        "girl",
        "gal",
        "amab",
        "mtf",
        "transfem",
        "trans fem",
        "trans-fem",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_transfemme(input_str:str):
    """
    takes a string

    returns True if it denotes anyone mtf (trans woman), mtx (amab nb), or xtf (intersex trans woman)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    if not is_trans(input_str):
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "transmasc",
        "trans masc",
        "trans-masc",
        "ftm",
        "female to male",
        "afab",
        "trans man",
        "trans guy",
        "trans dude",
        "trans boy",
        "transman",
        "girl in a trans way",
        "my gender is more trans than feminine",
        "trans and feminine",
        "assigned female",
        "effeminate",
        "transfem boy",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_detrans(input_str:str):
    """
    takes a string

    returns True if it denotes a non-reverted detransition (-> excluding "retransitioner"s)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = False
    
    # including stuff
    for item in [
        "detrans",
        "mtftm",
        "ftmtf",
        "(mtf)tm",
        "male to female to male",
        "female to male to female",
        "f2m2f",
        "m2f2m",
    ]:
        if item in lower_str:
            result_bool = True

    return result_bool
