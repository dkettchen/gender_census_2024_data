# pronoun combos we wanna track:
    # she they and he only
    # she/they / they/she
    # he/they / they/he
    # all three / any
    # neo pronouns only
    # any of previous options + neo pronouns (can check this via rel column x neopronouns user column)
import pandas as pd
from utils.csv_reader import df_from_csv

def make_pronoun_combos(input_df:pd.DataFrame):
    """
    takes an input df as read from q9 pronouns separated raw file

    returns a new df containing columns denoting whether someone
    - uses she, he, they, or it (not mutually exclusively -> straight from input data)
    - uses (any) neopronouns

    - how many sets (excluding "any", "questioning" and 
    "avoid pronouns/name as pronoun" options) they use in total
    - how many of the big three sets (he, she, they) they use

    - uses any of the above exclusively (ie only they/them, no other pronouns)
    - ticked "any" pronouns option

    - uses she or he, with they (ie she/they, he/they, they/she) 
    (not exclusive of it or neopronouns, ie he/they/ze would be included)
    - uses she and he pronouns (ie s/he) 
    (not exclusive of it or neopronouns, ie she/he/it would be included)
    - uses he, she, or they, with it pronouns (ie he/it) 
    - uses he, she, or they, with neopronouns (ie they/ze) 
    (we do not specify which neopronouns tho)

    - uses (at least) she, he, and they (ie she/he/they)
    """

    renaming_dict = {
        "q9_they/them" : "they_user",
        "q9_he/him" : "he_user",
        "q9_it/its" : "it_user",
        "q9_she/her" : "she_user",
        "q9_Questioning or unknown" : "questioning",
        "q9_Avoid pronouns / use name as pronoun" : "avoid_pronouns/name_as_pronoun",
        "q9_Any" : "any_user",
    }

    new_df = input_df.copy().rename(columns=renaming_dict)

    new_df.pop("q9_Pronoun_rules_(optional)") # getting rid of this right away cause Idc abt it

    # making useable none values for later
    for column in new_df:
        new_df[column] = new_df[column].mask(new_df[column] == "No", other="None").fillna("None")

    # make new column with count of how many pronoun sets someone uses (total & of big three)
    for set_case in ["number_of_sets", "number_of_big_three"]:

        # setting up dfs
        new_df[set_case] = 0
        temp_df = new_df.copy()
        if set_case == "number_of_sets":
            temp_df.pop("any_user")
            temp_df.pop("questioning")
            temp_df.pop("avoid_pronouns/name_as_pronoun")
        elif set_case == "number_of_big_three":
            temp_df = temp_df.get(["she_user","he_user","they_user"])

        # counting
        number_of_sets = pd.Series(index=temp_df.index)
        for row in temp_df.index:
            current_row = [item for item in temp_df.iloc[row] if item == "Yes"]
            number_of_sets[row] = len(current_row)
        
        # inserting
        new_df[set_case] = number_of_sets

    # make new column for anyone who uses neo pronouns
    new_df["neopronoun_user"] = "Yes"
    new_df["neopronoun_user"] = new_df["neopronoun_user"].where(
        (
            new_df["q9_Spivak_e/em"] == "Yes") | (
            new_df["q9_Elverson_ey/em"] == "Yes") | (
            new_df["q9_ae/aer"] == "Yes") | (
            new_df["q9_xe/xem"] == "Yes") | (
            new_df["q9_fae/faer"] == "Yes") | (
            new_df["q9_ze/hir"] == "Yes") | (
            new_df["q9_ze/zir"] == "Yes") | (
            new_df["q9_A pronoun set not listed here"] == "Yes"
        ), other="None"
    )

    # of ppl who uses one set only: make a column for each of the five options
    for set_case in [
        "she_user",
        "he_user",
        "they_user",
        "it_user",
        "neopronoun_user",
    ]:
        new_column_name = set_case[:-4] + "only"
        new_df[new_column_name] = "Yes"
        new_df[new_column_name] = new_df[new_column_name].where(
            (new_df[set_case] == "Yes") & (new_df["number_of_sets"] == 1),
            other="None"
        )
    
    # of ppl who use 2 sets: make a column for he/they, she/they, and she/he
    # make a new column for anyone who uses one of the big three and it pronouns
    # make a new column for anyone who uses one of the big three and neo pronouns
    for set_case in [
        ("she","they"),
        ("he","they"),
        ("she","he"),

        ("she","it"),
        ("he","it"),
        ("they","it"),

        ("she","[neo]"),
        ("he","[neo]"),
        ("they","[neo]"),
    ]:
        first_column = set_case[0] + "_user"
        if set_case[1] == "[neo]":
            second_column = "neopronoun_user"
        else: second_column = set_case[1] + "_user"
        set_name = set_case[0] + "/" + set_case[1]

        if set_case in [
            ("she","they"),
            ("he","they"),
            ("she","he"),
        ]:
            # we want to be able to cross reference with neo pronouns later
            number_column = "number_of_big_three" 
        else: number_column = "number_of_sets"

        new_df[set_name] = "Yes"
        new_df[set_name] = new_df[set_name].where(
            (
                new_df[first_column] == "Yes") & (
                new_df[second_column] == "Yes") & (
                new_df[number_column] == 2
            ), other="None"
        )

    # make a new column for anyone who uses all 3 big three
    new_df["she/he/they"] = "Yes"
    new_df["she/he/they"] = new_df["any_user"].where(
        (new_df["number_of_big_three"] == 3), 
        other="None"
    )

    # remove neo pronoun columns?
    for neo_pronoun_column in [
        "q9_Spivak_e/em",
        "q9_Elverson_ey/em",
        "q9_ae/aer",
        "q9_xe/xem",
        "q9_fae/faer",
        "q9_ze/hir",
        "q9_ze/zir",
        "q9_A pronoun set not listed here",
    ]:
        new_df.pop(neo_pronoun_column)

    return new_df

# test with only small sample for faster running
if __name__ == "__main__":
    read_data = df_from_csv("data/separated_questions/q9_pronouns.csv")

    new_df = make_pronoun_combos(read_data.head(100))

    new_df.to_csv(path_or_buf="data/cleaned_q9_with_new_columns/q9_clean_01.csv")