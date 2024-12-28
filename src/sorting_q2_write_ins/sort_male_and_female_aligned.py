"""
this file contains all the functions to do with whether or not a string implies male/female alignment
"""

# male aligned categories ✅
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

    # things that qualify it if present
    for item in [
        "when someone else calls me a girl/woman",
        "genderless boy",
        "genderless man",
        "man was not quite there",
        "a little guy",
        "neutral guy",
        "some kinda dude thing",
        "sort of a boy, almost but not quite",
        "trans male presenting",
        "ungendered but in a boy way",
        'born a woman with the brain of a man', 
        'boy in a girly way',
        'boy stuck in a "girl\\\'s" body',
        'female to male', 
        "ftm",
        'girl who grew up', 
        "gay man in a woman's body",
        'gender neutral demiboy', 
        'genderless boi', 
        'guy who just likes girls sm',
        'wish i was born and raised male', 
        'man in a female body',
        'man of lesbian origin', 
        'mostly male but not completely', 
        'trans man but not always completely binary', 
        'trans man of butch experience', 
        'male software female hardware', 
        'faggy trans non-binary man.', 
        'trans man, who is also non-binary',
        "man trapped in a",
        "a guy dressed as a girl",
        "boy but girly",
        "girly boy",
        "girly guy",
        "girlyboy",
        "girly dude",
        "girlish boy",
        "girlish-boy",
        "a girly man",
        "home im a guy who lies girls thats it im normale", # how did a straight guy get in here what
        "im a guy in the way ships are female",
        "like if a boy was raised as a girl", # assuming this to be literally this scenario??
        "man in a woman's body",
        "physically female, mentally male.",
        "some girl's loser boyfriend",
        "a ship is a woman",
        "close to man, but not completely",
        "i'm like if there was a guy",

        "faun", # for now to check all of em first
    ]:
        if item in lower_str \
        and "to female" not in lower_str \
        and "boy-girl" not in lower_str \
        and "boyish woman" not in lower_str \
        and "80/20" not in lower_str \
        and "not actually ftm" not in lower_str\
        and "just a girl/" not in lower_str\
        and "ftmgirl" not in lower_str:
            return True

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
        "fae",
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
        "non-male",
        "non-man",
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
        'post-male', 
        "she's the man", 
        'hrt fem"boy"',
        "sheboy",
        'tom-femboy', 
        'transfem boy', 
        "hrt-femboy",
        'whatever man', 
        "(wo)man",
        "one of the",
        "saphboy",
        "80/20 female to male",
        "boiwife",
        "boywife",
        "princess",
        "there's another me who is now a guy",
        "biological",
        "boy mode",
        "bro im just chilling",
        "bro its just vibes",
        "bromance",
        "fe(male)",
        "not actually ftm",
        "guywife",
        "just a girl/",
        "mamser",
        "manly moth",
        "mandox",
        "manmoder",
        "never felt comfortable being called a",
        "some manner of beast",
        "sometimes i feel more like a man sometimes not",
        "swarm of nanobots",
        "they/them femboy", # implies non-aligned femboy similar to hrt femboy
        "practicing",
        "your husband",
        "your wife",
        "boymoder",
        "boymoding",
        "husbandwife",

        "damsel",
        "nada masculino",
        "mother",
        "maiden",
        "ma'am",
        "maam",
        "madam",
        "mum",
        "chica",
        "twinkwife",
        "fagwife",
        "failwife",
        "femoid",
        "twink bride/wife",
        "weird wife",
        "wife (title)",
        "wife :)",
        "wife-gender",
        "womxn",
    ]:
        if item in lower_str:
            return False

    for item in [
        "ms",
        "wife",
        "ms."
    ]:
        if lower_str == item:
            return False

    # if none of these things are in the string => it qualifies
    return True

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

    # things to include
    for item in [
        'but not fully a girl.', 
        "don't know what to call me other than not a man",
        'almost a woman, definitely not a man', 
        "boyn't",
        "never a man",
        'not a guy, but "one of the guys"',
        "never a boy",
        "nada masculino",
    ]:
        if item in lower_str \
        and "boy or guy (never a man tho)" not in lower_str \
        and "no longer a woman, never a man" not in lower_str \
        and "but sometimes i'm not a woman" not in lower_str \
        and "never a man but always a gentleman" not in lower_str:
            return True

    result_bool = False

    # things that qualify it if included (to get rid of most other stuff)
    for item in [
        "not",
        "never",
        "non",
        "but",
        "except",
        "don't",
        "other",
        "than",
    ]:
        if item in lower_str:
            result_bool = True

    if result_bool == True: # if it qualified to begin with
        # things we're excluding (to narrow it down)
        for item in [
            "%","percent",
            "1/4",
            "girl",
            "woman",
            "butch",
            "female",
            "sister",

            "boy but",
            "boy, but",
            "boy , but",
            "boy, not",
            "boy not",
            "boy (",
            "dude but",
            "dude, but",
            "dude, not",
            "guy but",
            "guy, but",
            "guy (",
            "guy, not",
            "man but",
            "man, but",
            "man/not",
            "man (",
            "male but",
            "male, but",

            "don't know",
            "don't even know",
            "don't fuckin know",
            "dress like",
            "normative cis man",
            "not a trans man",
            "nonboyna",
            "old man calls his truck",
            "not actually ftm",
            "idk if guy",
            "she/he",
            "trans guy/dude",
            "not really a",
            "not quite a",
            "never a man but sometimes i'm not a woman",
            "no longer a woman, never a man",
            "absolutely not a man but also not a woman",
            "practicing",
            "but in a boy way",
            "there's another me who is now a guy",
            "boy or guy (never a man tho)",
            "(non-male) boy",
            "(wo)man",
            "sometimes i feel more like a man sometimes not",
            "women liking non woman but very much not a guy",
            "fae",
            "tradwife",
            "mother",
            "not a lady",
            "trans gal",
            "gxrl",
            
        ]:
            if item in lower_str:
                result_bool = False

    return result_bool

    # # things we're excluding
    # for item in [
    #     "%", "percent", 
    #     "1/2","half",
    #     "half",
    #     "lesbian",
    #     "dyke",
    #     "woman",
    #     "girl",
    #     "female",
    #     "gender neutral",
    #     "boy but",
    #     "boy, but",
    #     "boy , but",
    #     "dude but",
    #     "dude, but",
    #     "guy but",
    #     "guy, but",
    #     "dude, not",
    #     "boy, not",
    #     "gay man who",
    #     "man but",
    #     "man, but",
    #     "identified as male",
    #     "b.o.b",
    #     "basically a man",
    #     "butch",
    #     "boi",
    #     "ish",
    #     "kisser"

    # ]:
    #     if item in lower_str:
    #         return False

    # # if none of these things are in the string => it qualifies
    # return True

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

    # conflicted must not be in the explicitly male-aligned group or explicitly non_male-aligned group
    if is_male_aligned(input_str) or is_non_male_aligned(input_str):
        return False

    # => we only need to look at leftovers!

    result_bool = True

    # things to exclude
    for item in [
        "girl",
        "grl",
        "gurl",
        "gxrl",
        "gal",
        "woman",
        "women",
        "female",
        "chick",
        "sister",
        "mom",
        "lady",
        "gender neutral",
        "gender-neutral",
        "non-gender-specific",
        "non-gendered",
        "genderless slang",
        "butch lesbian",
        "lesbian and a gay man",
        "child identified",
        "b.o.b",
        "boyish",
        "kisser",
        "don't know",
        "dress like",
        "potheads",
        "but normative cis man",
        "tomboy",
        "male-bodied",
        "ungendered",
        "boy parts",
        "seem like",
        "my feeling is different",
        "don't even know",
        "don't fuckin know",
        "presenting as a man",
        "draw, man",
        "a boy because i was  born afab", #idk what this one's on abt I think they might've missed a word or smth
        "not a trans man",
        "just work here",
        "just sorta funky",
        "milf",
        "just me man",
        "a boy day",
        "lesbian in a man's body",
        'male impersonater', 
        'male presenting', 
        "maiden",
        "mannish",
        "mrs",
        "miss",
        "robot",
        "she",
        "daughter",
        "tom boy",
        "wouldn't you like to know",
        'amab trans boy', 
        'fuck if i know man', 
        'girboylent', 
        'genderless statue carved into the shape of a man', 
        'ice bot', 
        "idk man",
        'if a transmasc guy was also transfem',
        'just a guy (neutral)', 
        "(guy being neutral)",
        "clusters",
        "principal boy",
        "dragoness",
        'male is my government gender', 
        'male on paper',
        "socialised",
        "idk if guy",
        "nonboynary", # dunno what this one means and refuse to engage with it
        'nonboynairy',
        "one of the guys",
        'not really a dude, just impersonating it', 
        "transfem",
        'wanna-be-hrt-femboy', 
        'whatever man',
        'middle age started male hormones', 
        "one of the",
        "there's another me who is now a guy",
        "biological",
        "boy mode",
        "bro im just chilling",
        "bro its just vibes",
        "bromance",
        "fe(male)",
        "ftm trans guy who's not actually ftm",
        "mamser",
        "mandox",
        "manly moth",
        "manmoder",
        "(wo)man",
        "some manner of beast",
        "sometimes i feel more like a man sometimes not",
        "swarm of nanobots",
        "they/them femboy",
        "fae",
        "your husband",
        "husbandwife",
        "boymoder",
        "boymoding",
        "tradwife",
        "damsel",
        "mother",
        "ma'am",
        "madam",
        "mum",
        "chica",
        "your wife",
        "failwife",
        "femoid",
        "fagwife",
        "chic",
        "weird wife",
        "wife (title)",
        "wife :)",
        "wife-gender",
        "womxn"
    ]:
        if item in lower_str:
            result_bool = False

    if lower_str in [
        "ms",
        "ms.",
        "wife",

    ]:
        result_bool = False
    
    # things to re-include
    for item in [
        'man (in a gender neutral way)', # I will concede dude & guy gender neutral but man is largely Not That sorry
        'man (in a non-gendered context)', 
        "boy (gender neutral)",
        "boy but in an ungendered way",
        "sometimes i feel more like a man sometimes not",
        "fae boi",
        "genderfae demiboy",
        "faehusband",
    ]:
        if item in lower_str:
            result_bool = True
        
    return result_bool

# female aligned categories ✅
def is_female_aligned(input_str:str):
    """
    takes a string

    checks if the gender it describes qualifies as explicitly female-aligned 
    (ie "A trans girl", "butch woman", etc)

    if so returns True

    else returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # it it's already in male aligned we are not interested
    if is_non_male_aligned(input_str) \
    or is_male_aligned(input_str) \
    or is_conflicted_male_aligned(input_str):
        return False

    # things that qualify it if present
    for item in [
        "male to female",
        'a woman with a splash of non binary', 
        "to the left",
        "tough, muscular",
        "60% opacity",
        "tomato is a fruit",
        # "almost",
        'girl but a bit off', 
        "like a boat",
        "i'm half girl",
        "kind of girl",
        'off-brand', 
        '3d anime girl model', 
        'a woman of trans experience', 
        'woman of transgender experience', 
        'woman with a trans history',
        'girl but in a violent way', 
        "fine being seen as a girl", 
        'im a woman, but sometimes im just myself', 
        'masc-presenting female', 
        'misshapen girl', 
        'not not a woman', 
        'not-not-a-girl',
        'woman but in a nonhuman way', 
        'woman but slightly', 
        'a girl but in a non-binary way', 
        'a girl but in a somewhat way', 
        'a girl but like a little bit off', 
        'a girl but not a person', 
        'a girl but not a very good one', 
        'a pants girly', 
        'a woman but in a non-binary way', 
        'a woman but like in the way that a boat is a woman', 
        'a woman but that could change', 
        'a woman, but also several nonbinary genders.', 
        'aporagirlie', 
        'female gender but not human female gender', 
        'fully woman but also more', 
        'girl (gender neutral)', 
        'girl but only if i get to be butch', 
        'girl but only sometimes', 
        'girl but ordered from wish dot com', 
        "girl but something's off", 
        'girl but weird about it', 
        'girl sometimes but not in a cis way', 
        'girl, but not completely', 
        "girl/woman but only to those I'm attracted to", 
        'not not a girl', 
        'not not-a-girl', 
        'on the girl spectrum', 
        'on the woman-spectrum', 
        "woman but i'm doing it wrong on purpose", 
        'woman but it hits different', 
        'woman but like alien???', 
        'woman with a lowercase w', 
        'woman with a twist', 
        'woman, but as a job', 
        'woman, but specifically in sexual contexts', 
        "girl/woman but only to those I'm attracted to", 
        "a girl driving a meatmech man",
        "boyish lesbian",
        "now woman",
        "boyish woman",
        "lesbian in a man's body", # assuming this is a trans(femme) lesbian
        "a girl dressed as a guy",
        "want to be a girl",
        "woman/girl/girlie/girly",
        "woman who wears",
        "tomboy dickgirl",
        "euphoric as trans female",
        "flamboyant girl",
        "in-between the middle of man and woman and a woman",
        "genderfae/",
        "mama",
        "femoid",
        "she but the way an old man calls his truck she",
    ]:
        if item in lower_str \
        and "femboy" not in lower_str \
        and "not a girl but not not a girl" not in lower_str \
        and "not really" not in lower_str:
            return True

    # things we're excluding
    for item in [
        "boy",
        "dude",
        "guy",
        "boi",
        " man",
        " male",
        "in a woman's body", # indicates transmasc
        "not a girl",
        "not girl",
        "not a woman",
        "not quite",
        "afab", # if you gotta specify I presume you're not female aligned
        "female at birth",
        "anything but",
        "anything not",
        "but not",
        "dad",
        "neutral)",
        "demifemme",
        "don't just refere to me as a girl",
        "refused female hormones",
        'emotionally female', 
        'ex-girl', # indicates transmasc
        "former girl",
        "female to", # indicates transmasc
        "female bodied",
        "husband",
        "passing",
        "presenting",
        "non woman",
        "femme but",
        "act like",
        'girl dropout', # assuming this means dropping out of girl
        "cismale",
        "vibes only",
        "on t",
        "fag",
        "twink",
        "girlish",
        'girlman', 
        "girln't", 
        'girloy', 
        'prince', 
        "girly",
        "girlie",
        'grammatically and physically female',
        "he's my girlfriend",
        "don't (usually) feel like a woman",
        "dont want be read as female",
        "just work here",
        "not a lady",
        "only a girl when",
        'not "a woman."',
        "not woman",
        "out of phase of womanhood",
        "ladyman",
        'man enough to be a girl scout', 
        'man shaped girl', 
        'man who is a girl', 
        'man w',
        "man, w",
        'man-maiden', 
        'man-w', 
        'man/w',
        "man?wo",
        "manw",
        'masculine in a girly way', 
        'female puberty', 
        "woman but",
        "mister",
        "no comfortable",
        "non woman",
        "non-woman",
        'nongirl',
        "not completely",
        'not entirely', 
        "not female",
        "not fully",
        "not really",
        "not-girl",
        'not-woman', 
        'notgirl', 
        "brother",
        "one of the",
        "outwardly a girl",
        "partner",
        "physically",
        "on tv",
        "presumed",
        "rarely",
        "lady no",
        "socialised",
        "socialized",
        "/man",
        "son-daughter",
        "started a girl, no",
        '"man',
        "scary transgender",
        "unwomanly descent",
        "girl mode",
        "lady suit",
        "cosplay",
        "experience",
        "woman't",
        "(male)",
        "womanhood just made me unhappy",
        "girl but",
        "drag queen",
        "except",
        "assigned",
        "assumed",
        "beard",
        "bxy",
        'female-born', 
        "female impersonator",
        "kisser",
        "femalehood", # this is just a horrid word I dislike looking at and will not validate smh
        "he/him",
        "techically just a lad",
        "bear",
        "male and f",
        'male (sometimes/for legal identification)',
        'male woman', 
        'male-female', 
        'man and woman', 
        "man or woman",
        'mangirl', 
        'manwoman', 
        "female history",
        'misgendered female', # I think this is misgendered as female??
        'not a trans woman', 
        'not!woman', 
        'not-a-girl', 
        "not-a-woman",
        'not-quite-a-woman', 
        'other persons read me as female', 
        'past-life female', 
        'performatively female', 
        "politically", # we're talking COLD HARD FACTS HERE YOU FEMINISTS YOU
        "post-",
        "default",
        "seen as",
        "socially",
        "appears to be",
        "against my will",
        "theydy",
        "transman",
        "transmasc",
        'unable to girl',
        "used to be a girl",
        "woman, but",
        "irrevelant",
        "size/fatness",
        "duckling",
        "everything outside of female",
        "femboy",
        "shape",
        "man?woman?",
        "will not correct my mom",
        "not 100% a woman",
        'not a "real" girl', 
        "piloting",
        "raised",
        "girl's clothing",
        "feels wrong",
        "resembles",
        "woman's hat",
        "everything but",
        "girl wasn't",
        "your mom",
        'non-female', 
        'once-girl', 
        "92% neutral gender, 2% girl",
        "not always a",
        "biological",
        "person of the female sex", 
        "not a girl but not not a girl", # is conflicted
        "womanhood resister",
        "bad at ",
        "botgirl", # this may be a misspelling of boygirl =.=
        "genderless robot that's made to sound like a woman", # this is female passing??
        "girlless catgirl", # is conflicted
        "girlmech",
        "girlmoder",
        "(non gendered)",
        "lady lover", # like girl kisser??
        "ladybuck", # buck is a male deer right? if it was buck lady I'd let it slide same as doe boy
        "legally",
        "not quite",
        "practicing",
        "none girl",
        "occasionally ejected from womanhood",
        "kind of girl but not really",
        "mamser",
        "3d(masc,femme,fae) model that varies with time",
        "fae changeling",
        "fae creature",
        "fae being",
        "fae-like",
        "fae like",
        "neopronouns",
        "fae rules",
        "faekin",
        "fae/",
        "fae or fairy",
        "fairy/fae",
        "bird or bloke",
        "bro i don't know",
        "man and women",
        "madam sir",
        "male impersonater",
        "instead of mr or mrs",
        "mother in name only",
        "mr/mrs",
        "como ser una chica", # prompt was english sorry
        "robot (+ bot)",
        "robotgender/botgender",
        "urmum",
        "your wife",
        "bro im just chilling",
        "bro its just vibes",
        "bromance",
        "ftmgirl",
        "ice bot",
        "male dragoness",
        "male is my government gender",
        "male on paper",
        "man, as well as women",
        "manmoder",
        "(wo)man",
    ]:
        if item in lower_str:
            return False
    
    if lower_str in [
        "mannish",
    ]:
        return False

    # if none of these things are in the string => it qualifies
    return True

def is_non_female_aligned(input_str:str):
    """
    takes a string

    checks if the gender it describes qualifies as explicitly non-female aligned
    (ie "definitely not a woman", etc)

    if so returns True

    else returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # non-female aligned must not be in prior groups
    if is_female_aligned(input_str) \
    or is_non_male_aligned(input_str) \
    or is_male_aligned(input_str) \
    or is_conflicted_male_aligned(input_str):
        return False

    # => we only need to look at leftovers!

    # things to include
    for item in [
        'anything not female or female-coded', 
        'everything outside of female', 
        "girln't",
        "woman't",
        'dont want be read as female', 
        "just a person that's anything but a girl", 
        "body is a woman but i am not",
        'no comfortable being called a woman', 
        'anything but a girl', 
        'everything but a girl', 
        "definitely not female",
        "certainly not woman",
        "never a girl",
        "not female but men are ick",
        "i was a girl but i am not a woman", # this implies transmasc
    ]:
        if item in lower_str:
            return True

    result_bool = False

    # things that qualify it if included (to get rid of most other stuff)
    for item in [
        "not",
        "never",
        "non",
        "but",
        "except",
        "don't",
        "other",
        "than",
    ]:
        if item in lower_str:
            result_bool = True

    if result_bool == True: # if it qualified to begin with
        # things we're excluding (to narrow it down)
        for item in [
            "boy",
            "guy",
            "girl but",
            "and a butch woman",
            "woman but",
            "except male",
            "female presenting",
            "female( but",
            "gal or fella",
            "lady but",
            "girl, but",
            "a man",
            "man/woman",
            "if a girl was",
            "girly girl",
            "not *not*",
            "not not",
            'm "women"',
            "woman, but",
            "male nor female",
            "not always a woman",
            "non man",
            "my mom",
            "or man",
            "entirely female",
            "completely a woman",
            "fully a girl",
            "fully a woman",
            "just a woman",
            "male or female",
            "quite a woman",
            "quite girl",
            "male/female",
            "not-not",
            "girl maybe sometime",
            "girl-not girl",
            "really a girl",
            "(usually)",
            "with left gender",
            "entirely ma",
            "not really",
            "brother",
            "partner",
            "physically",
            "politically",
            "practicing",
            "but a girl",
            "woman not",
            "woman/not",
            "man or woman",
            "female but",
            "female gender but",
            "not constantly",
            "not always",
            "girl (but",
            "girl not",
            "girl sometimes",
            "a female animal",
            "lady not",
            "neither male not female",
            "man, woman,",
            "female or male",
            "nonbinary man",
            'not a trans woman', # unclear abt what distinction is made against
            "woman/man",
            "entirely a girl",
            "not like the other girls",
            "quite a girl",
            "not totally",
            "not-quite",
            "read me as female",
            'trans girl (but in the afab way)', # NOT HOW THAT WORKS MF
            "woman as a descriptor",
            "woman by",
            "not man",
            "non practing", # can't spell omg
            "don't just refere to me as a girl", # I misread this one before it's less clear than I thought
            "girl like but not quite",
            "not a guy but even less a girl",
            "im just a girl (non gendered)",
            "not a man, but definetly not a woman",
            "gay man",
            "tradwife", # doesn't mean not female aligned just not tradwife
            "bro I don't know",
            "potheads",
            "but normative cis man",
            "i don't even know",
            "i don't fuckin know",
            "i don't know",
            "not a trans man",
            "mother in name only",
            "not 100% a woman",
            'not a "real" girl',
            "she but the way",
            "(wo)man",
        ]:
            if item in lower_str:
                result_bool = False

    return result_bool

def is_conflicted_female_aligned(input_str:str):
    """
    takes a string

    checks if the gender it describes explicitly mentions female-aligned language but does 
    not seem to be able to make up its mind/commit to it (ie "a girl but not a woman", etc) 
    but is not a more unaligned conflicting statement (ie "100% man and 100% woman")

    if so returns True

    else returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    # conflicted must not be in previous groups
    if is_female_aligned(input_str) \
    or is_non_female_aligned(input_str) \
    or is_non_male_aligned(input_str) \
    or is_male_aligned(input_str) \
    or is_conflicted_male_aligned(input_str):
        return False

    # => we only need to look at leftovers!

    result_bool = True

    # things to exclude
    for item in [
        "boy",
        "guy",
        "fag",
        " male",
        " man",
        "woman's body",
        "afab",
        "twink",
        "female at birth",
        "assumed",
        "boi",
        "dad",
        "bruh",
        "duckling",
        "cosplay",
        "female hormones",
        "emotionally",
        'ex-girl',
        "female to",
        "female bod",
        "husband",
        "passing",
        "presenting",
        "shape",
        "forced",
        "former",
        "dropout",
        "cismale",
        "girlman",
        "girloy",
        "prince",
        "girly",
        "girlie",
        "physically",
        "he's my girlfriend", 
        'he/him woman',
        "(usually)", 
        "just work here",
        "was a girl but I am not a woman",
        "usual girly girl",
        "dude",
        'out of phase of womanhood', 
        "ladyman",
        "lived experience",
        "male-female",
        "man and woman",
        "man enough",
        'man who is a girl', 
        'man woman',
        "man, woman,",
        "man-maiden",
        'man-woman', 
        'man/woman', 
        "man?woman?", 
        'manwoman', 
        "female puberty",
        "mister",
        "none woman with left gender",
        "not a bot",
        "men are ick",
        "brother",
        "one of the",
        "partner",
        "reluctance to change",
        "size/fatness",
        "girl on t",
        "demifemme",
        "female form",
        "presumed",
        "raised",
        "rarely",
        "socialised",
        "socialized",
        "socially",
        "woman/man",
        "female/male",
        "clothing",
        "son-daughter",
        "started a girl",
        "man or woman",
        "unwomanly descent",
        "not entirely female below",
        "girl mode",
        "resemble",
        "lady suit",
        "(male)",
        "/man",
        'womanhood just made me unhappy', 
        "woman's hat",
        "assigned",
        "girlish confusion",
        "bxy",
        'female-born', 
        "female impersonator",
        "by default",
        "girlie",
        "girly",
        "expectation of femalehood",
        "he/him",
        "techically just a lad",
        "a bear was",
        "male and female",
        'male woman', 
        "mangirl",
        'masculine person who has female history', 
        'misgendered female', 
        'not a trans woman', 
        "a-man",
        'once-girl', 
        'other persons read me as female', 
        'past-life female', 
        'performatively female', 
        "post-",
        "presents as female",
        "seen as",
        "girlish",
        "in vibes",
        "when it's funny",
        "when its funny",
        'never masculine but not always a woman', 
        "kisser",
        "never fully female",
        "appears to be",
        "girl box against my will",
        "theydy",
        "transma",
        'unable to girl', 
        "used to be",
        "convenien",
        "woman feels wrong",
        "experience",
        "feminine, but",
        "feminine but",
        "womanhood is irrevelant to me",
        "biological",
        "girl mode",
        "don't just refere to me as a girl",
        "person of the female sex.",
        "practicing",
        "womanhood resister",
        "botgirl",
        "genderless robot that's made to sound like a woman",
        "bad at",
        "girlmoder",
        "girlmech",
        "mamser",
        "lady lover",
        "legally female",
        "fae",
        "man and women",
        "madam sir",
        "male impersonater",
        "mannish",
        "mr or mrs",
        "mr/mrs",
        "como ser una chica",
        "robot",
        "urmum",
        "your wife",
        "bro",
        "ice bot",
        "male (sometimes/for legal identification)",
        "male is my government gender",
        "male on paper",
        "man, as well as women",
        "manmoder",
        "(wo)man",
        "bird or bloke",
        "tradwife",
        "ftmgirl",
        "male dragoness",
    ]:
        if item in lower_str:
            result_bool = False
    
    # things to re-include
    for item in [
    ]:
        if item in lower_str:
            result_bool = True
        
    return result_bool
