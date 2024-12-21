from copy import deepcopy
from re import split

#TODO:
# men's func:
    # print to check values & build up if statements to sort them
    # are there any other categories we should be collecting?
# make funcs for other categories
    # start w ones that we need for cross referencing (ie women, various adjectives)

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
    ]:
        if item in lower_str \
        and "to female" not in lower_str \
        and "boy-girl" not in lower_str \
        and "boyish woman" not in lower_str \
        and "80/20" not in lower_str \
        and "not actually ftm" not in lower_str\
        and "just a girl/" not in lower_str:
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
    ]:
        if item in lower_str:
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
            "women liking non woman but very much not a guy"
            
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
    ]:
        if item in lower_str:
            result_bool = False
    
    # things to re-include
    for item in [
        'man (in a gender neutral way)', # I will concede dude & guy gender neutral but man is largely Not That sorry
        'man (in a non-gendered context)', 
        "boy (gender neutral)",
        "boy but in an ungendered way",
        "sometimes i feel more like a man sometimes not",
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
        "almost",
        'girl but a bit off', 
        "like a boat",
        "i'm half girl",
        "i'm not not a woman", 
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
        'not not a woman', 
        'not not a woman, not not cis', 
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
    ]:
        if item in lower_str \
        and "femboy" not in lower_str \
        and "not a girl but not not a girl" not in lower_str \
        and "kind of girl but not really" not in lower_str:
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
        "man?wo"
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
        "not 100% a woman"
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
        "mamser"
    ]:
        if item in lower_str:
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
            "usual girly girl",
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
        "miss my balls",
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
    ]:
        if item in lower_str:
            result_bool = False
    
    # things to re-include
    for item in [
    ]:
        if item in lower_str:
            result_bool = True
        
    return result_bool

# male & female passing/presenting ✅
def is_present_passing(input_str:str, data_case:str):
    """
    takes an input string and a data case string (data_case="male|female")

    returns true or false based on whether the string implies 
    the person passes or presents as male or female
    """

    # making case insensitive
    lower_str = input_str.lower()

    # we're not excluding any prior categories there may be overlap

    result_bool = False

    # things that qualify it if included (to get rid of most other stuff)
    for item in [
        "passing", 
        "present", 
        "see", 
        "perceive", 
        "look",
        "reason",
        "convenie",
        "rather",
        "soci",
        "shape",
        "dress",
        "legal",
        "government",
        "impersona",
        "bod",
        "deflaut",
        "default",
        "sumed", # assumed, presumed
        "outwardly",
        "form",
        "on tv",
        "read",
        "the outside",
        "woman as in i just work here",
        "inertia",
        "habit",


    ]:
        if item in lower_str:
            result_bool = True

    # excluding general stuff
    if result_bool:
        for item in [
            # can't make up their mind, useless to this
            "female/male",
            "woman/man",

            "a dress",
            "dress like a teenage boy",
            "dress boy",
            "dressed as",
            "crossdress",
            "like dresses",

            "dogs as boys",
            "dissociated",
            "government work",
            "socialised",
            "socialized",
            "woman when its funny, man when it's convenient",
            "woman who wears a dress (in a manly way)",
            "wow what an ugly woman, she looks like a man",
            "seem like a guy",
            "femme presenting",
            "masc-presenting",
            "social ",
            "misshapen",
            "partner",
            "society",
            "see how it fits",
            "in a trans woman's body",  # neither trans man nor cis woman in a trans woman's body 
                                        # are valid under my label police rule smh

            # implies not achieved presentation/passing
            "prefers to be perceived",
            "at least see me",
            "i'd prefer",
            "need to be perceived",
            "will have a man's body",
        ]:
            if item in lower_str:
                result_bool = False

    # excluding gender specifics
    if result_bool and data_case == "male":
        for item in [
            "ciswoman",
            "looks female",
            "looks like a girl",
            "legally a she",
            "legally girl",
            "female passing",
            "female presenting",
            "female-shape",
            "female shape",
            "girl shape",
            "girl-shape",
            "girl of",
            "girl out of",
            "cis/girl",
            "trapped in a woman's body",
            "as a girl",
            "shape of a girl",
            "socially female",
            "woman passing",
            "a girl when",
            "female by",
            "female impersona",
            "girl-passing",
            "legally female",
            "cis woman",
            "socially a girl",
            "socially a woman",
            "as a woman",
            "woman-shape",
            "woman by",
            "woman of",
            "woman shape",
            "woman when",
            "woman-look",
            "a woman's body",
            "a female body",
            "body is a woman",
            "girl's body",
            "boy stuck in a",
            "female bodied",
            "afab",
            "anxiety and dread but in a boy way",
            "assigned female",
            "sumed female",
            "former",
            "gender non conforming",
            "gender non-conforming",
            "gender noncomforming",
            "gender nonconforming",
            "non-conforming",
            "girl on the outside",
            "dont want be read",
            "female form",
            "play a girl on tv",
            "woman as in i just work here",
            "girl by default",
            "habitual girl",
            "other persons read me as female",
            "performatively female",
            "presumed woman for lack of a better option",
        ]:
            if item in lower_str:
                result_bool = False

    elif result_bool and data_case == "female":

        # stuff that qualifies if contains
        for item in [
            "ciswoman",
            "looks female",
            "looks like a girl",
            "legally a she",
            "legally girl",
            "female passing",
            "female presenting",
            "female-shape",
            "female shape",
            "girl shape",
            "girl-shape",
            "girl of",
            "girl out of",
            "cis/girl",
            "trapped in a woman's body",
            "as a girl",
            "shape of a girl",
            "socially female",
            "woman passing",
            "a girl when",
            "female by",
            "female impersona",
            "girl-passing",
            "cis woman",
            "socially a girl",
            "socially a woman",
            "as a woman",
            "woman-shape",
            "woman by",
            "woman of",
            "woman shape",
            "woman when",
            "woman-look",
            "a woman's body",
            "body is a woman",
            "girl's body",
            "boy stuck in a",
            "female bodied",
            "woman as in i just work here",
            "deflaut",
        ]:
            if item in lower_str:
                return True
            
        for item in [
            "cisman",
            "looks male",
            "looks like a boy",
            "legally a he",
            "legally boy",
            "male passing",
            "male presenting",
            "male-shape",
            "male shape",
            "boy shape",
            "boy-shape",
            "boy of",
            "boy out of",
            "cis/boy",
            "trapped in a man's body",
            "as a boy",
            "shape of a boy",
            "socially male",
            "man passing",
            "a boy when",
            "male by",
            "male impersona",
            "boy-passing",
            "legally male",
            "cis man",
            "socially a boy",
            "socially a man",
            "as a man",
            "man-shape",
            "man by",
            "man of",
            "man shape",
            "man when",
            "man-look",
            "a man for legal reasons",
            "perceived as male",
            "male for the sake of convenience",
            "man out of convenience",
            "shape of a man",
            "guy-shape",
            "male (sometimes/for legal identification)",
            "male for the sake of convenience",
            "male is my government gender",
            "male-passing",
            "man for convenience's sake",
            "dude, just impersonating",
            "a man's body",
            "male body",
            "afab",
            "in a boy way",
            "former",
            "gender non conforming",
            "gender non-conforming",
            "gender noncomforming",
            "gender nonconforming",
            "non-conforming",
            "man-form",
            "not a boy, but i play one on tv",
            "dont want be read", # implies potential retrospective (ie I no longer get read as female 
            # but also still do not want to be read as female)
            "legally female", # could refer to an outdated sex marker

        ]:
            if item in lower_str:
                result_bool = False

    return result_bool


# helper
def is_in_binaries_list(input_str):
    """
    takes a string

    checks if the string contains any of the key words that were being caught 
    for the male & female categories

    if so returns True

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    for item in [ # if the item was caught in the male/female list 
        "girl","woman","lady","gal","female","chic","maiden",
        "ma","am","mom","mum","miss","ms","daughter","sister","gxrl","wxman","womxn",

        "guy","dude","boy","boi","man","male","sir","lad","lord",
        "dad","mr","mister","son","bro","bloke","bxy","bruv",
    ]:
        if item in lower_str:
            return True
    
    return False


# both & neither ✅
def is_both(input_str:str):
    """
    takes a string

    checks if it describes a combination of male & female gender (ie "both a man and a woman")

    if so returns True

    else returns False
    """
    # making case insensitive
    lower_str = input_str.lower()

    if is_in_binaries_list(input_str):
        # excluding already aligned folks
        if is_female_aligned(input_str) \
        or is_male_aligned(input_str) \
        or is_non_female_aligned(input_str) \
        or is_non_male_aligned(input_str) \
        or is_conflicted_male_aligned(input_str) \
        or is_conflicted_female_aligned(input_str) \
        or is_present_passing(input_str, "male") \
        or is_present_passing(input_str, "female"):
            return False
    
    result_bool = False

    # things that qualify it if included (to get rid of most other stuff)
    for item in [
        ("boy", "girl"),
        ("man", "woman"),
        ("guy", "girl"),
        ("male", "female"),
        ("guy", "sister"),
        ("gay man", "lesbian"),
        ("boy", "woman"),
        ("male", "woman"),
        ("boi", "grl"),
        ("boi", "gurl"),
        ("boi", "girl"),
        ("bxy", "gxrl"),
        ("dad", "mom"),
        ("dad", "girl"),
        ("dude", "chick"),
        ("man", "female"),
        ("husband", "female"),
        ("fag", "girl"),
        ("twink", "girl"),
        ("man", "girl"),
        ("prince", "girl"),
        ("he", "girl"),
        ("he", "lesbian"),
        ("he", "woman"),
        ("dude", "lady"),
        ("fag", "lady"),
        ("boy", "lady"), # actually wait we shouldn't be including "Ladyboy" bc that's a known thingy
        ("boi", "lady"),
        ("dude", "woman"),
        ("man", "maiden"),
        ("dude", "girl"),
        ("male", "girl"),
        ("guy", "mom"),
        ("guy", "milf"),
        ("man", "women"),
        ("dude", "gal"),
        ("man", "lady"),
        ("miss", "mister"),
        ("brother", "sister"),
        ("son", "daughter"),
        ("guy", "female"),
        ("fem", "tom"),
        ("guy", "lady"),
        ("guy", "gal"),
        ("guy", "tomboy"),
        ("dad", "lady"),
        ("bear", "girl"),
        ("husband", "woman"),
        ("man", "she"),
        ("boy", "she"),
        ("boy", "sister"),
    ]:
        
        # if both items are in the string
        if item[0] in lower_str and item[1] in lower_str:

            # if the items overlap (ie man & woMAN)
            if item[0] in item[1]:
                # we don't know if it actually contains the smaller word!
                contains_first_word = False
                # exclude longer word
                split_string = split(item[1], lower_str)
                # check if smaller word remains
                for piece in split_string:
                    if item[0] in piece:
                        contains_first_word = True

            # elif the words are distinct it contains both
            else: contains_first_word = True

            # only if both words are contained in the string
            if contains_first_word:
                result_bool = True

    for item in [
        "girloy","girboy", 
        "both", "either",
        "(wo)man","(fe)male","wo(man)","fe(male)",
    ]: # mfs CANNOT SPELL/DECIDE ON CONVENTIONS
        if item in lower_str:
            result_bool = True

    # excluding general stuff
    if result_bool:
        for item in [
            # ok new rule: if they are CLAIMING TO BE BOTH, they will be counted
                # yes I will begrudgingly include the trans & cis divide disrespecters in this 
                # cause I GUESS THEY ALL ARE TECHNICALLY ANYWAY
            # if they are neither we remove em
            # if they do not qualify or are likely to not qualify we remove em too
            # if they are one of the both & neither ppl - excluded for now bc they couldn't pick

            "trans girl (but in",   # you can't be transmasc & transfemme at once
            "trans man in a trans woman's body",
            "ugly woman", 
            "socialised",
            "socialized",
            "girly",
            "cosplay",
            "passing", "presenting",
            "had a baby",
            "ladyboy",
            "girl scout",
            "neither",
            "never feel",
            "no 'mis",
            "non man",
            "not ",
            "apathetic",
            "don't know",
            "everything except",
            "in a cismale way", # I'm assuming this one means like girl in the gay way??
            "creature",
            "don't feel",
            "blue",
            "woman is 0",
            "in between",
            "spectrum",
            "who knows",
            "as opposed to man or woman",
            "one of the",
            "partner ",
            "a pup",
            "perceived as",
            "raised",
            "looks like",
            "started a girl, no longer there",
            "between",
            "when it's funny",
            "flamboyant girl",
            "in an asthetic way",
            "never 100%",
            "a man's body",
            "notboynotgirl",
            "notgirl/notboy",
            "no longer a woman, never a man",
        ]:
            if item in lower_str:
                if item != "neither" \
                or (item == "neither" and "both" not in lower_str):
                    result_bool = False

        if not result_bool:
            for item in [
                "if a boy was a girl",
                "if a man was a woman",
                "both and neither",
                "partly",
                "a boy but also a girl",
                "a boy and a girl",
                "boygirl",
                "boy-girl",
                "girlboy",
                "quantum",
                "why not both",
                "neither exclusively, more like both",
                "either and neither",
            ]:
                if item in lower_str:
                    result_bool = True

    return result_bool

def is_neither(input_str:str):
    """
    takes a string

    checks if it describes a negation of both male & female gender (ie "not a man or a woman")

    if so returns True

    else returns False
    """
    
    # making case insensitive
    lower_str = input_str.lower()

    if is_in_binaries_list(input_str):
        # excluding already aligned folks
        if is_female_aligned(input_str) \
        or is_male_aligned(input_str) \
        or is_non_female_aligned(input_str) \
        or is_non_male_aligned(input_str) \
        or is_conflicted_male_aligned(input_str) \
        or is_conflicted_female_aligned(input_str) \
        or is_present_passing(input_str, "male") \
        or is_present_passing(input_str, "female"):
            return False
    if is_both(input_str):
        return False

    result_bool = False

    # things that qualify it if included (to get rid of most other stuff)
    for item in [
        "apathetic",
        "everything except",
        "neither",
        "as much not",
        "don't feel",
        "never",
        "non",
        "not",
        "no 'miss,'",
        "opposed to",
        '"or"',
        "between",
    ]:
        
        # if item is in the string
        if item in lower_str:
            result_bool = True

    if result_bool:
        for item in [
            "girly but not really",
            "girly girl",
            "never masculine",
            "nonboyna",
            "left gender",
            "raised",
            "not entirely female",
            "not constantly",
            "not always",
            "non-gender",
            "more boy than girl",
            "rest of the spectrum",
            "a man's body",
            "not a trans woman",
            "she/he",
            "woman by experience",
            "mix",
            "practicing",
            "there's another me who is now a guy",
            "ftm trans guy who's not actually ftm",
            "not really",
            "i'm both cisgender and nonbinary : i'm intersex.",
            "i'm not both binary genders.",
        ]:
            if item in lower_str:
                result_bool = False

        # things to reinclude
        for item in [
            "not really a boy, but not really a girl",
            "not really male/female",
        ]:
            if item in lower_str:
                result_bool = True

    return result_bool

#TODO amab & afab
def is_agab(input_str:str, data_case:str):

    
    # making case insensitive
    lower_str = input_str.lower()

    result_bool = True

    # things that qualify it if included (to get rid of most other stuff)
    for item in [
        "raised",
        "born",
        "assigned",
        "at birth",
        "child",
        "trans",
        "hrt",
        "ex",
        "former",
        "now",
        "cis",

        "afab",
        "dfab",
        "ft",
        "female to",

        "amab",
        "dmab",
        "mt",
        "male to",

    ]:
        if item in lower_str:
            result_bool = False

    if result_bool:
        # things to exclude
        for item in []:
            if item in lower_str:
                result_bool = False

    return result_bool

    pass
# there are certain ones indicating amab/afab in the male/female list leftovers 
# -> include in there later
# raised, socialised, check presenting lists too, etc

#TODO femme & masc
# needs to include various words like pretty, butch, rosboy (look up masc female equivalent), etc 


#TODO afterwards, do for other categories
# - combine is conflicted male aligned & fagdyke shit to find all lesbianism for men!

# (this may be in other collection file:) include "impersonator/impersonation/impersonating" 
# and "principal boy", and "dame" ?? in cross dresser category!


# helper func to dispense the correct function based on data case! ✅
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
    elif data_case == "female_aligned":
        return is_female_aligned
    elif data_case == "non_female_aligned":
        return is_non_female_aligned
    elif data_case == "conflicted_female_aligned":
        return is_conflicted_female_aligned
    elif data_case == "male_passing" or data_case == "female_passing":
        return is_present_passing
    elif data_case == "both":
        return is_both
    elif data_case == "neither":
        return is_neither
    elif data_case == "afab" or data_case == "amab":
        return is_agab

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
        - data_case="female_aligned"
        - data_case="non_female_aligned"
        - data_case="conflicted_female_aligned"
        - data_case="male_passing"
        - data_case="female_passing"
        - data_case="both"
        - data_case="neither"
        - data_case="afab"
        - data_case="amab"
    """

    output_list = []

    checking_func = checking_func_dispenser(data_case) # variable function for relevant conditions

    # check words in input list
    for item in sorted(list(set(input_list))):

        # if they fit criteria for being counted 
        if (data_case not in [ 
            # cases that need a data_case
            "male_passing",
            "female_passing",
            "afab", 
            "amab"
        ] and checking_func(item))\
        or (data_case in [ # data case useable as is
            "afab",
            "amab"
        ] and checking_func(item, data_case))\
        or (data_case in [ # removing "_passing" or other 8 last letters from data case
            "male_passing",
            "female_passing"
        ] and checking_func(item, data_case[:-8])):
            
            # they are added to output list
            output_list.append(item)

    return output_list



