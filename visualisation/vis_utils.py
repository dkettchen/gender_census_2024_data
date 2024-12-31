from visualisation.chart_colours import pronoun_colours

def make_colour_list(input_list:list, data_case:str):
    """
    takes column names list (in order)

    returns corresponding colours in same order

    data_cases:
    - "pronouns"
    """

    if data_case == "pronouns":
        colour_ref = pronoun_colours
    
    colour_list = [colour_ref[item] for item in input_list]

    return colour_list