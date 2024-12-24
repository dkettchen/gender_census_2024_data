# have not put these into dispenser & cases yet bc I might still rename em idk

def is_wlw(input_str:str):
    """
    takes a string

    returns True if it denotes women loving women (including relevant words like butch), 
    excluding lesbianism for men type stuff (ie male lesbian, boydyke, etc)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "boy",
        "fag",
        "guy",
        "gay man",
        "he/him",
        "trans man",
        "in spirit",
        "dad",
        "twink",
        " man",
        "ftm",
        "i caucus with",
        "who took t once",
        "lesbear",
        "husband",
        "are attracted to me",
        "male lesbian",
        "sissy",
        "testo",
        "transmasc",
        "uncle",
        "bear butch",
        "bear dyke",
        "beardyke",
        "boi",
        "butch bear",
        "dandy",
        "cocksucking dyke",
        "culturally",
        "he him",
        "hehim",
        "yaoi",
        "dude",
        "like a nonbinary lesbian but the other way",
        "man but in a butch way",
        "man of lesbian origin",
        "not butch but i respect their beliefs",
        "where is dyke",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_mlm(input_str:str):
    """
    takes a string

    returns True if it denotes men loving men (including relevant words like bear/twink), 
    but including any homo & gay mention that isn't explicitly about lesbians (ie gay girl)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "lesb",
        "dyke",
        "neither gay nor a man",
        "a tranny with the boys",
        "aunt",
        "butch",
        "beard",
        "bitch",
        "boygirl",
        "build-a-bear",
        "is gay",
        "is inherently gay",
        "fagatha",
        "teddy",
        "(like the animal)",
        "faghag",
        "but no one knows in what direction",
        "girl",
        "homonculus",
        "homogeneous",
        "homophile",
        "not gay",
        "lady fag",
        "mama bear",
        "most homophobic slurs",
        "overbearing",
        "shebear",
        "theybear",
        "whatever makes you",
        "in all directions",
        "woman",
        "twinkette",
        "gayest",
        "whatever",
        "you had fag"
        "female twink",
        "twink sissy tranny", # I'm assuming this is some hrt femboy situation
        "wife",
        "futch",
        "bian",
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

#TODO
def is_bi_or_pan(input_str:str):
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
def is_ace_or_aro(input_str:str):
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