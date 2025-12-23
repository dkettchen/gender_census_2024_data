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

    # reinclude
    for item in [
        "fat dyke",
        "art dyke",
    ]:
        if item in lower_str:
            result_bool = True

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

    # reinclude
    for item in [
        "i'm gay, and i like men, so whatever that makes me",
    ]:
        if item in lower_str:
            result_bool = True

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

    # reinclude
    for item in [
        "in a man's body",
        "boyish lesbian",
    ]:
        if item in lower_str:
            result_bool = True

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


def is_conflicting_queer(input_str:str):
    """
    takes a string

    returns True if it denotes any conflicting combo (ie lesbianism for men, 
    faggotry for women, both mlm and wlw) of the various other queer labels

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # excluding all single label items
    if is_butch(input_str) or is_bear(input_str) \
    or is_achillean(input_str) or is_dyke(input_str) \
    or is_fag(input_str) or is_gay(input_str) \
    or is_lesbian(input_str) or is_homosexual(input_str) \
    or is_sapphic(input_str) or is_twink(input_str):
        return False

    result_bool = True
    
    # excluding stuff
    for item in [
        "in spirit",
        "neither gay nor a man",
        "teddy bear",
        "teddybear",
        "(like the animal)",
        "build-a-bear",
        "is gay",
        "by way of",
        "in a gay man way",
        "genderless amalgamation of flesh",
        "with the lesbians",
        "(though I am not a lesbian)",
        "coded",
        "are attracted to me",
        "mama bear",
        "otter",
        "whatever makes you",
        "is inherently gay",
        "culturally",
        "emotionally hetero",
        "of dyke experience",
        "futch",
        "hermaphrodyke",
        "i kinda wish i was a boy but still a lesbian",
        "you're gay",
        "it's not gay to like they",
        "like a nonbinary lesbian but the other way",
        "like if a dyke and a faggot had a baby",
        "of lesbian origin",
        "not butch but i respect their beliefs",
        "polar bear",
        "of butch experience",
        "what ever makes",
        "whatever gender makes",
        "whatever makes",
        "where is dyke",
        "why is fag on the list but not dyke",
        "lesbian but in a yaoi way", # this just has no overlap, like- there are no lesbians in yaoi?? wym??
        "t dyke", # t dyke might be tgirl dyke, not transmasc 🤔
        "t-dyke",
        "boy but in a fem way",
        "femtransboy",
        "boyfem",
        "fem and masc but neither boy or girl",
        "femhemidemisemiboy",
        "fem boy",
    ]:
        if item in lower_str:
            result_bool = False
    
    if "fembo" in lower_str: # exclude femboys except for conflicted ones
        result_bool = False
        for item in [
            "hrt",
            "she/her",
            "woman",
            "girl",
            "male to female",
            "not a boy",
            "butch",
        ]:
            if item in lower_str:
                result_bool = True

    return result_bool

def is_lesbianism_for_men(input_str:str):
    """
    takes a string

    returns True if it denotes any conflicting combo of wlw language and male/male_aligned 
    (incl transmasc (as denotes explicit non-cis/non-femaleness) but excl unspecific nb 
    (as may be transfemme or cis-leaning)) identity

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    if is_conflicting_queer(input_str):
        result_bool = True
    else: return False
    
    # excluding stuff
    for item in [
        "fag",
        "gay",
        "female twink",
        "manwoman",
        "direction",
        "girl",
        "twinkette",
        "(though i am not a lesbian)",
        "mix between fem twink and butch lesbian",
        "shebear",
        "sissy", # bc largely amab crossdressers leaning toward transfemme
        "fembo",
        'she/her',
    ]:
        if item in lower_str:
            result_bool = False

    # reincluding
    for item in [
        "butchfemboy",
        "butch femboy",
        "if a femboy were butch",
    ]:
        if item in lower_str:
            result_bool = True

    return result_bool

def is_faggotry_for_women(input_str:str):
    """
    takes a string

    returns True if it denotes any conflicting combo of mlm language and female/female_aligned 
    (incl transfemme (as denotes explicit non-cis/non-maleness) but excl unspecific nb 
    (as may be transmasc or cis-leaning)) identity

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    if is_conflicting_queer(input_str):
        result_bool = True
    else: return False
    
    if is_lesbianism_for_men(input_str):
        return False

    # excluding stuff
    for item in [
        "dyke",
        "butch",
        "bian",
        "boygirl",
        "direction",
        "both ways",
        "for everyone",
        "gayboy, gaygirl",
        "lesb",
        "boy but in a fem way",
        "femtransboy",
        "boyfem",
        "fem and masc but neither boy or girl",
        "fem boy",
        "femhemidemisemiboy",
    ]:
        if item in lower_str:
            result_bool = False

    for item in [
        "femboygirl",
    ]:
        if item in lower_str:
            result_bool = True


    return result_bool

def is_dykefag(input_str:str):
    """
    takes a string

    returns True if it denotes any conflicting combos of mlm & wlw language 
    that cannot be discerned as male/wlw or female/mlm aligned (ie dykefag 
    -> are u claiming to be a faggy dyke or a dykey fag?? idk!)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    if is_conflicting_queer(input_str):
        result_bool = True
    else: return False

    if is_faggotry_for_women(input_str) or is_lesbianism_for_men(input_str):
        return False
    
    # excluding stuff
    for item in [
        "(though I am not a lesbian)",
        "fembo",
        "fem bo",
        "boy but in a fem way",
        "femtransboy",
        "boyfem",
        "fem and masc but neither boy or girl",
        "femhemidemisemiboy",
    ]:
        if item in lower_str:
            result_bool = False

    return result_bool


def is_bi_pan(input_str:str):
    """
    takes a string

    returns True if it denotes polysexuality (bi/pan/etc)

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "a bit of both (both being female and non-binary)",
        "lesbian (sexuality)",
        "n.bi",
        "nobi",
        "panadox (pangender + agender in a paradoxical way)",
        "tr*nssexual",
        "bi-gender",
        "bi-sex/bi-sexed",
        "lesbian gender , t4t sexuality",
        "gendergrey",
        "greygender",
        "grey gender",
        "grey-gender",
        "greygender",
        "gendergray",
        "graygender",
        "gray gender",
        "gray-gender",
        "graygender",
        "boygray",
        "gray agender",
        "grey agender",
        "pan gender",

        "ace",
        "aro",
        "asexual",
        "demi",
    ]:
        if item in lower_str:
            result_bool = False
    
    if lower_str in [
        "bisex",
        "panfemme",
        "grey",
        "gray",
    ]:
        result_bool = False

    return result_bool

def is_ace_aro(input_str:str):
    """
    takes a string

    returns True if it denotes ace aro spec

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True
    
    # excluding stuff
    for item in [
        "a bit of both (both being female and non-binary)",
        "lesbian (sexuality)",
        "n.bi",
        "nobi",
        "panadox (pangender + agender in a paradoxical way)",
        "tr*nssexual",
        "bi-gender",
        "bi-sex/bi-sexed",
        "lesbian gender , t4t sexuality",
        "gendergrey",
        "greygender",
        "grey gender",
        "grey-gender",
        "greygender",
        "gendergray",
        "graygender",
        "gray gender",
        "gray-gender",
        "graygender",
        "boygray",
        "gray agender",
        "grey agender",

        "demigirl",
        "demi girl",
        "demi-boy",
        "emiboy",
        "demiboi",
        "demi woman",
        "demi-woman",
        "demiwoman",
        "demi-ma",
        "demima",
        "demi ma",
        "demiguy",
        "demilady",
        "demi gender",
        "demigender",
        "demi-cis",
        "demicis",
        "demi-f",
        "demi-trigender",
        "demiagender",
        "demiandrogyn",
        "demiqndrogyne",
        "demiapora",
        "demicass",
        "demienby",
        "demif",
        "demixenogender",
        "demirosboy",
        "demi duo",
        "demi flux",
        "demi guy",
        "demi-dyke",
        "demi-xyrl",
        "demi-agender",
        "demi-androgyne",
        "demi-creature",
        "demi-gender",
        "demibro",
        "demidude",
        "demigal",
        "demineutrois",

        "bi",
        "pan",
        "duosexual",
        "polysexual",
    ]:
        if item in lower_str:
            result_bool = False
    
    if lower_str in [
        "bisex",
        "panfemme",
        "grey",
        "gray",
        "demi",
    ]:
        result_bool = False

    return result_bool

