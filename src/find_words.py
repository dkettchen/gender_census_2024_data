from utils.read_txt import read_txt
from copy import deepcopy

input_list = read_txt("q2") # retrieving data in function

def find_adj_men_n_women(new_dict, reference_dict, input_str):
    """
    takes 
    - a new dictionary one wants to update (can be empty)
    - a dictionary containing the raw categories to reference
    - a string to check

    returns a new copy of the new dict with the string added to any 
    "{adjective} {man/woman}" categories it fits into

    if the categories were not in the input new dict yet, they have been added
    """

    input_dict = deepcopy(new_dict)

    for label in [ # finding overlap between these labels & male/female categories
        "gnc", 
        "genderqueer", 
        "bigender", 
        "genderfluid", 
        "nonbinary", 
        "intersex",
        "trans",
        "gay",
        "lesbian",
        "dyke",
        "sapphic",
        "cis",
    ]:
        if input_str in reference_dict["man/boy/male"] and input_str in reference_dict[label]:
            if input_str in reference_dict["woman/girl/female"]: # if it caught on woMAN
                continue
            category = f"{label} man"
        elif input_str in reference_dict['woman/girl/female'] and input_str in reference_dict[label]:
            category = f"{label} woman"
        else:
            continue

        if category not in input_dict.keys():
            input_dict[category] = []
        input_dict[category].append(input_str)

        return input_dict


    #TODO: 
    # - separate each section into its own function for ease of organisation
    # - check for racial words bc I know I've seen black & the n word in there
        # check for asians too, but using keyword "sian" bc we wanna catch gaysian too
        # -> to count toward my argument of "other intersections make standard 
        # gender roles harder to process and/or relate to" 
    # - place sorting functions in a way that'll ripple down (ex sorting through 
    # male *before* using it to collect adjectives etc)
    # - collect remaining catches somehow to look through later

    # collecting initial values using key words

def find_known_birthsexes(new_dict, reference_dict, input_str):
    """
    takes 
    - a new dictionary one wants to update 
    (should already contain "cis man"/"cis woman" keys)
    - a dictionary containing the raw categories to reference 
    (should contain "afab"/"amab" and "transmasc"/"transfemme" keys)
    - a string to check

    returns a new copy of the new dict with the string added to the "afab"/"amab" keys 
    if it was in any of the relevant groups in the new & reference dict 
    (afab/amab, transmasc/transfemme, cis woman/man)

    if the "afab"/"amab" keys were not in the input new dict yet, they have been added

    if the string was not in any of the relevant keys 
    and the "afab"/"amab" keys were already contained, 
    the new dict will be returned unchanged
    """

    input_dict = deepcopy(new_dict)

    for known_birthsex in [ # finding birthsexes we know about
            ("afab", "transmasc", "cis woman"),
            ("amab", "transfemme", "cis man")
        ]:
            if known_birthsex[0] not in input_dict.keys():
                input_dict[known_birthsex[0]] = []

            if input_str in reference_dict[known_birthsex[0]] \
            or input_str in reference_dict[known_birthsex[1]] \
            or input_str in input_dict[known_birthsex[2]]:
                birthsex = known_birthsex[0]
                input_dict[birthsex].append(input_str)

    return input_dict

def cross_reference_narrow_down(input_dict, input_list):

    category_dict = deepcopy(input_dict)
    
    # for reference
    key_ref = [
        '-sexual', 
        'DID_related', 
        'afab', 
        'agender', 
        'amab', 
        'androgynous', 
        'autism_related', 
        'bigender', 
        'binary', 
        'butch/masc/tomboy', 
        'cis', 
        'creature', 
        'demi', 
        'demiboy', 
        'demigirl', 
        'dysphoric', 
        'fag_dyke', 
        'femboy', 
        'femme', 
        'flux', 
        'gay', 
        'gender', 
        'genderfluid', 
        'genderqueer', 
        'gnc', 
        'half', 
        'hermaphrodite', 
        'human', 
        'intersex',
        'lesbian',
        'sapphic',
        'dyke', 
        'man/boy/male', 
        'me', 
        'name', 
        'nb', 
        'neither', 
        'neutral', 
        'no', 
        'nonbinary', 
        'none', 
        'other', 
        'other_neurodiversity_related', 
        'person', 
        'queer', 
        'questioning', 
        'sex', 
        'they/them', 
        'thing', 
        'trans', 
        'transfemme', 
        'transmasc', 
        'transvestite/crossdresser/drag', 
        'trap', 
        'two-spirit', 
        'woman/girl/female'
    ]

    label_categories_dict = {} # cross referencing
    for item in input_list:

        # cross referencing various adjectives with male & female categories (ie "genderqueer man", etc)
        label_categories_dict = find_adj_men_n_women(label_categories_dict, category_dict, item)

        # locating known birtsex info via afab/amab, trans directions & cis men & women
        label_categories_dict = find_known_birthsexes(label_categories_dict, category_dict, item)

        # finding boths?
        # both + anything that's in both male & female category

        # finding male/female only items -> anything that isn't in both

    #print(sorted(category_dict.keys()))
    return label_categories_dict


(# notes from earlier
    # print(len(input_list) - left_overs - skip_overs)
    # # we've collected about 10k unique entries to be sorted through now
    # print(skip_overs)
    # # we have just shy of 800 skips for yapping
    # print(left_overs)
    # # we have about 4600 leftovers that have no more reasonable inclusions to extract 
    # as far as I can tell from skimming em

        # etc
        # first put in all the diff main categories & then we can go through & fix things
        # could refactor if statements via keyword list w type checking
            # if it's a string, check if it's in the item
            # if it's a tuple of two, check if both are in the item
            # etc
        # make sure we descend in granularity/stuff that could get mixed up

        # if x word is in item
        # add to relevant key on dict
    # print key -> see if anything is amiss
        # if smth was caught erroneously: make a case to exclude that item/those items
    # repeat for all needed keys
    # -> this way we need to type a lil & read a bunch, rather than copy pasting everything!
)

