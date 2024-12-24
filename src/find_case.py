from utils.sorting_dispenser import checking_func_dispenser

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
        - data_case="femboy"

        - data_case="autistic"
        - data_case="neurodivergent"
        - data_case="plural"

        - data_case="genderqueer"
        - data_case="genderfluid"
        - data_case="genderflux"
        - data_case="queer"
        - data_case="gnc"
        - data_case="nb"

        - data_case="human"
        - data_case="person"

        - data_case="trans"
        - data_case="transfemme"
        - data_case="transmasc"
        - data_case="detrans"
        - data_case="cis"
        - data_case="intersex"
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


