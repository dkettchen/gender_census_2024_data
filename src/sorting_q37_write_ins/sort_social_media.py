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
        "gender census"
        "google",
        "mastodon",
        "friend",
    ]
    tuple_dict = {
        "bluesky": ("blue", "sky"),
        "nonbinary wiki": ("nonbinary", "wiki"),
        "snapchat": ("snap", "chat"),
        "yikyak": ("yik", "yak"),
        "anime feminist": ("anime", "feminist"),
        "gender reveal": ("gender", "reveal"),
        "linkedin": ("linked", "in"),
        "gender census": ("gender", "census"),
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
        else: # if it is one of the tuple ones
            tuple_case = tuple_dict[data_case]
            if tuple_case[0] not in lower_str or tuple_case[1] not in lower_str:
                return False

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
    else: 
        exclusion_list = []
    
    # excluding whatever is in the excl list
    for item in exclusion_list:
        if item in lower_str:
            result_bool = False

    # return result bool
    return result_bool