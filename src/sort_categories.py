from copy import deepcopy

def sort_men(input_dict): #WIP
    """
    removes unneeded/incorrect values from the "man/boy/male" key of the input_dict

    if they specify non-manhood specifically, void of other words to be caught on, 
    they will be added to a "non-man" key instead
    """

    category_dict = deepcopy(input_dict)

    men_list = category_dict["man/boy/male"]

    new_men = []
    non_men = []

    for item in men_list:
        # items that were caught by accident get dropped
            # f.e. we are collecting woman elsewhere already
        if "woman" in item:
            # print(item)
            continue

        # items that are negating manhood get collected on a new key
        if "not a man" in item:
            # print(item)
            non_men.append(item)

        # correct items get collected for new man key
        else:
            # print(item)
            new_men.append(item)
    
    category_dict["man/boy/male"] = new_men
    category_dict["non-men"] = non_men

    return category_dict

