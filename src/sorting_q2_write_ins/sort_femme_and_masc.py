# anything femme ✅
def is_femme(input_str:str):
    """
    takes a string

    returns True if it denotes an alignment with femininity

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "masc",
        "utch",
        "tomboy",
        "femininity is something deeply performative for me", # implies non-enjoyment of it
        "angry at societal expectations of femininity",
        "macho",
        "never quite doing femininity right",
        "nonfem",
        "not fem",
        "non-fem",
        "unfem",
        "femoid",
        "post-",
        "rosazur",
        "trans fem / transfem",
        "transfem (short but cute for transfeminine)",
        "would be cuter if i wasn't so lazy",
        "azur",
        "tom",
        "handsome",
    ]:
        if item in lower_str:
            result_bool = False

    # reincluding transmascs etc
    for item in [
        "trans masc",
        "transmasc",
        "trans-masc",
        "not female",
    ]:
        if item in lower_str:
            result_bool = True

    # remove non-qualifying transmasc mentions
    for item in [
        "transmascfem",
        "transmascfemme",
        "butch",
    ]:
        if item in lower_str:
            result_bool = False
    
    return result_bool

# anything masc ✅
def is_masc(input_str:str):
    """
    takes a string

    returns True if it denotes an alignment with masculinity

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    if is_femme(input_str):
        return False

    result_bool = True
    
    for item in [
        "fem",
        "gay man", # bc used as opposing butch
        "fag",
        "flamboyant",
        "peacock",
        "girly",
        "pretty",
        "cute",
        "rosazur",

        "i was a tomboy", # in the past or hypothesis
        "when i was young",
        "former ",
        "wanna",
        "moder",

        "masc because that's what people expect of me", # implies non-enjoyment
        "never masc",
        "not masc",
        "non masc",
        "non-masc",
        "masculine urge",
        "not always masc",
        "not butch",
    ]:
        if item in lower_str:
            result_bool = False
    
    # reincluding transfemmes etc
    for item in [
        "trans fem",
        "transfem",
        "trans-fem",
        "female",
        "butch fag",
        "butchfag",
        "fag butch",
        "fagbutch",
    ]:
        if item in lower_str:
            result_bool = True

    # remove non-qualifying transfemme mentions
    for item in [
        "trans-femme-tomboy-whatever",
        "femmasc",
        "femmemasc",
        "femasc",
        "femneumasc",
    ]:
        if item in lower_str:
            result_bool = False
    
    
    return result_bool

# anything both ✅
def is_futch(input_str:str):
    """
    takes a string

    returns True if it denotes an alignment with both masculinity and femininity

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    if is_femme(input_str) or is_masc(input_str):
        return False

    result_bool = True
    
    for item in [ # things to exclude
        "i was a",
        "former",
        "femininity is something deeply performative for me",
        "masc because that's what people expect of me",
        "neither masc nor fem",
        "never masc",
        "never quite doing femininity right",
        "non masc",
        "non-masc",
        "nonmasc",
        "non-fem",
        "nonfem",
        "non fem",
        "not masc",
        "not fem",
        "masculine urge",
        "unfem",
        "wanna",
        "angry at societal expectations of femininity",
        "fagdyke",
        "dykefag",
        "dyke-fag",
        "not always masc",
        "not butch",
        "post-",
        "when i was young",
        "moder",
        "transfemasc",
        "transfemmasc",
        "transfemneumasc",
        "transmascfem",
        "transneufemmasc",
        "would be cuter if i wasn't so lazy"
    ]:
        if item in lower_str:
            result_bool = False

    
    # reincluding stuff
    for item in [
        "female",
    ]:
        if item in lower_str:
            result_bool = True

    return result_bool