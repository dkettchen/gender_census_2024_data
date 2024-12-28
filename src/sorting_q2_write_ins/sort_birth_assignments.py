from utils.sorting_helpers import caught_wrong_word

# amab & afab ✅
def is_agab(input_str:str, data_case:str):
    """
    takes an input string and a data case string (data_case="amab|afab")

    returns true or false based on whether the string implies 
    the person is amab or afab
    """
    # making case insensitive
    lower_str = input_str.lower()

    result_bool = False

    # things that qualify it if included (to get rid of most other stuff)
    for item in [
        "raised",
        "born",
        "assigned",
        "birth",
        "child",
        "trans",
        "hrt",
        "ex",
        "former",
        "now",
        "cis",
        "biological",
        "horm",
        "physical",
        "body",
        "default",
        "inertia",
        "reluctance to change",
        "form",
        "sociali",
        "start",
        "closet", # implies pre transition so might be useful
        "aspiring",
        "wish",
        "want",
        "origin",
        "history",
        "future",
        "wanna",
        "mentally",
        "on my way to",

        "afab",
        "dfab",
        "ft",
        "f to",
        "female to",
        "bonus hole",
        "uterus",
        "womb",
        "pussy",
        "cunt",
        "on t",
        "was a girl",
        "seahorse", # mpreg innit
        "tboy",
        "tboi",
        "tguy",
        "c-boy", # assuming this is short for cunt
        "cboy",
        "t boy",
        "t guy",
        "t man",
        "t-boy",
        "vagi",
        "clit",
        "preg",
        "menstr",

        "amab",
        "dmab",
        "mt",
        "m to",
        "male to",
        "dick",
        "sack",
        "ball",
        "penis",
        "boy parts",
        "ladyboy", # explicitly transfemme term
        "tgirl",
        "t-girl",
        "t girl",


    ]:
        if item in lower_str:
            contains_word = True

            # checking we didn't caught the wrong thing by accident
            for key_and_catch in [ # I think this is how tuples work right??
                ("ft", "left"),
                ("ft", "fifth"),
                ("ex", "except"),
                ("ex", "sexual"),
                ("now", "know"),
                ("trans", "transcend"),
            ]:
                key_word = key_and_catch[0]
                catch_word = key_and_catch[1]
                if item == key_word and catch_word in lower_str: 
                    # we no longer know if it contains the word or if it's wrongly caught
                    contains_word = False

                    # check if it caught the wrong word
                    contains_word = caught_wrong_word(lower_str, key_word, catch_word)

            if not contains_word: # if it just caught "left"
                continue
            else:
                result_bool = True

    # general stuff to exclude for either case!
    if result_bool:
        for item in [
            "transv",
            "man child",
            "person of trans experience",
            "transgender tomboy",
            "intersex",
            "almost boy",
            "aspiring transsexual",
            "in relation to",
            "boy , but not man",
            "boylexic",
            "boyplex",
            "cat",
            "cistrans",
            "context-dependently transgender",
            "culturally afab", # you better be intersex mf or transitioned mtf as a toddler
            "demi-transbinary",
            "digi-trans",
            "discount",
            "don't want to transition",
            "but not boy",
            "everything but normative cis man",
            "refused female hormones", # not enough info may be intersex
            "evil trans",
            "in a cismale way", # does not say *they* are cis male
            "full medical transition completed",
            "gender non conforming black woman",
            "gender non-conforming female",
            "but boy",
            "on the outside",
            "sexual context",
            "hovering near trans",
            "i don't want to be a man",
            "dont want be read as female per default", # not enough info
            "just wanna play games and draw",
            "want to be cute", # "and a guy" -> not specific enough bc could be trans guy or cis femboy
            "wanna be her boyfriend",
            "not cis or trans",
            "sexy",
            "trans person",
            "boy was a girl",
            "guy was a girl",
            "i'm sure i'm not a trans man", # incredible unhelpful statement without other info bud
            "off wish",
            "it boy",
            "jewish woman",
            "that's anything but a girl",
            "kinda trans",
            "king of the crane machine", # how did you even get here
            "lived experience as a woman",
            "lost boy",
            "man-form",
            "maybe trans, i wonder a lot",
            "multitrans",
            "coolest boy",
            "cis nor trans",
            "exclusive",
            "left-boy",
            "left boy",
            "not a girl but i really wish i was", # I've decided the afabs be like 
                                        # "if only I could be a girl but alas god made me trans ToT"
                                        # so we can't be sure
            "not a woman but i wish i could have been one.",
            "not boy",
            "not cis not trans",
            "not entirely female physically",
            "not exactly trans but not exactly cis",
            "not woman, not man",
            "not yet transitioned",
            "not-cis woman", # ye olde is it a trans woman who doesn't like being called that
                            # or a cis woman who doesn't like being called that, we may never know 
            "pinwheeling transexual",
            "transhuman",
            "play a girl on tv", # I've seen many a trans woman play girls on tv so
            "questioning under the trans umbrella",
            "rat",
            "robot",
            "soft guy",
            "softbo",
            "female/male",
            "sometimes I just wanna be a dude man idk",
            "in the trans camp",
            "static",
            "straight man",
            "surfer dude imitator",
            "(transmisogyny affected)", # YOU PEOPLE ARE USELESS TO ME
            "(transmisogyny exempt)",
            "that guy",
            "scary transgender",
            "another me",
            "trans nonbinary is my",
            "trans tomboy?",
            "trans being",
            "bifauxnen", # idek
            "both ways", # no
            "trans but not quite",
            "trans fag",
            "trans folk",
            "trans ish",
            "trans mack",
            "trans neither",
            "neutral",
            "trans potato",
            "trans thing",
            "trans tomboy",
            "trans with commitment issues",
            "trans*",
            "trans-Femboy", # hrt femboy or transmasc femboy?
            "trans-cendent",
            "trans-questioning",
            "something-or-other",
            "trans/transgender",
            "transx",
            "transancient",
            "transandro",
            "transandrogyn",
            "transaporine",
            "transautistic (reclaimed)", # babe did anyone try and take it from you
            "transbeach",
            "transbian", # transmasc lesbians are ruining lesbianism for trans WOMEN smh
            "transbigender",
            "transenby",
            "transesque",
            "transex[ed]/[ual]",
            "transexpressive",
            "freak",
            "trash",
            "ginger",
            "transient",
            "transish",
            "transitioner",
            "transjester",
            "transkenous",
            "transmascfem",
            "transmeadow",
            "transn't",
            "neural",
            "nuetral", # spellinggggg
            "transoutherine",
            "transparent",
            "transsexual (occasionally)",
            "transsexual.",
            "species",
            "tidal",
            "transummer",
            "transwhatever",
            "wannabe femboy", # not enough info, even if likely amab
            "femboy aspiring",
            "from wish",
            "woman in shared experience",
            "inexhaustive",
            "woman through experience",
            "a secret third thing",
            "a wishful girl",
            "adult boy",
            "afab but not actually afab", # again unless ur intersex or mtf as a toddler there is no excuse
            "assumed to be a cis woman", # so maybe amab passing stealth
            "bisex",
            "born again girl", # what does this even meannnn
            "boy not man",
            "boy, but not man",
            "cis the same way a tomato is a fruit",
            "double trans",
            "external presentation trans",
            "extreme trans-neptunian object", # you are not space rocks, if you can FILL OUT A SURVEY, 
                                            # YOU ARE NOT SPACE ROCKS
            "female cis-genderless",
            "femme (without the trans)", # doesn't mean is transfemme who doesn't wanna be called that
            "ftm trans guy who's not actually ftm", # again unless ur intersex there is no excuse
            "full boy but with something extra in there",
            "future dad",
            "gender non-conforming woman",
            "gender nonconforming man",
            "girl (I wish...)",
            "girl in a trans way", # again there's afab nbs out there crazy enough for this
            "girl more often than not",
            "girl, but guy",
            "he/him but only to trans people",
            "heteroflexible (male presenting)", # now this could be a cis guy but eh
            "i want other people to think i'm a feminine guy",
            "if a man was on the clearance rack",
            "inter/trans",
            "itboy",
            "just a guy, just like",
            "large girl or extra large boy",
            "like if a girl wasn't exactly a girl",
            "like if a thing was a girl",
            "male to a first degree of approximation",
            "male to the left",
            "man (in a non-gendered context)",
            "masc (without the trans)",
            "mentally ill tranny demon hacker",
            "mentally transgender",
            "my gender is more trans than feminine",
            "nebula",
            "neither trans nor cis",
            "never fully female but on the rest of the spectrum",
            "non-binary transgender androgyne",
            "non-cisgender woman",
            "non-conforming male",
            "nonbinary in the sense of the trans/cis binary",
            "none gender left man",
            "none gender with left guy",
            "not a boy, but i play one on tv",
            "not binary trans",
            "not cis but not trans",
            "not fem but often a woman",
            "not man",
            "not quite trans'",
            "not-boy",
            "on the girl spectrum",
            "on the woman-spectrum",
            "one of them transes you hear about",
            "outside of the cis/trans binary",
            "part-time-trans",
            "performatively female",
            "queer trans nonbinary person",
            "retrotransgender",
            "rounds off to male, most of the time",
            "seen as a cis woman",
            "sexgirl",
            "slutboy",
            "soft bo",
            "some flavor of trans",
            "sometimes cis sometimes trans",
            "sometimes trans",
            "somewhere between cisgender and transgender",
            "somewhere on the man side of thinngs",
            "sysythenotstraightguyy",
            "the smartest man alive",
            "trans fuck",
            "trans history",
            "trans in a circle",
            "trans nonbinary person",
            "trans spectrum",
            "trans tiger",
            "trans-androgynous",
            "trans-effeminate",
            "trans-enby/trans-nonbibary",
            "trans-inclusive",
            "trans??",
            "transgender in my heart",
            "transistorosexual",
            "czech",
            "transkenoine",
            "miscellaneous",
            "(tme)",
            "transmulti",
            "transnetral",
            "transnetural",
            "menace",
            "transthemme",
            "transthing",
            "transwarp",
            "transy",
            "tris/trans-cis",
            "under the trans umbrella",
            "woman by experience, nonbinary by identity",
            "left guy",
            "(distinct from fag)",
            "a boy but girl",
            "almost girl",
            "almost-girl",
            "comet",
            "diet",
            "girl-not girl",
            "hot girl",
            "meat girl", # could be dick euphemism but I won't put my money on that
            "left girl",
            "not girl",
            "not-girl",
            "notgirl",
            "part-girl",
            "plant",
            "spiritually transfemme", # not a thing
            "trans-femme-tomboy-whatever",
            "transfemmasc",
            "transfemmemasc",
            "transfemasc",
            "transfemneumasc",
            "transneufemmasc",
            "transtransfem",
            "but not girl or ms",
            " at girl",
            "beast",
            "botgirl",
            "boy but girly",
            "dick/bitch (both)",
            "femininity in an amab way",
            "flamboyant girl",
            " but girl",
            "part girl part creature",
            "world's first cisgender trans woman", # idk what that means girl
            "afab/amab", # USELESS
            "transfemme/transmasc",
            "transfem transmasc",
            "if a transmasc guy was also transfem",
            "transfem in a transmasc way",
            "transfeminine in a transmasculine way",
            "transfeminine transmasc",
            "feminist",
            "transmasc but transfem in a way",
            "transmasc transfem",
            "transmasc transgirl",
            "wants a penis",
            "ball jointed",
            "ball of",
            "ball filled",
            "better than just dicks and clits",
            "we ball",
            "goofball",
            "with a penis", # doesn't guarantee natively
            "vagina wielder",
            "dickless!!",
            "don't be a dick",
            "dickhead",
            "sex dysphoric",
            "shapeshifting chaos fae",
        ]:
            if item in lower_str:
                result_bool = False
        
        for item in [
            "trans butch",
            "transbutch",
            "nonbinary trans",
            "trans nonbinary",
            "trans non-binary",
            "trans-nonbinary",
            "transnonbinary",
            "trans",
            "transexual",
            "transsex",
            "transsexed",
            "transsexual",
            "transgender",
            "a transgender",
            "atransgender", # why
            "transneu", # TIL neugender's neu is short for neutral/neutrois, not the german word for new
            "externally trans",
            "non-transitioning",
            "nonbinary/trans",
            "retrans",
            "retrans/retransitioned",
            "retransgender",
            "trans adjacent",
            "trans and feminine",
            "trans but not dysphoric",
            "trans dyke",
            "trans lesbian",
            "trans-nothing",
            "trans-sexual",
            "trans-sorta",
            "trans-whatever",
            "trans-dyke",
            "transnb",
            "trans enby",
            "transadrogynous",
            "transbifag",
            "transdrogynous",
            "transdyke",
            "transeffeminate",
            "transex",
            "transfag",
            "transfagdyke",
            "transfaggotry",
            "transfaglesb",
            "transfloral",
            "transfur",
            "transgender butch",
            "transgendered",
            "transgenderfluid",
            "transgenderist",
            "transgenderless",
            "translesbian",
            "transmav",
            "transnon-binary",
            "transnull",
            "transomnine",
            "transperson",
            "transsexual/transexual",
            "transsexuel",
            "not a trans woman",
            "somewhat girl",
            "detrans", # add useable ones back in later
            "detransitioned",
            "detransitioning",
            "of detrans experience",
            "detransfem", # idk what this means
            "ball",
            "pussy",
            "pussy van faggot",
            "pussy gender",
            "cis t4t",
        ]:
            if item == lower_str: # if it needs to be exactly that 
                                    # bc there may be longer versions we wanna include
                result_bool = False
    
    # separating case specifics
    if data_case == "amab":
        if result_bool and is_agab(input_str, "afab"): 
            # if it's already in the afab list
            return False
            # otherwise it's true because we've sorted out all non-useable ones above already!
        for item in [
            "cunt",
            

        ]:
            if item in lower_str:
                result_bool = False

    elif data_case == "afab":
        if result_bool:
            # things to exclude
            for item in [
                "amab",
                "dmab",
                "dick",
                "sack",
                "balls",
                "boy parts",
                "ladyboy", # explicitly transfemme term
                "tgirl",
                "t-girl",
                "t girl",
                "trans girl",
                "trans woman",
                "mtf", # gotta re-find the detransitioners later tho
                "male to female",
                "transfem",
                "trans fem",
                "as child identified as male",
                "wish i was a woman",
                "i'm a boy because i was  born afab,", # I think this is just missing a "not" in the double space
                "transgender woman",
                "in a man's body",
                "male by",
                "transwoman",
                "trans gal",
                "trans-femme",
                "snc cis man",
                "trans lady",
                "trans women", # cause we still can't spell
                "trans nonbinary woman",
                "transdomme", # female form of domme, so assuming transfemme
                "transexual woman",
                "transfae",
                "transgender girl",
                "transgirl",
                "transneufem",
                "transwomen",
                "woman of transgender experience", # assuming trans woman not detrans
                "woman with a trans history",
                "a woman of trans experience",
                "biological male",
                "biologically male",
                "cis male nonbinary",
                "cishet man",
                "closeted femboy", # assuming this means amab femboy
                "default male presenting", # assuming default refers to birthsex
                "girl wanna-be", # assuming this means trans girl with imposter syndrome
                "male body, female mind",
                "male-socialised",
                "nonbinary transsexual female",
                "probably future woman-adjacent",
                'she/her dysphoric hrt fem"boy"',
                "temporarily nonbinary (on my way to womanhood)",
                'trans"women"',
                "trans-woman",
                "wanna-be girl",
                "wanna-be-hrt-femboy",
                "wannabe-woman",
                "want to be a girl but don't hate being a guy",
                "former man",
                "trans fae",
                "don't want to be a man",
                "mtx",
                "mtu",
                "mtn",
                "mtwtf", # no clue what this stands for but go off hon, you're def not from the f camp
                "cunt",
                "pussy",
                "wants a penis", # could be intersex
            ]:
                if item in lower_str:
                    result_bool = False

        if not result_bool:
            # things to re-include
            for item in [
                "ftmtf",
                "female to male to female",
                "i would be the same if i had been amab", # implies they are actually afab
                "dickless boy toy",
                "presents as female by default",
                "afab transfem",
                "afab trans woman", # not how that works but you're telling me your birth assignment hnng
                "trans girl (but in the afab way)",
                "in a transmasc body",
                "detrans woman",
                "ftmtn",
                "ftmtx",
                "t-cunt",
                "with a pussy",
                "pussy haver",
                "cunt boy",
                "cuntboy",
                "cunt-boy",
                "pussy boy",
                "pussyboy",
                "boycunt",
                "boypussy",
                "cuntman", # favourite superhero smh
                "pussyboi",
            ]:
                if item in lower_str:
                    result_bool = True

    return result_bool

    pass

