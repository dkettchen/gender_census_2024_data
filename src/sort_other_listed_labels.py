def is_genderqueer(input_str:str):
    """
    takes a string

    returns True if it denotes genderqueerness

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # verifying input
    if "gender" in lower_str and "queer" in lower_str:
        result_bool = True
    else:
        return False
    
    # excluding stuff
    for item in [
        "queergender",
        "queer-gender",
        "queer gender",
        "queer (not just",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_genderfluid(input_str:str):
    """
    takes a string

    returns True if it denotes gender fluidity

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # verifying input
    if "fluid" in lower_str:
        result_bool = True
    else:
        return False
    
    # excluding stuff
    for item in [
        "present",
        "express",
        "isn't fluid",
        "some fluidity of",
        "ran out of gender fluid",
        "intensity of gender feelings are fluid",
        "my gender is blinker fluid",
        "(doesnt really fit but i like the label)", # then don't write it in omg
        "my self description is fluid",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_genderflux(input_str:str):
    """
    takes a string

    returns True if it denotes any form of gender flux
    (currently redundant as all collected items pass)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # verifying input
    if "flux" in lower_str:
        result_bool = True
    else:
        return False
    
    # excluding stuff
    for item in [

    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_queer(input_str:str):
    """
    takes a string

    returns True if it denotes comfort calling oneself queer

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    if is_genderqueer(input_str): # if it was just caught on genderqueer
        return False 

    # verifying input
    if "queer" in lower_str:
        result_bool = True
    else:
        return False
    
    # excluding stuff
    for item in [
        "alternative to queer",
        "queer way", # not the word itself
        "queer theory",
        "coded", # queer coded not the word itself
        "queering",
        "queerly",
        "queer-gender",
        "queergender",
        "queer gender",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool

def is_gnc(input_str:str):
    """
    takes a string

    returns True if it denotes gnc-ity 
    (currently redundant as all collected items pass)

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

def is_nb(input_str:str):
    """
    takes a string

    returns True if it denotes a nonbinary labelled identity

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "binary-nonbinary binary",
        "opposite of nonbinary",
        "none gender left binary",
        "outside the concept of nonbinary",
        "not binary but also not nonbinary", # not how words work but knock yourself out
        "she / they but not in a nonbinary way",
        "by identifier",
        "by my job description (eg. engineer, or baker)",
        "by name",
        "by self-pronouns: myself, me, i, etc",
        "byy",
        "ftenby trans person who's not actually ftenby",
        "futa", # idk what this is
        "(by only close friends)",
        "not always enby",
        "not binary or nonbinary",
        "not nonbinary",
        "not quite nonbinary",
        "unbothered by ", # dunno why this ain't catching smh
    ]:
        if item in lower_str:
            result_bool = False

    if item == "nonboy":
        return False

    return result_bool