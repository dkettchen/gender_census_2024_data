import pandas as pd

case_get_lists = {
    #"case" : ["get", "list"],
    "total_users":[
        "she_user",
        "he_user",
        "they_user",
        "it_user",
        "neopronoun_user",
        "any_user",

        "questioning",
        "avoid_pronouns/name_as_pronoun",
    ],
    "only_one_set":[
        "she_only",
        "he_only",
        "they_only",
        "it_only",
        "neopronoun_only",
        "avoid_pronouns/use_name_only",
        "questioning_only",
    ],
    "big_three_combos":[
        "he/they",
        "she/they",
        "she/he",
        "she/he/they_any"
    ],
    "it_and_neo_combos":[
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
    ],
    "pronoun_pie":[ # also "aligned_pronoun_pie", this one is just combo of only, big three, & it/neo above
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
    ],

    "tickbox_label_total":[
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
    ],
    "tickbox_nb_labels":[
        "agender_tickbox",
        "bigender_tickbox",
        "enby_tickbox",
        "genderfluid_tickbox",
        "nonbinary_tickbox",
        "is_nb_tickbox",
        "is_nb_umbrella_tickbox",
    ],
    "tickbox_trans_cis_labels":[
        "is_trans_tickbox",
        "is_cis_tickbox",
        "conflicted_cis/trans_tickbox",
        "unspecified_cis/trans_tickbox",
    ],
    "tickbox_trans_direction_labels":[
        "is_transmasc_tickbox",
        "is_transfemme_tickbox",
        "conflicted_transmasc/transfem_tickbox",
        "unspecified_transmasc/transfem_tickbox",
    ],
    "tickbox_nb_no_nb":[
        "is_nb_tickbox"
    ],
    "tickbox_nb_no_nb_umbrella":[
        "is_nb_umbrella_tickbox"
    ],
    "tickbox_non_trans":[ # everything other than trans labels we've excluded already + nb_umbrella total
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
    ],
    "tickbox_non_nb":[ # everything other than nb umbrella labels we've excluded already
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
    ],
    "tickbox_non_nb_trans":[ # everything other than nb umbrella labels we've excluded already
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
}

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

# helper func
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