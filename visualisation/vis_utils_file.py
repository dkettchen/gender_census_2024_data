from visualisation.chart_colours import (
    pronoun_colours, alignment_colours, tickbox_labels, other_tickbox_labels,
    other_colours

)
import pandas as pd
import plotly.express as px

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
    elif data_case == "sources":
        colour_ref = px.colors.qualitative.Prism + px.colors.qualitative.Prism + px.colors.qualitative.Prism
    else: 
        colour_ref = other_colours
    
    if data_case == "tickbox_labels": # getting colours based on whether they're tickbox or added columns
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
    elif data_case == "sources":
        colour_list = colour_ref
    else: # getting specific colours for each item
        colour_list = [colour_ref[item] for item in input_list]

    return colour_list

def make_alignment_srs(input_srs:pd.Series, data_case:str):
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

def make_labels(input_list:list, data_case:str, chart_type:str="bar"):
    """
    takes an input series and a data case

    returns formatted labels to be used in the relevant diagram
    """

    labels = []
    for column in input_list:
        new_column = column

        if chart_type == "pie":
            # simplifying any "unspecified" & "conflicted" columns
            for item in ["unspecified", "conflicted"]:
                if item in column:
                    new_column = item
                    break # we don't need to check the second one if we found the first

        if "_tickbox" in new_column: # removing "_tickbox"
            new_column = new_column[:-8]
        
        if data_case in ["tickbox_nb_labels"] or chart_type == "pie" and "tickbox" in data_case:
            if "is_" in new_column: # removing "is_"
                new_column = new_column[3:]

            if new_column in ["nb", "nb_umbrella"] \
            and data_case in ["tickbox_nb_labels"] \
            and chart_type == "bar": # adding "_total"
                new_column += "_total"

        labels.append(new_column)

    return labels
