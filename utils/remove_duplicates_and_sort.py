from copy import deepcopy

def remove_duplicates_and_sort(input_dict):
    """
    takes a dictionary with list values on its keys

    returns a new dictionary where each input list has had duplicates removed if any, 
    and has been sorted
    """

    category_dict = deepcopy(input_dict)

    for key in category_dict: # sorting & making sure we don't have duplicates in key values
        current_list = category_dict[key]
        sorted_list = sorted(list(set(current_list)))
        category_dict[key] = sorted_list
    
    return category_dict
