from utils.sorting_dispenser import checking_func_dispenser
from utils.data_lists import social_media_list, offline_categories

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

        - data_case="femme"
        - data_case="masc"
        - data_case="futch"

        - data_case="androgynous"
        - data_case="androgyne"

        - data_case="crossdresser"
        - data_case="drag"
        - data_case="femboy"
        - data_case="sissy"
        - data_case="trap"

        - data_case="autistic"
        - data_case="neurodivergent"
        - data_case="plural"

        - data_case="genderqueer"
        - data_case="genderfluid"
        - data_case="genderflux"
        - data_case="queer"
        - data_case="gnc"
        - data_case="nb"
        - data_case="agender"
        - data_case="neutral"
        - data_case="bigender"
        - data_case="demi"

        - data_case="human"
        - data_case="person"

        - data_case="trans"
        - data_case="transfemme"
        - data_case="transmasc"
        - data_case="detrans"
        - data_case="cis"
        - data_case="intersex"
        - data_case="binary"

        - data_case="lesbian"
        - data_case="butch"
        - data_case="dyke"
        - data_case="fag"
        - data_case="gay"
        - data_case="twink"
        - data_case="bear"
        - data_case="homo"
        - data_case="sapphic"
        - data_case="achillean"
        - data_case="conflicted_queer_labels"
        - data_case="dykefag"
        - data_case="lesbianism_for_men"
        - data_case="faggotry_for_women"
        - data_case="bi_pan"
        - data_case="ace_aro"

        - data_case="she"
        - data_case="he"
        - data_case="they"
        - data_case="she_female_aligned"
        - data_case="he_male_aligned"

        - data_case = any word from utils/data_lists' social_media_list
    """

    output_list = []

    checking_func = checking_func_dispenser(data_case) # variable function for relevant conditions

    # check words in input list
    for item in sorted(list(set(input_list))):

        # if they fit criteria for being counted 
        if (
            data_case not in [ 
                # cases that need a data_case
                "male_passing",
                "female_passing",
                "afab", 
                "amab",
                "she_female_aligned",
                "he_male_aligned",
                "video", "thing of things","forum","word of mouth","remem",
            ] + social_media_list + offline_categories \
            and checking_func(item))\
        or (
            data_case in [ # data case useable as is
                "afab",
                "amab",
                "video", "thing of things","forum","word of mouth","remem",
            ] + social_media_list + offline_categories \
            and checking_func(item, data_case))\
        or (
            data_case in [ # removing "_passing" or other 8 last letters from data case
                "male_passing",
                "female_passing"
            ] and checking_func(item, data_case[:-8])) \
        or ( # removing "she_" from data_case
            data_case == "she_female_aligned" \
            and checking_func(item, data_case[4:])
        ) or ( # removing "he_" from data_case
            data_case == "he_male_aligned" \
            and checking_func(item, data_case[3:])
        ):
            
            # they are added to output list
            output_list.append(item)

    return output_list


