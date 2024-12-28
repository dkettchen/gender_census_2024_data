from src.sorting_q2_write_ins.sort_male_and_female_aligned import (
    is_male_aligned, is_non_male_aligned, is_conflicted_male_aligned,
    is_female_aligned, is_non_female_aligned, is_conflicted_female_aligned,
)
from src.sorting_q2_write_ins.sort_presenting_passing import is_present_passing
from utils.sorting_helpers import is_in_binaries_list
from re import split

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
            "both feminine and masculine", # expression not gender
            "both masc and femme",
            "both masculine, feminine and neither",
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
                "being both makes me functionally neither",
                "am i both genders? yes",
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
            "neither masc nor fem",
            "both masculine, feminine and neither",
            "i'm not a trans man",
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

