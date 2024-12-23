#TODO: 
# add keys for race mentions ✅
# add keys for pronouns other than they/them ✅

from utils.key_word_catches import words_catching
from re import split

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
        
        ("gender", "queer"),"fluid","flux",
        ("gender", "non", "conforming"),"snc","gnc",
        
        ("trans", "masc"),
        ("trans", "fem"),
        ("trans", "man"),
        ("trans", "woman"),
        ("trans", "guy"),
        ("trans", "girl"),
        "transv","cross","drag","trav","panto","principal boy",
        "sissy",
        "tran", ("tr","nny"), # tryna catch slurs too
        "queen", # leaving this separate due to gay connotation

        "girl","woman","lady","gal","female","chic","maiden",
        ("ma","am"),"mom","mum","miss","ms","daughter","sister","gxrl","wxman","womxn",

        "guy","dude","boy","boi","bot","man","male","sir","lad","lord",
        "dad","mr","mister","son","bro","bloke","bxy","bruv",

        "afab","dfab",
        "amab","dmab",
        "ftm","mtf",
        "question",
        'nonbinary','enby',("non", "bin"),"nb",
        'queer',
        'name',
        "me",
        'agender',
        'bigender',
        'binary',
        'butch',"tom","azur","masc",
        "fem","ros","pretty","cute","flamboyant",
        "futch",
        'cis',
        'demiboy',
        'demigirl',
        ("fag","dyke"),
        "dyke",
        "lesb","lez","les",
        "sapph",
        "fag","gay","achillean","homo"
        "xeno",
        "auti",
        "system","plural","did","alter",
        ("a","hd"),"neuro","nuro",
        "both","neither",
        ("fem", "boy"),("fem", "boi"),
        "they","them",
        "twink",
        "bear",
        "half",
        "thing",
        "intersex","herm",
        "sexual","bi","pan","ace","aro","roman",
        "andro",
        "neut",
        "dysp",
        ("2","spirit"),("two","spirit"),
        "none",
        "no",
        "other",
        "demi",
        "sex",
        "trap",
        "gender", # this gets us a solid 2k extra catches atm 

        "black",("n","gga"), # I saw the n word in there somewhere
        "sian", # to catch gaysian etc too
        "brown", 
        "of color", "of colour", "woc", "moc", "poc",
        "white", # I've seen too many white mentions by now to not include it I guess

        "muslim", # I've seen a muslim mention!
        "jew", # there was a jew mention too
        'romani',
        "eastern european", # why 
        
        "she","her",
        "he","him",

        "testo", "estro", "hrt", "horm",
    ]

    # do we want to add more items?
        # alt words like punk -core etc?
        # stud (and other words for gnc & queer folks we may have overlooked so far)
        # ladyboy maybe bc a known word also joso? hijra?
        # hormone info "hormone", "puberty", "hrt"
        # add principal boy to crossdressers
        # ex, former, once, etc -> denoting transition away from (there were others too)
        # find colours for anyone who decides to describe middle or third option 
            # using purple or yellow or green (maybe look for red, pink, blue too)

    # make dict
    category_dict = {}

    # counting what remains
    left_overs = 0
    skip_overs = 0

    # iterate over input list
    for item in input_list:

        # skip items that are too long
            # no time for yappers
            # no time for jokesters
        if len(item) > 50 \
        or "joke" in item.lower() \
        or "joking" in item.lower() \
        or "sarca" in item.lower(): 
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
            elif key_word == "flux":
                umbrella_word = "genderflux"
            elif key_word in [("gender", "non", "conforming"), "snc"]:
                umbrella_word = "gnc"
            elif key_word == "auti":
                umbrella_word = "autism_related"
            elif key_word in [("trans", "masc"),("trans", "man"),("trans", "guy"),"ftm"]:
                umbrella_word = "transmasc"
            elif key_word in [("trans", "fem"),("trans", "woman"),("trans", "girl"),"mtf"]:
                umbrella_word = "transfemme"
            elif key_word in ["transv", "cross", "drag", "trav","panto","principal boy",]: # "or" ones can just be strings
                umbrella_word = "crossdresser"
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
            elif key_word in ['butch',"tom","azur","masc",]:
                umbrella_word = "masc"
            elif key_word in ["fem","ros","pretty","cute","flamboyant",]:
                umbrella_word = "femme"
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
            elif key_word in ["she","her"]:
                umbrella_word = "she/her"
            elif key_word in ["he","him"]:
                umbrella_word = "he/him"
            elif key_word in [
                "of color", "of colour", "woc", "moc", "poc",
                "black",("n","gga"),
                "sian",
                "brown",
            ]:
                umbrella_word = "POC_mention"
            elif key_word in ["jew", "muslim"]:
                umbrella_word = "religion_mention"
            elif key_word in [("fem", "boy"),("fem", "boi"),]:
                umbrella_word = "femboy"
            elif key_word in ["testo", "estro", "hrt", "horm",]:
                umbrella_word = "hormones"
            elif key_word in ["human","person","people",]:
                umbrella_word = "human/person"
            elif key_word in ["sexual","bi","pan","ace","aro","roman",]:
                umbrella_word = "sexuality_mention"
            else: umbrella_word = key_word # if it doesn't need to be different

            # words we don't mean that might catch on our key words!
            if key_word in words_catching:
                words_that_catch = words_catching[key_word]
            elif umbrella_word in words_catching: # for tuples
                words_that_catch = words_catching[umbrella_word]
            else:
                words_that_catch = []

            # find words 
            # save em under key

            # single key word
            if type(key_word) == str and key_word in lower_item:
                if umbrella_word not in category_dict.keys():
                    category_dict[umbrella_word] = []
                
                # we have detected key word in the item
                contains_key_word = True
                # but was it a wrong catch?
                for incorrect_word in words_that_catch:
                    # if the incorrect word is in the item
                    if incorrect_word in lower_item:
                        # we split at the incorrect word (eliminating it)
                        split_string = split(incorrect_word, lower_item)
                        # we don't know if it *also* contains our actual key word
                        contains_key_word = False
                        # we check every piece of the split string
                        for piece in split_string:
                            # if it still contains the word
                            if key_word in piece:
                                contains_key_word = True
                                break # we have located the correct word in this piece 
                                      # so it does contain it
                        break # we have located an incorrect word, 
                              # so don't need to check the others

                # if it does not contain the word outside of a wrongly caught word
                if not contains_key_word:
                    continue
                # otherwise it appends the item
                category_dict[umbrella_word].append(item)
                was_not_collected = False # has been collected

            # multiple keywords to combine
            elif type(key_word) == tuple:
                #TODO: implement the wrongly caught words code for tuples too

                if len(key_word) == 2 \
                and (key_word[0] in lower_item \
                and key_word[1] in lower_item):
                    if umbrella_word not in category_dict.keys():
                        category_dict[umbrella_word] = []

                    # we have detected key word in the item
                    contains_key_word_1 = True
                    contains_key_word_2 = True
                    # but was it a wrong catch?
                    for incorrect_word in words_that_catch:
                        # if the incorrect word is in the item
                        if incorrect_word in lower_item:
                            # we split at the incorrect word (eliminating it)
                            split_string = split(incorrect_word, lower_item)
                            # we don't know if it *also* contains our actual key word
                            contains_key_word_1 = False
                            contains_key_word_2 = False
                            # we check every piece of the split string
                            for piece in split_string:
                                # if it still contains the word
                                if key_word[0] in piece:
                                    contains_key_word_1 = True
                                if key_word[1] in piece:
                                    contains_key_word_2 = True
                                if contains_key_word_1 and contains_key_word_2:
                                    break # we have located the correct word in this piece 
                                        # so it does contain it
                            break # we have located an incorrect word, 
                                # so don't need to check the others

                    # if it does not contain the word outside of a wrongly caught word
                    if not contains_key_word_1 or not contains_key_word_2:
                        continue
                    # otherwise it appends the item
                    category_dict[umbrella_word].append(item)
                    was_not_collected = False # has been collected

                elif len(key_word) == 3 \
                and (key_word[0] in lower_item \
                and key_word[1] in lower_item \
                and key_word[2] in lower_item):
                    if umbrella_word not in category_dict.keys():
                        category_dict[umbrella_word] = []

                    # we have detected key word in the item
                    contains_key_word_1 = True
                    contains_key_word_2 = True
                    contains_key_word_3 = True
                    # but was it a wrong catch?
                    for incorrect_word in words_that_catch:
                        # if the incorrect word is in the item
                        if incorrect_word in lower_item:
                            # we split at the incorrect word (eliminating it)
                            split_string = split(incorrect_word, lower_item)
                            # we don't know if it *also* contains our actual key word
                            contains_key_word_1 = False
                            contains_key_word_2 = False
                            contains_key_word_3 = False
                            # we check every piece of the split string
                            for piece in split_string:
                                # if it still contains the word
                                if key_word[0] in piece:
                                    contains_key_word_1 = True
                                if key_word[1] in piece:
                                    contains_key_word_2 = True
                                if key_word[1] in piece:
                                    contains_key_word_3 = True
                                if contains_key_word_1 and contains_key_word_2 and contains_key_word_3:
                                    break # we have located the correct word in this piece 
                                        # so it does contain it
                            break # we have located an incorrect word, 
                                # so don't need to check the others

                    # if it does not contain the word outside of a wrongly caught word
                    if not contains_key_word_1 or not contains_key_word_2 or not contains_key_word_3:
                        continue
                    # otherwise it appends the item
                    category_dict[umbrella_word].append(item)
                    was_not_collected = False # has been collected

        if was_not_collected:
            left_overs += 1

    # return dict
    return category_dict
