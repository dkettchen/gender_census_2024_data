from utils.read_txt import read_txt
from copy import deepcopy

input_list = read_txt("q2") # retrieving data in function

def collect_key_words_from_q2(input_list):
    """
    takes a list of custom gender label strings (question 2)

    returns a dictionary with a variety of keys collecting all custom input labels 
    containing relevant word bits and below 50 characters in length
    """

    # key words we'll be finding
    key_word_list = [
        "human","person","people",
        "creature",
        "auti",
        ("gender", "queer"),"fluid",
        ("gender", "non", "conforming"),
        "gnc",
        ("non", "bin"),
        ("trans", "masc"),
        ("trans", "fem"),
        ("trans", "man"),
        ("trans", "woman"),
        ("trans", "guy"),
        ("trans", "girl"),
        "transv","cross","drag","trav",
        "tran", ("tr","nny"), # tryna catch slurs too
        "girl","woman","lady","gal","female","chic","maiden",
        ("ma","am"),"mom","mum","miss","ms","daughter","sister","gxrl","wxman","womxn",
        "guy","dude","boy","boi","bot","man","male","sir","lad","lord",
        "dad","mr","mister","son","bro","bloke","bxy","bruv",
        "afab","dfab",
        "amab","dmab",
        "ftm",
        "mtf",
        "question",
        'nonbinary','enby',
        'queer',
        'name',
        "me",
        'agender',
        'bigender',
        'binary',
        'butch',"tomboy",
        "femi","femm",
        "masc",
        'cis',
        'demiboy',
        'demigirl',
        ("fag","dyke"),
        "dyke","lesb","lez","les","sapph",
        "fag","gay","achillean","homo"
        "xeno",
        "flux",
        "system","plural","did","alter",
        ("a","hd"),"neuro","nuro",
        "both","neither",
        "femboy",
        "they","them",
        "twink",
        "bear",
        "half",
        "thing",
        "intersex","herm",
        "sexual",
        "andro",
        "neut",
        "dysp",
        ("2","spirit"),("two","spirit"),
        "none",
        "no",
        "other",
        "nb",
        "demi",
        "sex",
        "trap",
        "gender" # this gets us a solid 2k extra catches atm 
    ]

    # make dict
    category_dict = {}

    # counting what remains
    left_overs = 0
    skip_overs = 0

    # iterate over input list
    for item in input_list:

        # skip items that are too long
        if len(item) > 50: # no time for yappers
            skip_overs += 1
            continue

        # keeping track of what was collected
        was_not_collected = True

        # get case insensitive item
        lower_item = item.lower()

        # iterate over key words
        for key_word in key_word_list:

            # keys we'll be saving them under
            if key_word == ("gender", "queer"):
                umbrella_word = "genderqueer"
            elif key_word == "fluid":
                umbrella_word = "genderfluid"
            elif key_word == ("gender", "non", "conforming"):
                umbrella_word = "gnc"
            elif key_word == "auti":
                umbrella_word = "autism_related"
            elif key_word in [("trans", "masc"),("trans", "man"),("trans", "guy"),"ftm"]:
                umbrella_word = "transmasc"
            elif key_word in [("trans", "fem"),("trans", "woman"),("trans", "girl"),"mtf"]:
                umbrella_word = "transfemme"
            elif key_word in ["transv", "cross", "drag", "trav"]: # "or" ones can just be strings
                umbrella_word = "transvestite/crossdresser/drag"
            elif key_word in [
                "girl",
                "woman",
                "lady",
                "gal",
                "female",
                "chic",
                "maiden",
                ("ma","am"),
                "mom",
                "mum",
                "miss",
                "ms",
                "daughter",
                "sister",
                "gxrl",
                "wxman",
                "womxn",
            ]:
                umbrella_word = "woman/girl/female"
            elif key_word in [
                "guy",
                "dude",
                "boy",
                "boi",
                "bot",
                "man",
                "male",
                "sir",
                "lad",
                "lord",
                "dad",
                "mr",
                "mister",
                "son",
                "bro",
                "bloke",
                "bxy",
                "bruv",
            ]:
                umbrella_word = "man/boy/male"
            elif key_word == "question":
                umbrella_word = "questioning"
            elif key_word == ("fag","dyke"):
                umbrella_word = "fag_dyke"
            elif key_word in [("non","bin"),"enby","nb"]:
                umbrella_word = "nb"
            elif key_word in [
                "system",
                "plural",
                "did",
                "alter"
            ]:
                umbrella_word = "DID_related"
            elif key_word in [("a","hd"),"neuro","nuro"]:
                umbrella_word = "other_neurodiversity_related"
            elif key_word in ["tran", ("tr","nny")]:
                umbrella_word = "trans"
            elif key_word in ["femi", "femm"]:
                umbrella_word = "femme"
            elif key_word in ["lesb", "lez", "les",]: 
                umbrella_word = "lesbian"
            elif key_word == "sapph":
                umbrella_word = "sapphic"
            elif key_word in ["gay", "achillean", "homo", "fag", "twink", "bear"]:
                umbrella_word = "gay"
            elif key_word == "dfab":
                umbrella_word = "afab"
            elif key_word == "dmab":
                umbrella_word = "amab"
            elif key_word in ["they", "them"]:
                umbrella_word = "they/them"
            elif key_word == "people":
                umbrella_word = "person"
            elif key_word == "herm":
                umbrella_word = "hermaphrodite"
            elif key_word == "sexual":
                umbrella_word = "-sexual"
            elif key_word == "andro":
                umbrella_word = "androgynous"
            elif key_word == "neut":
                umbrella_word = "neutral"
            elif key_word == "dysp":
                umbrella_word = "dysphoric"
            elif key_word in [("2","spirit"),("two","spirit"),]:
                umbrella_word = "two-spirit"
            elif key_word in ["butch", "masc","tomboy",]:
                umbrella_word = "butch/masc/tomboy"
            else: umbrella_word = key_word # if it doesn't need to be different

            # find words 
            # save em under key

            # single key word
            if type(key_word) == str and key_word in lower_item:
                if umbrella_word not in category_dict.keys():
                    category_dict[umbrella_word] = []
                category_dict[umbrella_word].append(item)
                was_not_collected = False # has been collected

            # multiple keywords to combine
            elif type(key_word) == tuple:

                if len(key_word) == 2 \
                and (key_word[0] in lower_item \
                and key_word[1] in lower_item):
                    if umbrella_word not in category_dict.keys():
                        category_dict[umbrella_word] = []
                    category_dict[umbrella_word].append(item)
                    was_not_collected = False # has been collected

                elif len(key_word) == 3 \
                and (key_word[0] in lower_item \
                and key_word[1] in lower_item \
                and key_word[2] in lower_item):
                    if umbrella_word not in category_dict.keys():
                        category_dict[umbrella_word] = []
                    category_dict[umbrella_word].append(item)
                    was_not_collected = False # has been collected

        if was_not_collected:
            left_overs += 1

    # return dict
    return category_dict

def find_adj_men_n_women(new_dict, reference_dict, input_str):
    """
    takes 
    - a new dictionary one wants to update (can be empty)
    - a dictionary containing the raw categories to reference
    - a string to check

    returns a new copy of the new dict with the string added to any 
    "{adjective} {man/woman}" categories it fits into

    if the categories were not in the input new dict yet, they have been added
    """

    input_dict = deepcopy(new_dict)

    for label in [ # finding overlap between these labels & male/female categories
        "gnc", 
        "genderqueer", 
        "bigender", 
        "genderfluid", 
        "nonbinary", 
        "intersex",
        "trans",
        "gay",
        "lesbian",
        "dyke",
        "sapphic",
        "cis",
    ]:
        if input_str in reference_dict["man/boy/male"] and input_str in reference_dict[label]:
            if input_str in reference_dict["woman/girl/female"]: # if it caught on woMAN
                continue
            category = f"{label} man"
        elif input_str in reference_dict['woman/girl/female'] and input_str in reference_dict[label]:
            category = f"{label} woman"
        else:
            continue

        if category not in input_dict.keys():
            input_dict[category] = []
        input_dict[category].append(input_str)

        return input_dict


    #TODO: 
    # - separate each section into its own function for ease of organisation
    # - check for racial words bc I know I've seen black & the n word in there
        # check for asians too, but using keyword "sian" bc we wanna catch gaysian too
        # -> to count toward my argument of "other intersections make standard 
        # gender roles harder to process and/or relate to" 
    # - place sorting functions in a way that'll ripple down (ex sorting through 
    # male *before* using it to collect adjectives etc)
    # - collect remaining catches somehow to look through later

    # collecting initial values using key words

def find_known_birthsexes(new_dict, reference_dict, input_str):
    """
    takes 
    - a new dictionary one wants to update 
    (should already contain "cis man"/"cis woman" keys)
    - a dictionary containing the raw categories to reference 
    (should contain "afab"/"amab" and "transmasc"/"transfemme" keys)
    - a string to check

    returns a new copy of the new dict with the string added to the "afab"/"amab" keys 
    if it was in any of the relevant groups in the new & reference dict 
    (afab/amab, transmasc/transfemme, cis woman/man)

    if the "afab"/"amab" keys were not in the input new dict yet, they have been added

    if the string was not in any of the relevant keys 
    and the "afab"/"amab" keys were already contained, 
    the new dict will be returned unchanged
    """

    input_dict = deepcopy(new_dict)

    for known_birthsex in [ # finding birthsexes we know about
            ("afab", "transmasc", "cis woman"),
            ("amab", "transfemme", "cis man")
        ]:
            if known_birthsex[0] not in input_dict.keys():
                input_dict[known_birthsex[0]] = []

            if input_str in reference_dict[known_birthsex[0]] \
            or input_str in reference_dict[known_birthsex[1]] \
            or input_str in input_dict[known_birthsex[2]]:
                birthsex = known_birthsex[0]
                input_dict[birthsex].append(input_str)

    return input_dict

def cross_reference_narrow_down(input_dict, input_list):

    category_dict = deepcopy(input_dict)
    
    # for reference
    key_ref = [
        '-sexual', 
        'DID_related', 
        'afab', 
        'agender', 
        'amab', 
        'androgynous', 
        'autism_related', 
        'bigender', 
        'binary', 
        'butch/masc/tomboy', 
        'cis', 
        'creature', 
        'demi', 
        'demiboy', 
        'demigirl', 
        'dysphoric', 
        'fag_dyke', 
        'femboy', 
        'femme', 
        'flux', 
        'gay', 
        'gender', 
        'genderfluid', 
        'genderqueer', 
        'gnc', 
        'half', 
        'hermaphrodite', 
        'human', 
        'intersex',
        'lesbian',
        'sapphic',
        'dyke', 
        'man/boy/male', 
        'me', 
        'name', 
        'nb', 
        'neither', 
        'neutral', 
        'no', 
        'nonbinary', 
        'none', 
        'other', 
        'other_neurodiversity_related', 
        'person', 
        'queer', 
        'questioning', 
        'sex', 
        'they/them', 
        'thing', 
        'trans', 
        'transfemme', 
        'transmasc', 
        'transvestite/crossdresser/drag', 
        'trap', 
        'two-spirit', 
        'woman/girl/female'
    ]

    label_categories_dict = {} # cross referencing
    for item in input_list:

        # cross referencing various adjectives with male & female categories (ie "genderqueer man", etc)
        label_categories_dict = find_adj_men_n_women(label_categories_dict, category_dict, item)

        # locating known birtsex info via afab/amab, trans directions & cis men & women
        label_categories_dict = find_known_birthsexes(label_categories_dict, category_dict, item)

        # finding boths?
        # both + anything that's in both male & female category

        # finding male/female only items -> anything that isn't in both

    #print(sorted(category_dict.keys()))
    return label_categories_dict


def sort_men(input_dict): #WIP
    """
    removes unneeded/incorrect values from the "man/boy/male" key of the input_dict

    if they specify non-manhood specifically, void of other words to be caught on, 
    they will be added to a "non-man" key instead
    """

    category_dict = deepcopy(input_dict)

    men_list = category_dict["man/boy/male"]

    new_men = []
    non_men = []

    for item in men_list:
        # items that were caught by accident get dropped
            # f.e. we are collecting woman elsewhere already
        if "woman" in item:
            # print(item)
            continue

        # items that are negating manhood get collected on a new key
        if "not a man" in item:
            # print(item)
            non_men.append(item)

        # correct items get collected for new man key
        else:
            # print(item)
            new_men.append(item)
    
    category_dict["man/boy/male"] = new_men
    category_dict["non-men"] = non_men

    return category_dict


(# notes from earlier
    # print(len(input_list) - left_overs - skip_overs)
    # # we've collected about 10k unique entries to be sorted through now
    # print(skip_overs)
    # # we have just shy of 800 skips for yapping
    # print(left_overs)
    # # we have about 4600 leftovers that have no more reasonable inclusions to extract 
    # as far as I can tell from skimming em

        # etc
        # first put in all the diff main categories & then we can go through & fix things
        # could refactor if statements via keyword list w type checking
            # if it's a string, check if it's in the item
            # if it's a tuple of two, check if both are in the item
            # etc
        # make sure we descend in granularity/stuff that could get mixed up

        # if x word is in item
        # add to relevant key on dict
    # print key -> see if anything is amiss
        # if smth was caught erroneously: make a case to exclude that item/those items
    # repeat for all needed keys
    # -> this way we need to type a lil & read a bunch, rather than copy pasting everything!
)

