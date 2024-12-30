from utils.key_word_catches import survey_catching
from utils.sorting_helpers import caught_wrong_word
from utils.data_lists import offline_categories

def is_offline(input_str:str, data_case:str):
    """
    takes an input string and a data case denoting one 
    of the collected offline categories

    checks for given offline category in string

    if it denotes that offline category, it returns True, 
    otherwise it returns False
    """

    lower_str = input_str.lower()

    # input checking
    complex_cases = offline_categories
    if data_case not in complex_cases:
        if data_case not in lower_str:
            return False
        
        if data_case in survey_catching:
            for catch_word in survey_catching[data_case]:
                if catch_word in lower_str and not caught_wrong_word(lower_str, data_case, catch_word):
                    return False
    else:        
        if data_case == "friend":
            if "friend" not in lower_str and "freind" not in lower_str \
            and "peer" not in lower_str:
                return False
        elif data_case == "family":
            if "family" not in lower_str and "offspring" not in lower_str \
            and "parent" not in lower_str and "mom" not in lower_str:
                return False
        elif data_case == "partner":
            if "partner" not in lower_str and "spouse" not in lower_str \
            and "wife" not in lower_str and "boyfriend" not in lower_str \
            and "girlfriend" not in lower_str and "fiance" not in lower_str \
            and "husband" not in lower_str:
                return False
        elif data_case == "school":
            if "school" not in lower_str and "uni" not in lower_str \
            and "college" not in lower_str and "teacher" not in lower_str:
                return False
        elif data_case == "work":
            if "staff" not in lower_str and "work" not in lower_str \
            and "lab" not in lower_str:
                return False
        elif data_case == "lgbt":
            if "group" not in lower_str and "lgbt" not in lower_str \
            and "gsa" not in lower_str and "pride" not in lower_str \
            and "queer" not in lower_str:
                return False
        elif data_case == "clinician":
            if "ist" not in lower_str and "doctor" not in lower_str:
                return False

        # this bit technically does not work flawlessly for these cases but seems to do it for now??
            # as it may not include data_case itself 
            # but may include one of the other words/spellings we're looking for 🤔
        if data_case in survey_catching:
            for catch_word in survey_catching[data_case]:
                if catch_word in lower_str and not caught_wrong_word(lower_str, data_case, catch_word):
                    return False

    # let it run through at first & print to files
    result_bool = True

    # make cases to exclude stuff
    exclusion_list = []
    reinclusion_list = []

    if data_case == "clinician":
        exclusion_list = [
            "it existed",
            "listerv for queer and trans therapists",
            "university rainbow mailing list",
            "feminist",
            "distributed at my school's pride club"
        ]
    elif data_case == "lgbt":
        exclusion_list = [
            "(also queer)",
            "discord group",
            "queerly_beloved",
            "friend group",
            "groupchat",
            "im group",
            "lex",
            "group chat",
            "teams group",
            "in a group facebook mess",
            "signal group",
            "signal-group",
            "in a group whatsapp",
            "telegram",
            "whatsapp",
            "watsapp",
            "teloegram",
            "work social network group",
        ]
        reinclusion_list = [
            "for trans students",
            "queer",
            "lgbt",
        ]
    elif data_case == "school":
        exclusion_list = [
            "dreamwidth",
        ]
    elif data_case == "remem":
        exclusion_list = [
            "don't rem",
            "can't rem",
        ]

    # excluding whatever is in the excl list
    for item in exclusion_list:
        if item in lower_str:
            result_bool = False
    
    # reincluding items 
    for item in reinclusion_list:
        if item in lower_str and "lex" not in lower_str:
            result_bool = True

    # return result bool
    return result_bool