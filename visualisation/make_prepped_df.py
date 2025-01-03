import pandas as pd

def count_df(input_df:pd.DataFrame, data_case:str):
    """
    prep df by counting columns

    returns a df with relevant (as per data_case) columns, 
    sorted in descending value order, 
    and percentage numbers
    """
    new_series = input_df.copy().count() # this becomes a series
    if "UserID" in new_series.index:
        new_series.pop("UserID")

    # get columns!
    if data_case == "total_users":
        get_list = [
            "she_user",
            "he_user",
            "they_user",
            "it_user",
            "neopronoun_user",
            "any_user",

            "questioning",
            "avoid_pronouns/name_as_pronoun",
        ]
    elif data_case == "only_one_set":
        get_list = [
            "she_only",
            "he_only",
            "they_only",
            "it_only",
            "neopronoun_only",
            "avoid_pronouns/use_name_only",
            "questioning_only",
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
            "they/[neo]",
            "she/it/[neo]",
            "he/it/[neo]",
            "they/it/[neo]",
            "it/[neo]",
        ]
    elif data_case in ["pronoun_pie","aligned_pronoun_pie"]:
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
            "they/[neo]",
            "she/it/[neo]",
            "he/it/[neo]",
            "they/it/[neo]",
            "it/[neo]",
            "avoid_pronouns/use_name_only",
            "questioning_only",
        ]
    elif data_case == "tickbox_label_total":
        get_list = new_series.index
    elif data_case == "tickbox_nb_labels":
        get_list = []
        for column in new_series.index:
            for key_word in [
                "nonbinary","enby","nb_",
                "fluid","bigender","agender",
            ]: 
                if key_word in column:
                    get_list.append(column)

    new_series = new_series.get(get_list)

    # special adjustments
    if data_case == "aligned_pronoun_pie":
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

        new_series["female_aligned"] = new_series.get(female_aligned).agg("sum")
        new_series["male_aligned"] = new_series.get(male_aligned).agg("sum")
        new_series["unaligned"] = new_series.get(unaligned).agg("sum")

        new_series = new_series.get(["female_aligned", "male_aligned", "unaligned"])

    new_series = new_series.apply(lambda x: round((x/len(input_df))*100, 2))

    new_series = new_series.sort_values(ascending=False)

    return new_series