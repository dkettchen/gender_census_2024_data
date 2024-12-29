from utils.key_word_catches import survey_catching as words_catching
from re import split

#TODO a bunch of words aren't catching, I suspect if there are multiple things catching at the same time
    # -> figure out why and fix

def collect_key_words_from_q37(input_list):
    """
    takes a list of custom gender label strings (question 2)

    returns a dictionary with a variety of keys collecting all custom input labels 
    containing relevant word bits and below 50 characters in length
    """

    # key words we'll be finding
    key_word_list = [
        "tumblr",
        "reddit",
        "discord",
        "patreon",
        "twitter",
        "pronouns",
        "mastodon","mastadon",
        "whatsapp",
        "facebook",
        "slack",
        "threads",
        "telegram",
        "t4t",
        "spacehey",
        "pillowfort",
        "substack",
        "cohost",
        "melonland",
        "eunuch",
        "youtube",
        "teams",
        "zoom",
        "pinterest",
        "lex",
        "twitch",
        "duckduckgo",
        "irc",
        "fetlife",
        "goodreads",
        "insta",
        "quotev",
        "scratch",
        "tiktok",
        "lemmy",
        "signal",
        "wattpad",
        "ao3",
        "matrix",
        "neocities",
        ("linked","in",),
        ("chat","gpt",),"ai",
        ("blue","sky",),
        ("nonbinary","wiki",),
        ("snap", "chat",),
        ("yik","yak",),
        ("anime","feminist",),
        ("gender", "reveal",),
        ("gender","census",),
        "googl", # google, googling
        "thing of things",

        "wiki", # there's some mispelled wikipedias in there and other wikis
        "podcast","forum","website","video","blog",
        "search","look","find",
        "mail","newsletter",
        "app",

        "word of mouth",
        "peer","freind","friend",
        "family","parent","offspring","mom",
        "partner","wife","husband","fianc","spouse",
        "staff","work","lab",
        "school","uni","college","teacher",
        "group","lgbt","gsa","pride","queer",
        "ist","doctor",
        
        "forg", # they forgor
        "remem",
    ]

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
            if key_word == ("blue","sky"):
                umbrella_word = "bluesky"
            elif key_word == ("nonbinary","wiki",):
                umbrella_word = "nonbinary wiki"
            elif key_word == ("snap", "chat"):
                umbrella_word = "snapchat"
            elif key_word == ("yik","yak",):
                umbrella_word = "yikyak"
            elif key_word == ("anime","feminist"):
                umbrella_word = "anime feminist"
            elif key_word == ("gender", "reveal"):
                umbrella_word = "gender reveal" # podcast??
            elif key_word in [("chat","gpt"), "ai"]:
                umbrella_word = "ai"
            elif key_word == ("linked","in"):
                umbrella_word = "linkedin"
            elif key_word == ("gender","census"):
                umbrella_word = "gender census"
            elif key_word == "googl":
                umbrella_word = "google"
            elif key_word in ["mastodon","mastadon",]:
                umbrella_word = "mastodon"
            elif key_word == "freind":
                umbrella_word = "friend"
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
