import pandas as pd

def count_df(input_df:pd.DataFrame, data_case:str):
    """
    prep df by counting columns

    returns a df with relevant (as per data_case) columns, 
    sorted in descending value order, 
    and percentage numbers
    """
    # TODO: refactor tickbox_trans_direction_labels to shorten to only trans ppl at the beginning instead
    
    new_df = input_df.copy()

    # conditionally shortening df for certain cases
    if data_case == "tickbox_non_trans": # isolating only non-trans respondants
        new_df = new_df.where(new_df["is_trans_tickbox"] != "Yes").dropna(how="all")
    elif data_case == "tickbox_non_nb": # isolating only non-nb-umbrella respondants
        new_df = new_df.where(new_df["is_nb_umbrella_tickbox"] != "Yes").dropna(how="all")
    elif data_case == "tickbox_non_nb_trans": # isolating only neither nb nor trans respondants
        new_df = new_df.where(
            (new_df["is_nb_umbrella_tickbox"] != "Yes") & (new_df["is_trans_tickbox"] != "Yes")
        ).dropna(how="all")
    
    new_series = new_df.count() # this becomes a series
    
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
        get_list = [
            "a person/human/[my name]/just me_tickbox",
            "agender_tickbox",
            "bigender_tickbox",
            "binary_tickbox",
            "butch_tickbox",
            "cisgender_tickbox",
            "demiboy_tickbox",
            "demigirl_tickbox",
            "enby_tickbox",
            "fag_tickbox",
            "gender non-conforming_tickbox",
            "genderfluid_tickbox",
            "genderqueer_tickbox",
            "nonbinary_tickbox",
            "queer_tickbox",
            "questioning/unknown_tickbox",
            "trans_tickbox",
            "transfeminine_tickbox",
            "transgender_tickbox",
            "transmasculine_tickbox",
            "no self-description_tickbox",
        ]
    elif data_case == "tickbox_nb_labels":
        get_list = [
            "agender_tickbox",
            "bigender_tickbox",
            "enby_tickbox",
            "genderfluid_tickbox",
            "nonbinary_tickbox",
            "is_nb_tickbox",
            "is_nb_umbrella_tickbox",
        ]
    elif data_case == "tickbox_trans_cis_labels":
        get_list = [
            "is_trans_tickbox",
            "is_cis_tickbox",
            "conflicted_cis/trans_tickbox",
            "unspecified_cis/trans_tickbox",
        ]
    elif data_case == "tickbox_trans_direction_labels":
        get_list = [
            "is_trans_tickbox", # to have the total in there
            "is_transmasc_tickbox",
            "is_transfemme_tickbox",
            "conflicted_transmasc/transfem_tickbox",
            "unspecified_transmasc/transfem_tickbox",
        ]
    elif data_case == "tickbox_nb_no_nb":
        get_list = [
            "is_nb_tickbox"
        ]
    elif data_case == "tickbox_nb_no_nb_umbrella":
        get_list = [
            "is_nb_umbrella_tickbox"
        ]
    elif data_case == "tickbox_non_trans":
        get_list = [ # everything other than trans labels we've excluded already + nb_umbrella total
            "a person/human/[my name]/just me_tickbox",
            "agender_tickbox",
            "bigender_tickbox",
            "binary_tickbox",
            "butch_tickbox",
            "cisgender_tickbox",
            "demiboy_tickbox",
            "demigirl_tickbox",
            "enby_tickbox",
            "fag_tickbox",
            "gender non-conforming_tickbox",
            "genderfluid_tickbox",
            "genderqueer_tickbox",
            "nonbinary_tickbox",
            "queer_tickbox",
            "questioning/unknown_tickbox",
            "no self-description_tickbox",

            "is_nb_umbrella_tickbox",
        ]
    elif data_case == "tickbox_non_nb":
        get_list = [ # everything other than nb umbrella labels we've excluded already
            "a person/human/[my name]/just me_tickbox",
            "binary_tickbox",
            "butch_tickbox",
            "cisgender_tickbox",
            "demiboy_tickbox",
            "demigirl_tickbox",
            "fag_tickbox",
            "gender non-conforming_tickbox",
            "genderqueer_tickbox",
            "queer_tickbox",
            "questioning/unknown_tickbox",
            "trans_tickbox",
            "transfeminine_tickbox",
            "transgender_tickbox",
            "transmasculine_tickbox",
            "no self-description_tickbox",

            "is_trans_tickbox",
        ]
    elif data_case == "tickbox_non_nb_trans":
        get_list = [ # everything other than nb umbrella labels we've excluded already
            "a person/human/[my name]/just me_tickbox",
            "binary_tickbox",
            "butch_tickbox",
            "cisgender_tickbox",
            "demiboy_tickbox",
            "demigirl_tickbox",
            "fag_tickbox",
            "gender non-conforming_tickbox",
            "genderqueer_tickbox",
            "queer_tickbox",
            "questioning/unknown_tickbox",
            "no self-description_tickbox",
        ]

    new_series = new_series.get(get_list)

    # special adjustments
    if data_case == "aligned_pronoun_pie": # adding alignments up
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
    elif data_case == "tickbox_nb_no_nb": # making "is_not_nb" value
        new_series["is_not_nb_tickbox"] = len(new_df) - new_series["is_nb_tickbox"]
    elif data_case == "tickbox_nb_no_nb_umbrella": # making "is_not_nb_umbrella" value
        new_series["is_not_nb_umbrella_tickbox"] = len(new_df) - new_series["is_nb_umbrella_tickbox"]
    elif data_case in ["tickbox_non_trans","tickbox_non_nb","tickbox_non_nb_trans"]: # making "total" value
        new_series["total"] = len(new_df)

    if data_case == "tickbox_trans_direction_labels":
        total_no = new_series["is_trans_tickbox"] # total number of trans people only
    else:
        total_no = len(input_df) # total length of original df (shortened where relevant, otherwise same as input)

    new_series = new_series.apply(lambda x: round((x/total_no)*100, 2))

    # removing total column again after calculating % 
    if data_case == "tickbox_trans_direction_labels":
        new_series.pop("is_trans_tickbox")

    new_series = new_series.sort_values(ascending=False)

    return new_series