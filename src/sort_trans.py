#TODO
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
        "what Lovecraft would think of a trans person",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

#TODO
def is_transmasc(input_str:str):
    """
    takes a string

    returns True if it denotes [...]

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
def is_transfemme(input_str:str):
    """
    takes a string

    returns True if it denotes [...]

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

#TODO (not added to dispenser yet)
def is_detrans(input_str:str):
    """
    takes a string

    returns True if it denotes [...]

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
