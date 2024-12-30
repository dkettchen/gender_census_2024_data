from utils.key_word_catches import survey_catching
from utils.sorting_helpers import caught_wrong_word

def is_social_media(input_str:str, data_case:str):
    """
    takes an input string and a data case denoting one 
    of the collected social media sites (ie tumblr, google)

    checks for given social media in string

    if it denotes that social media, it returns True, 
    otherwise it returns False
    """

    lower_str = input_str.lower()

    # input checking
    complex_cases = [
        "ai",
        "bluesky",
        "nonbinary wiki",
        "snapchat",
        "yikyak",
        "anime feminist",
        "gender reveal",
        "linkedin",
        "gender census",
        "google",
        "mastodon",
        "friend",
        "whatsapp",
        "pronouns page",
        "anime feminist",
        "gender reveal",
        "wikipedia",
        "telegram",
    ]
    tuple_dict = {
        "bluesky": ("blue", "sky"),
        "nonbinary wiki": ("nonbinary", "wiki"),
        "snapchat": ("snap", "chat"),
        "yikyak": ("yik", "yak"),
        "anime feminist": ("anime", "feminist"),
        "gender reveal": ("gender", "reveal"),
        "linkedin": ("linked", "in"),
        "pronouns page": ("pronoun", "page"),
        "anime feminist": ("anime", "feminist"),
        "gender reveal": ("gender","reveal"),
    }
    if data_case not in complex_cases:
        if data_case not in lower_str:
            return False
        
        if data_case in survey_catching:
            for catch_word in survey_catching[data_case]:
                if catch_word in lower_str and not caught_wrong_word(lower_str, data_case, catch_word):
                    return False
    else:        
        if data_case == "ai":
            if "ai" not in lower_str and ("chat" not in lower_str or "gpt" not in lower_str):
                return False
        elif data_case == "google":
            if "googl" not in lower_str:
                return False
        elif data_case == "friend":
            if "friend" not in lower_str and "freind" not in lower_str:
                return False
        elif data_case == "mastodon":
            if "mast" not in lower_str:
                return False
        elif data_case == "whatsapp":
            if "whatsapp" not in lower_str and "watsapp" not in lower_str:
                return False
        elif data_case == "gender census":
            if "you" not in lower_str and ("gender" not in lower_str or "census" not in lower_str)\
            and "mail" not in lower_str and "website" not in lower_str and "look" not in lower_str:
                return False
        elif data_case == "wikipedia":
            if "wikip" not in lower_str:
                return False
        elif data_case == "telegram":
            if "telegram" not in lower_str and "teloegram" not in lower_str:
                return False

        else: # if it is one of the tuple ones
            tuple_case = tuple_dict[data_case]
            if tuple_case[0] not in lower_str or tuple_case[1] not in lower_str:
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
    if data_case == "eunuch":
        exclusion_list = [
            "looked up what a eunuch was and this came up lol",
        ]
    elif data_case == "tumblr":
        # excluding tumblr via other places/reposts, 
        # but including "and tumblr"/"tumblr and" ones
        exclusion_list = [ 
            "reddit",
            "r/"
            "tumblr link",
            "last year",
        ] # this will have many things
    elif data_case == "gender census":
        exclusion_list = [
            "anime",
            "friend",
            "gender kit",
            "gender reveal",
            "other mailing list",
            "pronouns page",
            "university rainbow mailing list",
            "some lgbtqia+ website",
            "eunuch",
            "google",
            "pronouns"
        ]
    else: 
        exclusion_list = []
    
    # excluding whatever is in the excl list
    for item in exclusion_list:
        if item in lower_str:
            result_bool = False

    # return result bool
    return result_bool

def is_other_online(input_str:str, data_case:str):
    """
    takes an input string and a data case denoting [...]

    checks for given [...] in string

    if it denotes [...], it returns True, 
    otherwise it returns False
    """

    lower_str = input_str.lower()

    # input checking (no complex cases here)
    if data_case not in lower_str:
        return False
    if data_case in survey_catching:
        for catch_word in survey_catching[data_case]:
            if catch_word in lower_str and not caught_wrong_word(lower_str, data_case, catch_word):
                return False

    # let it run through at first & print to files
    result_bool = True

    # make cases to exclude stuff
    if data_case == "forum":
        exclusion_list = [
            "melonland",
            "eunuch",
            "limonnur",
        ]
    else: 
        exclusion_list = []
    
    # excluding whatever is in the excl list
    for item in exclusion_list:
        if item in lower_str:
            result_bool = False

    # return result bool
    return result_bool