import pandas as pd
from visualisation.vis_utils.get_pronoun_alignment import get_pronoun_alignment
from visualisation.vis_utils.count import count
from visualisation.vis_utils.import_data import case_get_lists
from visualisation.vis_utils.geo_utils import english_speaking, other_countries
from visualisation.vis_utils.make_percent import percent

def prep_pronoun_data(input_df:pd.DataFrame):
    """
    takes a df with data from question 9 (pronouns)

    returns a dict with descriptive keys and Series values containing the relevant data

    pronoun data includes:
    - "% of respondants who use this pronoun"
    - "Pronoun sets used by respondants (%)"
    - "% of respondants who only use one pronoun"
    - "% of respondants who use a combination of the big three"
    - "% of respondants whose multi-pronoun set includes it and/or neo pronouns"
    - "Alignment of pronoun sets used by respondants (%)"
    """
    
    pronoun_df = input_df.copy()

    data = {}

    # total users per pronoun as per original data (incl any users)
    data["% of respondants who use this pronoun"] = count(pronoun_df, "total_pronoun_users")

    # all combination categories
    all_combos = count(pronoun_df, "all_pronoun_combos")
    data["Pronoun sets used by respondants (%)"] = all_combos

    # sub sets of all pronoun combos
    # only one set/type users
    data["% of respondants who only use one pronoun"] = all_combos.where(
        all_combos.index.str.contains("_only")
    ).dropna(how="all") # count_df(pronoun_df, "only_one_set")
    # big three combos (she/they, he/they, she/he, she/he/they)
    data["% of respondants who use a combination of the big three"] = all_combos.where(
        ~all_combos.index.str.contains(
            "_only"
        ) & ~all_combos.index.str.contains(
            "it"
        ) & ~all_combos.index.str.contains(
            "neo"
        )
    ).dropna(how="all") # count_df(pronoun_df, "big_three_combos")
    # combos with it and neo pronouns
    data["% of respondants whose multi-pronoun set includes it and/or neo pronouns"] = all_combos.where(
        ~all_combos.index.str.contains(
            "_only"
        ) & (all_combos.index.str.contains(
            "it"
        ) | all_combos.index.str.contains(
            "neo"
        ))
    ).dropna(how="all") # count_df(pronoun_df, "it_and_neo_combos")

    # by alignment
    data["Alignment of pronoun sets used by respondants (%)"] = get_pronoun_alignment(all_combos)
    # count_df(pronoun_df, "aligned_pronoun_pie")

    return data

def prep_label_tickbox_data(input_df:pd.DataFrame):
    """
    takes a df with data from question 1 (tickbox labels)

    returns a dict with descriptive keys and Series values containing the relevant data

    tickbox label data includes:
    - "% of respondants who ticked this label"
    - "% of respondants who use nb umbrella labels"
    - "Trans status (%)"
    - "Transition direction of trans respondants (%)"
    - "Nb umbrella label use (%)"
    - "Top labels (used by > 1/5) of {
        trans|nb|non-trans|non-nb|trans-nb|neither trans nor nb
    } respondants ({x}% of total) (%)"
    - "Trans and nb intersection (%)"
    """

    tickbox_df = input_df.copy()

    # prep subset dfs
    trans_df = tickbox_df.where(tickbox_df["is_trans_tickbox"] == "Yes").dropna(how="all")
    nb_df = tickbox_df.where(tickbox_df["is_nb_umbrella_tickbox"] == "Yes").dropna(how="all")

    data = {}

    # total users per tickbox label (as is)
    data["% of respondants who ticked this label"] = count(tickbox_df, "tickbox_label_total")

    # nb label users vs total nb umbrella label users
    # nb labels vs other nb umbrella labels (comparison in each label's numbers)
    data["% of respondants who use nb umbrella labels"] = count(tickbox_df, "tickbox_nb_labels")

    # trans, cis, conflicted, unspecified
    data["Trans status (%)"] = count(tickbox_df, "tickbox_trans_cis_labels")

    # transmasc, transfemme, unspecified trans
    data["Transition direction of trans respondants (%)"] = count(trans_df, "tickbox_trans_direction_labels")

    # what labels nb users use
    for category in case_get_lists["tickbox_nb_and_umbrella"]:
        nb_df[category] = "Yes"
    nb_df["uses_both"] = nb_df["uses_both"].where( # nb yes, nb umb yes
        (nb_df["is_nb_tickbox"] == "Yes") & (nb_df["is_a_bi_fluid_gender_tickbox"] == "Yes")
    )
    nb_df["only_uses_nb"] = nb_df["only_uses_nb"].where( # nb yes, nb umb no
        (nb_df["is_nb_tickbox"] == "Yes") & (nb_df["is_a_bi_fluid_gender_tickbox"] != "Yes")
    )
    nb_df["only_uses_agender/bigender/genderfluid"] = nb_df["only_uses_agender/bigender/genderfluid"].where( # nb no, nb umb yes
        (nb_df["is_nb_tickbox"] != "Yes") & (nb_df["is_a_bi_fluid_gender_tickbox"] == "Yes")
    )
    data["Nb umbrella label use (%)"] = count(nb_df, "tickbox_nb_and_umbrella")

    # prep for later
    trans_and_nb = pd.Series(index=["trans_only", "nb_only", "trans_and_nb", "neither_trans_nor_nb"])

    # most popular labels for relevant sub-sets of respondants
    for c in ["trans", "non-trans", "nb_umbrella", "non-nb_umbrella", "trans-nb", "neither trans nor nb"]: 
        # prep subsets
        if "trans" in c and "nb" in c:
            if "neither" in c:
                df = tickbox_df.where(
                    (tickbox_df[f"is_trans_tickbox"] != "Yes") & (
                        tickbox_df[f"is_nb_umbrella_tickbox"] != "Yes")
                ).dropna(how="all")
                # add this as well while we have the df
                trans_and_nb["neither_trans_nor_nb"] = round((len(df) / len(tickbox_df)) * 100, 2)
            else:
                df = trans_df.where(
                    trans_df[f"is_nb_umbrella_tickbox"] == "Yes"
                ).dropna(how="all")
                # add this as well while we have the df
                trans_and_nb["trans_and_nb"] = round((len(df) / len(tickbox_df)) * 100, 2)
        elif "non-" in c:
            df = tickbox_df.where(tickbox_df[f"is_{c[4:]}_tickbox"] != "Yes").dropna(how="all")
        elif c == "trans":
            df = trans_df
        elif c == "nb_umbrella":
            df = nb_df

        # remove _umbrella bit so we can reuse it for labels
        if "nb_umbrella" in c: c = c[:-9]

        # count total labels for this subset
        srs = count(df, "tickbox_label_total")

        # only include labels used by over 1/5 of subset
        srs = srs.where(srs > 20).dropna(how="all")

        # calculate percent of total respondants this subset makes up
        total_percent = round((len(df) / len(tickbox_df)) * 100, 2)

        # add to data dict
        data[f"Top labels (used by > 1/5) of {c} respondants ({total_percent}% of total) (%)"] = srs

    # add other values
    trans_and_nb["trans_only"] = round((len(
        trans_df.where(trans_df["is_nb_umbrella_tickbox"] != "Yes").dropna(how="all")
    ) / len(tickbox_df)) * 100, 2)
    trans_and_nb["nb_only"] = round((len(
        nb_df.where(nb_df["is_trans_tickbox"] != "Yes").dropna(how="all")
    ) / len(tickbox_df)) * 100, 2)

    # how many respondants are trans/not nb, nb/not trans, trans+nb, neither (with umbrella)
    data["Trans and nb intersection (%)"] = trans_and_nb.sort_values(ascending=False)

    return data

def prep_pronouns_by_labels(label_df:pd.DataFrame, pronoun_df:pd.DataFrame):
    """
    takes dfs with data from question 1 (tickbox labels) and question 9 (pronouns)

    returns a dict with descriptive keys and Series values containing the relevant data

    it checks for the following label categories:
    - cis
    - transmasc
    - transfemme
    - unspecified cis/trans status
    - trans but unspecified direction

    the returned data includes
    - pronoun sets used by respondants of the relevant category (%)
    - the alignment of those pronoun sets (%)
    """

    # join dfs
    pronouns_x_labels = pronoun_df.join(label_df, lsuffix="left", rsuffix="right")

    # prep df with label categories

    # groups we want:
    categories = {
        # trans directions
        "is_transmasc_tickbox": "transmasc",
        "is_transfemme_tickbox": "transfemme",
        # unspecified trans direction
        "conflicted_transmasc/transfem_tickbox": "unspecified_trans",
        "unspecified_transmasc/transfem_tickbox": "unspecified_trans",
        # cis
        "is_cis_tickbox": "cis",
        # unspecified trans/cis status
        "conflicted_cis/trans_tickbox": "unspecified_cis_trans",
        "unspecified_cis/trans_tickbox": "unspecified_cis_trans",
    }

    # make a column of groups we want
    pronouns_x_labels["trans_status"] = None
    for column_name in categories:
        pronouns_x_labels["trans_status"] = pronouns_x_labels["trans_status"].mask(
            pronouns_x_labels[column_name] == "Yes", # check column in question
            other=categories[column_name] # mark with category label
        )

    data = {}
    
    # count pronoun sets per each category
    get_list = ["trans_status"] + case_get_lists["all_pronoun_combos"]
    pronoun_sets = pronouns_x_labels.get(get_list).groupby(by="trans_status").count().transpose()

    # separate, process & save them to our data dict with descriptive labels
    for column in pronoun_sets.columns:
        if "_" in column:
            label = ""
            suffix = " of unspecified"
            if "cis" in column:
                suffix += " cis/trans status"
            else:
                label += " trans"
                suffix += " direction"
        else:
            label = " " + column
            suffix = ""
        
        # get total number of this category
        total_respondants = pronoun_sets[column].sum()
        # get their pronoun sets
        label_sets = pronoun_sets[column].sort_values(ascending=False).apply(
            percent, args=[total_respondants]
        )
        # pronoun sets
        data[f"Pronoun sets used by{label} respondants{suffix}"] = label_sets
        # pronoun alignments
        data[f"Pronoun alignments of{label} respondants{suffix}"] = get_pronoun_alignment(label_sets)

    return data

def prep_geo_data(input_df:pd.DataFrame):

    geo_df = input_df.copy().set_index("UserID")

    total_geo_srs = geo_df["q35_Location"] # countries column
    english_geo_srs = english_speaking(geo_df)["english_or_no"]

    total_respondants = len(geo_df)
    data = {}

    for data_case in ["total", "english-speaking"]:
        if data_case == "total":
            srs = total_geo_srs
        else:
            srs = english_geo_srs
        
        srs = srs.dropna(how="all")
        
        # fixing list values back to strings smh
        for i in range(len(srs)):
            item = srs.iloc[i]
            if type(item) != str:
                srs.iloc[i] = str(item)

        country_srs = srs.groupby(by=srs.values).count().sort_values(ascending=False)
        country_srs = country_srs.apply(percent, args=[total_respondants])

        if data_case == "total": # adding "other countries" for any countries under 0.5%
            country_srs = other_countries(country_srs, total_respondants)

        data[f"Location of respondants ({data_case})"] = country_srs

    return data

# TODO survey origin

if __name__ == "__main__":
    from utils.csv_reader import df_from_csv

    # pronoun_df = df_from_csv("data/cleaned_q9_with_new_columns/q9_clean_01.csv")
    # print(prep_pronoun_data(pronoun_df))

    # tickbox_label_df = df_from_csv("data/cleaned_q1_with_new_columns/q1_clean_01.csv")
    # print(prep_label_tickbox_data(tickbox_label_df))

    # print(prep_pronouns_by_labels(tickbox_label_df, pronoun_df))

    geo_df = df_from_csv("data/separated_questions/q35_location.csv")
    print(prep_geo_data(geo_df))