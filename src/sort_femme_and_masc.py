#TODO femme & masc
# needs to include various words like pretty, butch, rosboy (look up masc female equivalent), etc 

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
        "andro",
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
    ]:
        if item in lower_str:
            result_bool = False

    # reincluding transmascs
    for item in [
        "trans masc",
        "transmasc",
        "trans-masc",
    ]:
        if item in lower_str:
            result_bool = True

    # remove non-qualifying transmasc mentions
    for item in [
        "transmascfem",
        "transmascfemme",
    ]:
        if item in lower_str:
            result_bool = False
    
    return result_bool

# anything masc
def is_masc(input_str:str):

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    for item in [
        
    ]:
        if item in lower_str:
            result_bool = False
    
    return result_bool

# anything both
def is_futch(input_str:str):

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    for item in []:
        if item in lower_str:
            result_bool = False
    
    return result_bool