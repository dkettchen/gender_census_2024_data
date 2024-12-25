def is_achillean(input_str:str):
    """
    takes a string

    returns True if it denotes achillean (the label, not its full meaning, 
    we have other categories to cover that)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "achillean" not in lower_str:
        return False

    result_bool = True
    
    # excluding stuff
    for item in [

    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_bear(input_str:str):
    """
    takes a string

    returns True if it denotes a (gay) bear

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "bear" not in lower_str:
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "teddy bear",
        "teddybear",
        "(like the animal)",
        "butch",
        "dyke",
        "lesb",
        "ursula",
        "build-a-bear",
        "mama bear",
        "girl",
        "shebear",
        "polar bear",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_butch(input_str:str):
    """
    takes a string

    returns True if it denotes butches excluding male/transmasc ones

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "butch" not in lower_str:
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        " man",
        "dad",
        "twink",
        "bear",
        "guy",
        "boy",
        "boi",
        "fag",
        "ftm",
        "futch",
        "testo",
        "dandy",
        "he/him",
        "hehim",
        "he him",
        "man but in a butch way",
        "not butch",
        "tbutch",
        "transmasc",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_dyke(input_str:str):
    """
    takes a string

    returns True if it denotes dykes excluding male/transmasc ones

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "dyke" not in lower_str:
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "fag",
        "boy",
        "bear",
        " man",
        "ftm",
        "guy",
        "t dyke",
        "t-dyke",
        "testo",
        "transmasc",
        "twink",
        "uncle",
        "boi",
        "sissy",
        "dude",
        "where is dyke", # complaints are useless here
        "hermaphr",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_fag(input_str:str):
    """
    takes a string

    returns True if it denotes faggots excluding female/transfemme/lesbian ones (ie fagdyke)
    but including presumed transmascs combining it with non-op body parts (ie fagpussy haver)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "fag" not in lower_str:
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "dyke",
        "girl",
        "male to female",
        "a tranny with the boys",
        "aunt",
        "butch",
        "hag",
        "lady",
        "whatever makes you",
        "bian",
        "lesb",
        "bitch",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_gay(input_str:str):
    """
    takes a string

    returns True if it denotes gay people

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "gay" not in lower_str:
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "lesbian",
        "who is neither gay nor a man",
        "(like the gay kind)", # not claiming gay itself
        "is gay",
        "in a gay man way",
        "direction",
        "gaybian", # assuming this is trying to claim both not to denote gay girl
        "a woman was a gay man",
        "whatever",
        "whichever",
        "is inherently gay",
        "both ways",
        "for everyone",
        "gayboy, gaygirl",
        "girl who is a gay boy",
        "you're gay",
        "it's not gay to like they",
        "what ever",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_homosexual(input_str:str):
    """
    takes a string

    returns True if it denotes homosexuality

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "homo" not in lower_str:
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "and everything else",
        "hetero",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_lesbian(input_str:str):
    """
    takes a string

    returns True if it denotes lesbians excluding male/transmasc ones

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "les" not in lower_str and "lez" not in lower_str and "bian" not in lower_str:
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "in spirit",
        " man",
        "boy",
        "he/him",
        "not a lesbian",
        "ftm",
        "gaybian",
        "with the lesbians",
        "lesbear",
        "husband",
        "coded",
        "are attracted to me",
        "male lesbian",
        "twink",
        "succubian",
        "culturally",
        "fag",
        "hehim",
        "he him",
        "uncle",
        "hesbian",
        "yaoi",
        "guy",
        "of lesbian origin",
        "but the other way",
        "transmasc",
        "transman",
        "boi",
        "dude",
        "genderless amalgamation of flesh", # idk why this doesn't catch properly smh
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_sapphic(input_str:str):
    """
    takes a string

    returns True if it denotes sapphics excluding male ones (the label not the full category)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "sapph" not in lower_str:
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "guy",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_twink(input_str:str):
    """
    takes a string

    returns True if it denotes twinks excluding female/transfemme ones

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "twink" not in lower_str:
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "female",
        "butch",
        "girl",
        "sissy tranny", # presumably amab in which case you can't be a tranny and a twink at once
        "dyke",
        "twinkette",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

#TODO
def is_bi_pan(input_str:str):
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
def is_ace_aro(input_str:str):
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
def is_dykefag(input_str:str):
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

