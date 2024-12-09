from src.read_txt import read_txt

def clean_data(data_case:str):
    input_list = read_txt(data_case) # retrieving data in function
    # categorised = []
    # for cate in cat[data_case]: # what we've already categorised
    #     categorised += cat[data_case][cate] # unpacking all the lists into one big one

    if data_case == "q2": # custom/unlisted words/phrases/labels

        most_columns = [
            'me',
            'my name',
            'a person',
            'person',
            'a human',
            'human',
            'agender',
            'bigender',
            'binary',
            'butch',
            'cisgender',
            'demiboy',
            'demigirl',
            'enby',
            'fag',
            'gender non-conforming',
            'genderfluid',
            'genderqueer',
            'nonbinary',
            'queer',
            'questioning',
            'trans',
            'transfeminine',
            'transgender',
            'transmasculine',
            'none',
        ]
        
        # other stuff to check for: 
        # anything above a certain letter count can go in yappers to be rid of it ✅
        # case insensitive versions of everything in most_columns ✅
        # gender + fluid ✅ / flux  📌
        # dyke / lesbian / sapphic ✅
        # fag 📌 / gay ✅
        # tranny (remainder) 📌
        # butch ✅ / femi(nine) 📌 / masc 📌 / andro(gynous/gyne/etc) 📌
        # xeno (just to have that out the way) 📌
        # quest(ioning) 📌
        # woman 📌, girl 📌, lady 📌, gal, female 📌, etc
        # man 📌, boy 📌, boi 📌, guy 📌, dude 📌, male 📌, etc (bot 📌 bc common mispelling of boy)
        # afab 📌 / amab 📌 / agab 📌 / intersex 📌 / herm(aphrodite) 📌
        # drag 📌 / cross(dresser) 📌 / transv(estite) 📌
        # queer (remainder) 📌
        # neuro(diversity) 📌
        # DID 📌 / plural 📌 / system 📌 / front / us/we (I wanna track DID folks where we have info on em)
        # they / them 📌, he / him, she / her -> check for pronouns bc some ppl include those in labels/phrases
        # cis 📌
        # bi
        # agender 📌
        # both 📌 & neither 📌
        # trans / mtf 📌 / ftm 📌 / fte / ftx 📌 / transmasc 📌 / transfem 📌
        # nonbinary 📌, enby 📌, non + binary 📌 / x + gender 📌
        # binary 📌
        # remaining "no" stuff (not, no, none mentions)
        # creature 📌 / thing / etc
        # human / person
        # 
        # at the very end: gender -> to see how many are left

        # this is not an efficient way of doing this:
            # do it programmatically & build in exceptions to sort cases automatically!

        #TODO: 
        # - separate each section into its own function for ease of organisation
        # - check for racial words bc I know I've seen black & the n word in there
            # check for asians too, but using keyword "sian" bc we wanna catch gaysian too
            # -> to count toward my argument of "other intersections make standard 
            # gender roles harder to process and/or relate to" 
        # - place sorting functions in a way that'll ripple down (ex sorting through 
        # male *before* using it to collect adjectives etc)
        # - collect remaining catches somehow to look through later
        
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
            "system","plural","did",
            ("a","hd"),"neuro","nuro"
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

        # collecting initial values using key words

        # make a dict
        category_dict = {}

        # counting what remains
        left_overs = 0
        skip_overs = 0

        # iterate over list
        for item in input_list:
            if len(item) > 50: # no time for yappers
                skip_overs += 1
                continue

            lower_item = item.lower()

            # keeping track of what was collected
            was_not_collected = True

            for key_word in key_word_list:

                #setting umbrella terms for tuple ones
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

                # if statements

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

        for key in category_dict: # sorting & making sure we don't have duplicates in key values
            current_list = category_dict[key]
            sorted_list = sorted(list(set(current_list)))
            category_dict[key] = sorted_list
        
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
                if item in category_dict["man/boy/male"] and item in category_dict[label]:
                    if item in category_dict["woman/girl/female"]: # if it caught on woMAN
                        continue
                    category = f"{label} man"
                elif item in category_dict['woman/girl/female'] and item in category_dict[label]:
                    category = f"{label} woman"
                else:
                    continue

                if category not in label_categories_dict.keys():
                    label_categories_dict[category] = []
                label_categories_dict[category].append(item)

            for known_birthsex in [ # finding birthsexes we know about
                ("afab", "transmasc", "cis woman"),
                ("amab", "transfemme", "cis man")
            ]:
                if known_birthsex[0] not in label_categories_dict.keys():
                    label_categories_dict[known_birthsex[0]] = []

                if item in category_dict[known_birthsex[0]] \
                or item in category_dict[known_birthsex[1]] \
                or item in label_categories_dict[known_birthsex[2]]:
                    birthsex = known_birthsex[0]
                    label_categories_dict[birthsex].append(item)

            # finding boths?
            # both + anything that's in both male & female category

            # finding male/female only items -> anything that isn't in both

        print(sorted(category_dict.keys()))

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

        # counter = 0
        # for item in input_list:
        #     # (excluding the ones we've already collected)
        #     if item not in categorised \
        #     and len(item.lower()) < 100 \
        #     and ("bot" in item.lower()): #  and "gender" in item.lower()
        #         print(f'"{item}",')
        #         # counter += 1
        
                #drop if len(item.lower()) > 100 bc there's too many goddamn yappers in here smh
        # print(len(categorised))
        # print(counter)

    elif data_case == "q4_1": # a title not listed here (abbr)
        pass
    elif data_case == "q4_2": # a title not listed here (full)
        pass
    elif data_case == "q4_3": # a title not listed here (pronunciation)
        pass
    elif data_case == "q8": # title not listed that u want ppl to use
        pass
    elif data_case == "q35": # custom family mess
        pass
    elif data_case == "q37": # how did u find this survey
        pass


    pass

if __name__ == "__main__":
    for data_case in ["q2","q4_1","q4_2","q4_3","q8","q35","q37"]:
        if data_case != "q2":
            continue
        cleaned_data = clean_data(data_case)