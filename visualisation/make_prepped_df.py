import pandas as pd
from visualisation.vis_utils import make_alignment_srs
from visualisation.chart_import_data import case_get_lists

def count_df(input_df:pd.DataFrame, data_case:str):
    """
    prep df by counting columns

    returns a df with relevant (as per data_case) columns, 
    sorted in descending value order, 
    and percentage numbers
    """
    new_df = input_df.copy()

    # shortening df for certain cases
    if data_case == "tickbox_trans_direction_labels": # isolating only trans respondants
        new_df = new_df.where(new_df["is_trans_tickbox"] == "Yes").dropna(how="all")
    elif data_case == "tickbox_non_trans": # isolating only non-trans respondants
        new_df = new_df.where(new_df["is_trans_tickbox"] != "Yes").dropna(how="all")
    elif data_case == "tickbox_non_nb": # isolating only non-nb-umbrella respondants
        new_df = new_df.where(new_df["is_nb_umbrella_tickbox"] != "Yes").dropna(how="all")
    elif data_case == "tickbox_non_nb_trans": # isolating only neither nb nor trans respondants
        new_df = new_df.where(
            (new_df["is_nb_umbrella_tickbox"] != "Yes") & (new_df["is_trans_tickbox"] != "Yes")
        ).dropna(how="all")
    
    new_series = new_df.count() # this becomes a series
    
    # removing index if it is left over
    if "UserID" in new_series.index:
        new_series.pop("UserID")

    # get columns!
    if "pronoun_pie" in data_case:
        get_list = case_get_lists["pronoun_pie"]
    else: get_list = case_get_lists[data_case]
    new_series = new_series.get(get_list)

    # special adjustments
    if data_case == "aligned_pronoun_pie": # adding alignments up using helper func
        new_series = make_alignment_srs(new_series, "pronouns")
    elif data_case == "tickbox_nb_no_nb": # making "is_not_nb" value
        new_series["is_not_nb_tickbox"] = len(new_df) - new_series["is_nb_tickbox"]
    elif data_case == "tickbox_nb_no_nb_umbrella": # making "is_not_nb_umbrella" value
        new_series["is_not_nb_umbrella_tickbox"] = len(new_df) - new_series["is_nb_umbrella_tickbox"]
    elif data_case in ["tickbox_non_trans","tickbox_non_nb","tickbox_non_nb_trans"]: # making "total" value
        new_series["total"] = len(new_df)

    # total length of original df (shortened where relevant, otherwise same as input)
    total_no = len(input_df) 
    # making percent values & rounding em
    new_series = new_series.apply(lambda x: round((x/total_no)*100, 2))

    # sorting descending
    new_series = new_series.sort_values(ascending=False)

    return new_series
