import pandas as pd

def count_df(input_df:pd.DataFrame, data_case:str):
    """
    prep df by counting columns

    returns a df with relevant (as per data_case) columns, 
    sorted in descending value order, 
    and percentage numbers
    """
    new_series = input_df.copy().count() # this becomes a series

    if data_case == "total_users":
        get_list = [
            "she_user",
            "he_user",
            "they_user",
            "it_user",
            "neopronoun_user",
            "any_user"
        ]
    elif data_case == "only_one_set":
        get_list = [
            "she_only",
            "he_only",
            "they_only",
            "it_only",
            "neopronoun_only"
        ]
    elif data_case == "big_three_combos":
        get_list = [
            "he/they",
            "she/they",
            "she/he",
            "she/he/they_any"
        ]
    elif data_case == "it_and_neo_combos":
        get_list = [
            "he/it",
            "she/it",
            "they/it",
            "he/[neo]",
            "she/[neo]",
            "they/[neo]"
        ]
    elif data_case == "pronoun_pie":
        get_list = [
            "she_only",
            "he_only",
            "they_only",
            "it_only",
            "neopronoun_only",
            "he/they",
            "she/they",
            "she/he",
            "she/he/they_any",
            "he/it",
            "she/it",
            "they/it",
            "he/[neo]",
            "she/[neo]",
            "they/[neo]"
        ]

    new_series = new_series.get(get_list)

    new_series = new_series.apply(lambda x: round((x/len(input_df))*100, 2))

    new_series = new_series.sort_values(ascending=False)

    return new_series