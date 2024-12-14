#TODO: 
# add keys for race mentions ✅
# add keys for pronouns other than they/them ✅

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
        "ftm","mtf",
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
        "dyke",
        "lesb","lez","les",
        "sapph",
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
        "gender", # this gets us a solid 2k extra catches atm 

        "black",("n","gga"), # I saw the n word in there somewhere
        "sian", # to catch gaysian etc too
        "she","her",
        "he","him",
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
            elif key_word in ["black", ("n","gga")]:
                umbrella_word = "black"
            elif key_word == "sian":
                umbrella_word = "asian"
            elif key_word in ["she","her"]:
                umbrella_word = "she/her"
            elif key_word in ["he","him"]:
                umbrella_word = "he/him"
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
