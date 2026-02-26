import pandas as pd
from typing import Literal

def get_trans_aligned_pronouns(all_combos_srs:pd.Series, direction:Literal["transmasc", "transfemme"]):
    """
    takes a series of all pronoun set combos

    returns a new series of the relevant numbers added up by whether they include trans-aligned pronouns or not
    """

    # categorise labels by trans alignment
    def usage(entry:str, direction:Literal["transmasc", "transfemme"]):
        """
        determines whether a pronoun set (that conforms to our methodology in terms of order)
        contains trans aligned pronouns or not

        returns a string
        """

        if direction == "transfemme":
            if "she" in entry:
                return "she_user"
            else:
                return "no_she"
        elif direction == "transmasc":
            if entry[:2] == "he" or "/he" in entry:
                return "he_user"
            else: 
                return "no_he"

    ref = pd.Series(all_combos_srs.index, all_combos_srs.index).apply(usage, args=[direction])

    # add up numbers for each category
    if direction == "transfemme":
        usage_list = ["she_user", "no_she"]
    else:
        usage_list = ["he_user", "no_he"]
    usage_series = pd.Series(index=usage_list)
    for a in usage_list:
        usage_series[a] = all_combos_srs.where(
            ref == a
        ).apply("sum")
    
    return usage_series.sort_values(ascending=False)
