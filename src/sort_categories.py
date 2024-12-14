from copy import deepcopy

#TODO:
# men's func:
    # print to check values & build up if statements to sort them
    # are there any other categories we should be collecting?
# make funcs for other categories
    # start w ones that we need for cross referencing (ie women, various adjectives)

# ✅
def is_male_aligned(input_str:str):
    """
    takes a string

    checks if the gender it describes qualifies as explicitly male-aligned 
    (ie "A trans dude", "feminine guy", "boy but in a fruity way", etc)

    if so returns True

    else returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # things we're excluding
    for item in [
        "girl",
        "woman",
        "female",
        "sister",
        "but not",
        "neutral",
        "genderless",
        "lesb",
        "sbian",
        "dyke",
        "nor a man",
        "but also not",
        "child identified",
        "b.o.b",
        "gurl",
        "gxrl",
        "grl",
        "mom",
        "not a man",
        'never a "man"',
        "butch",
        "kisser",
        "dress like a teenage boy",
        "not a boy",
        "not a guy",
        "potheads",
        "chick",
        "everything but",
        "everything except",
        "tomboy", # was caught in conjunction with femboy
        "male-bodied",
        "not male",
        "ungendered",
        "nongendered",
        "non-gender-specific",
        "non-gendered",
        "but technically not",
        "boy parts",
        "seem like a guy",
        "don't (usually) feel like a man",
        "but my feeling is different",
        "idk",
        "don't know",
        "don't even know",
        "don't fuckin know",
        "don't want to be a man",
        "presenting as a man",
        "draw, man",
        "raised male",
        "i'm a boy because i was  born afab", # bitches be confused idk
        "like if there was a guy", # what does this mean
        "not a trans man",
        "milf",
        "women",
        "just me man",
        "a boy day",
        "gal",
        'male impersonater', 
        'male presenting', 
        'male-trending', 
        'man-maiden', 
        "male hormones",
        "mannish",
        "mrs",
        "miss",
        "nonboy",
        "not boy",
        "not-boy",
        "not male",
        'not-male',
        "not-man",
        "not man",
        "nonman",
        "not quite",
        "not really",
        "never a man",
        "don't think i am",
        "male agenda",
        "concept of being a guy",
        "+ bot",
        "robotgender",
        "sapph",
        "calls his truck she",
        "she's my boyfriend",
        "other than a man",
        "daughter",
        "outside the boy box",
        'temporary', 
        "absence of man",
        'tom boy', 
        'boy shaped', 
        "wouldn't you like to know",
        "rhetorical",
        'amab trans boy',
        "anything but",
        "alternating tuesdays",
        "but only",
        "boyish",
        "boyn't",
        "not gender specific",
        "just work here",
        "trans guy who's not actually ftm",
        "fuck if i know",
        "girboylent",
        "lady",
        "ice bot",
        "transmasc guy was also transfem",
        "clusters",
        "pantomime principal boy",
        "dragoness",
        'male is my government gender', 
        'male on paper', 
        "socialised",
        "never a boy",
        "never felt comfortable"
        'one of the guys',
        'post-male', 
        "she's the man", 
        'hrt fem"boy"',
        "sheboy",
        'tom-femboy', 
        'transfem boy', 
        "hrt-femboy",
        'whatever man', 
    ]:
        if item in lower_str:
            return False

    # if none of these things are in the string => it qualifies
    return True

#TODO:
def is_non_male_aligned(input_str:str):
    """
    takes a string

    checks if the gender it describes qualifies as explicitly non-male aligned
    (ie "definitely not a man", etc)

    if so returns True

    else returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # non-male aligned must not be in the male-aligned group
    if is_male_aligned(input_str):
        return False

    # => we only need to look at leftovers!

    # things we're excluding
    for item in []:

        if item in lower_str:
            return False

    # if none of these things are in the string => it qualifies
    return True

#TODO: this one after non-male aligned (so we can use it to exclude stuff)
def is_conflicted_male_aligned(input_str:str):
    """
    takes a string

    checks if the gender it describes explicitly mentions male-aligned language but does 
    not seem to be able to make up its mind/commit to it (ie "a guy but not a man", "boy dyke", etc) 
    but is not a more unaligned conflicting statement (ie "100% man and 100% woman")

    if so returns True

    else returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # conflicted must not be in the explicitly male-aligned group
    if is_male_aligned(input_str):
        return False
    
    # conflicted must not be in the explicitly non_male-aligned group
    if is_non_male_aligned(input_str):
        return False

    # => we only need to look at leftovers!

    # things we're excluding
    for item in []:

        if item in lower_str:
            return False

    # if none of these things are in the string => it qualifies
    return True


#TODO repeat for female aligned items (female-aligned, non-female aligned, conflicted female aligned)

#TODO afterwards, do for other categories


#TODO: make a helper func to dispense the correct function based on data case! ✅
def checking_func_dispenser(data_case:str):
    """
    returns appropriate helper function depending on data case
    """
    if data_case == "male_aligned":
        return is_male_aligned
    elif data_case == "non_male_aligned":
        return is_non_male_aligned
    elif data_case == "conflicted_male_aligned":
        return is_conflicted_male_aligned

#TODO: continue adding new implemented data_cases to doc string
def find_case(input_list:list, data_case:str):
    """
    takes the list value of the relevant key from the initially collected dict and a relevant data_case
    (ie man/boy/male key's list value & "male_aligned" data_case to find all male_aligned items in it)

    returns a new list with only the relevant items remaining, 
    according to the data_case's relevant helper function's criteria

    currently implemented data_cases (using corresponding helper functions):
        - data_case="male_aligned"
        - data_case="non_male_aligned"
        - data_case="conflicted_male_aligned"

    """

    output_list = []

    checking_func = checking_func_dispenser(data_case) # variable function for relevant conditions

    # check words in input list
    for item in sorted(list(set(input_list))):
        # if they fit criteria for being counted 
        if checking_func(item):
            # they are added to output list
            output_list.append(item)

    return output_list



