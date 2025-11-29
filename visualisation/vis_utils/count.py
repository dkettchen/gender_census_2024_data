import pandas as pd
from visualisation.vis_utils.import_data import case_get_lists

def count(input_df:pd.DataFrame, data_case:str):
    """
    prep data by counting columns

    takes a dataframe and a case

    returns a series with relevant values and index labels, 
    sorted in descending value order, and percentage numbers

    - data_case="total_pronoun_users" - counts how many respondants use each pronoun 
    (non-exclusively, ex. someone who uses "she" and "they" will be counted twice)
    - data_case="all_pronoun_combos" - counts how many respondants use each pronoun set combo 
    (mutually exclusive, ex. someone who uses "she" and "they" will be counted once for "she/they")
    """
    new_df = input_df.copy()

    # counting
    new_series = new_df.count() # this becomes a series
    
    # removing index if it is left over
    if "UserID" in new_series.index:
        new_series.pop("UserID")

    # get columns!
    get_list = case_get_lists[data_case]
    new_series = new_series.get(get_list)

    # total length of original df (shortened where relevant, otherwise same as input)
    total_no = len(input_df) 

    # making percent values & rounding em
    new_series = new_series.apply(lambda x: round((x/total_no)*100, 2))

    # sorting descending
    new_series = new_series.sort_values(ascending=False)
    
    # remove any 0 values bc we have no respondants of that label/combo/etc
    new_series = new_series.where(new_series != 0).dropna(how="all")

    return new_series
