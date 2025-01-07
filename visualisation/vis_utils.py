from visualisation.chart_colours import pronoun_colours, alignment_colours, tickbox_labels, other_tickbox_labels

def make_colour_list(input_list:list, data_case:str):
    """
    takes column names list (in order)

    returns corresponding colours in same order

    data_cases:
    - "pronouns"
    """

    if data_case == "pronouns":
        colour_ref = pronoun_colours
    elif data_case == "alignments":
        colour_ref = alignment_colours
    elif data_case == "tickbox_labels":
        colour_ref = tickbox_labels
    
    if data_case in ["pronouns","alignments"]: # getting specific colours for each item
        colour_list = [colour_ref[item] for item in input_list]
    elif data_case == "tickbox_labels": # getting colours based on whether they're tickbox or added columns
        colour_list = []
        for item in input_list:
            colour = None
            # colour coding all straight up tickbox labels
            if item in tickbox_labels:
                #colour = "indigo"
                colour = tickbox_labels[item]
                
            # colour coding all conflicted & unspecified items the same
            elif "conflicted" in item:
                colour = "firebrick"
            elif "unspecified" in item:
                colour = "slategrey"

            # any other columns
            else: 
                for category in other_tickbox_labels:
                    current_collection = other_tickbox_labels[category]
                    if item in current_collection: # if the column is listed in this one
                        if type(current_collection) == dict: # if we've given it a colour
                            colour = current_collection[item]
                        else: # default colour
                            colour = "purple"
            if not colour: # if we haven't got a colour yet
                if "non_trans" in item:
                    colour = "black"
                elif "non_nb" in item:
                    colour = "black"
                else: colour = "slategrey"
            colour_list.append(colour)

    return colour_list

def make_alignment_srs(input_srs:pd.DataFrame, data_case:str):
    """
    takes an input series with relevant mutually exclusive columns, 
    and a data_case ("pronouns"|"tickbox_labels")

    returns a new series that has 3 columns: ["female_aligned", "male_aligned", "unaligned"] 
    which contain the sum of the values in each of the relevant (aligned/unaligned) columns 
    from the input series
    """

    if data_case == "pronouns":
        female_aligned = [
            "she_only",
            "she/they",
            "she/it",
            "she/[neo]",
            "she/it/[neo]",
        ]
        male_aligned = [
            "he_only",
            "he/they",
            "he/it",
            "he/[neo]",
            "he/it/[neo]",
        ]
        unaligned = [
            "they_only",
            "it_only",
            "neopronoun_only",
            "she/he",
            "she/he/they_any",
            "they/it",
            "they/[neo]",
            "avoid_pronouns/use_name_only",
            "questioning_only",
            "they/it/[neo]",
            "it/[neo]",
        ]

    new_series = input_srs.copy()

    new_series["female_aligned"] = new_series.get(female_aligned).agg("sum")
    new_series["male_aligned"] = new_series.get(male_aligned).agg("sum")
    new_series["unaligned"] = new_series.get(unaligned).agg("sum")

    new_series = new_series.get(["female_aligned", "male_aligned", "unaligned"])

    return new_series
