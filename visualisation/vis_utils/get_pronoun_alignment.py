import pandas as pd

def get_pronoun_alignment(all_combos_srs:pd.Series):
    """
    takes a series of all pronoun set combos

    returns a new series of the relevant numbers added up by whether they're 
    "female_aligned", "male_aligned", or "unaligned"
    """

    # categorise labels by alignment
    def alignments(entry:str):
        """
        determines whether a pronoun set (that conforms to our methodology in terms of order)
        is male-, female- or unaligned

        returns a string
        """
        if "she" in entry and "/he" not in entry:
            return "female_aligned"
        elif ("he/" in entry or "he_" in entry) and "she" not in entry:
            return "male_aligned"
        else:
            return "unaligned"
    alignment_ref = pd.Series(all_combos_srs.index, all_combos_srs.index).apply(alignments)

    # add up numbers for each alignment
    alignment_list = ["female_aligned", "male_aligned", "unaligned"]
    alignment_series = pd.Series(index=alignment_list)
    for a in alignment_list:
        alignment_series[a] = all_combos_srs.where(
            alignment_ref == a
        ).apply("sum")
    
    return alignment_series.sort_values(ascending=False)
