import pandas as pd
from visualisation.vis_utils.get_pronoun_alignment import get_pronoun_alignment
from visualisation.vis_utils.count import count

def prep_pronoun_data(input_df:pd.DataFrame):
    
    pronoun_df = input_df.copy()

    data = {}

    # total users per pronoun as per original data (incl any users)
    data["% of respondants who use this pronoun"] = count(pronoun_df, "total_pronoun_users")

    # all combination categories
    all_combos = count(pronoun_df, "all_pronoun_combos")
    data["pronoun sets used by respondants (%)"] = all_combos

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
    data["alignment of pronoun sets used by respondants (%)"] = get_pronoun_alignment(all_combos)
    # count_df(pronoun_df, "aligned_pronoun_pie")

    return data



if __name__ == "__main__":
    from utils.csv_reader import df_from_csv
    pronoun_df = df_from_csv("data/cleaned_q9_with_new_columns/q9_clean_01.csv")
    print(prep_pronoun_data(pronoun_df))