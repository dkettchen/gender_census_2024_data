def is_cis(input_str:str):
    """
    takes a string

    returns True if it denotes cis gender
    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "cis" not in lower_str:
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "not cis",
        "not-cis",
        "non-cis",
        "trans",
        "cisn't",
        "everything but normative cis man",
        "in a cismale way",
        "intersex",
        "cis people",
        "not entirely",
        "not quite",
        "assumed",
        "passing",
        "cisdissident",
        "cis privilege",
        "internally", # what this mean bro
        "nicht cis-hetero", # thank gosh I speak german smh
        "noncis",
        "not!cis",
        "seen as",
        "as a cis person",
        "it ain't cis",
        "t4t", # can't be t4t if you're not t hun
        "not in a cis way",
        "cish ",
    ]:
        if item in lower_str:
            result_bool = False

    if lower_str == "cish":
        result_bool = False

    return result_bool

def is_binary(input_str:str):
    """
    takes a string

    returns True if it denotes binary gender
    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # input checking
    if "binary" not in lower_str:
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "outside",
        "extra",
        "gender binary",
        "binary spectrum",
        "of the binary",
        "nonbinary",
        "never binary",
        "can't understand binary",
        "not both binary genders",
        "ain't binary",
        "mid",
        "binary broken",
        "binary lie",
        "non-binary",
        "non binary",
        "of binary gender",
        "beyond",
        "too early",
        "is fake",
        "removed from",
        "not entirely binary",
        "not in the binary",
        "not very binary",
        "philosophically opposed",
        
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool


# can't we just cross reference these with the male/female categories?
    # I saw some "cis femme" type mentions but idk what they mean by that clearly enough to use it decisively
#TODO
def is_cismale(input_str:str):
    pass

#TODO
def is_cisfemale(input_str:str):
    pass