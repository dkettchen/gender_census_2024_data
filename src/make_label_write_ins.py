import pandas as pd
from utils.csv_reader import df_from_csv

def make_write_in_columns(input_df:pd.DataFrame):
    new_df = collect_write_in_columns(input_df)
    return new_df

def collect_write_in_columns(input_df:pd.DataFrame):
    """
    collects all write ins form the 20 available columns

    returns a new df with the following columns
    - all_write_ins (a list of all the write in items)
    - no_of_write_ins (the length of that list)
    - wrote_in (a yes/no value)

    the new df only contains respondants that did write in (ie only "Yes" wrote_in values)
    """

    write_in_columns = [
        #"UserID",
        "q2_Word/phrase 1_(optional)",
        "q2_Word/phrase 2_(optional)",
        "q2_Word/phrase 3_(optional)",
        "q2_Word/phrase 4_(optional)",
        "q2_Word/phrase 5_(optional)",
        "q2_Word/phrase 6_(optional)",
        "q2_Word/phrase 7_(optional)",
        "q2_Word/phrase 8_(optional)",
        "q2_Word/phrase 9_(optional)",
        "q2_Word/phrase 10_(optional)",
        "q2_Word/phrase 11_(optional)",
        "q2_Word/phrase 12_(optional)",
        "q2_Word/phrase 13_(optional)",
        "q2_Word/phrase 14_(optional)",
        "q2_Word/phrase 15_(optional)",
        "q2_Word/phrase 16_(optional)",
        "q2_Word/phrase 17_(optional)",
        "q2_Word/phrase 18_(optional)",
        "q2_Word/phrase 19_(optional)",
        "q2_Word/phrase 20_(optional)"
    ]

    new_df = input_df.copy().set_index("UserID")

    # adding list, count, and whether they wrote in or no
    indexes = list(new_df.index)
    new_df["all_write_ins"] = "wrong"
    new_df["no_of_write_ins"] = 0
    new_df["wrote_in"] = "No"

    for i in indexes:
        # add all columns to a list for each respondant
        new_list = []
        for column in write_in_columns:
            value = new_df.loc[i][column]
            if value: # if it's not None
                new_list.append(value)
        new_df.at[i,"all_write_ins"] = new_list
        new_df.at[i,"no_of_write_ins"] = len(new_list)
    new_df.loc[new_df['no_of_write_ins'] > 0, 'wrote_in'] = "Yes"

    # we don't need the og columns as we've saved them in the list
    new_df = new_df.get(["all_write_ins","no_of_write_ins",'wrote_in'])

    # shorten data to only those? (as that's all we'd add when joining these?)
    new_df = new_df.where(new_df["wrote_in"] == "Yes").dropna(how="all")

    return new_df

def assign_categories(input_df:pd.DataFrame): #TODO

    # check all categories represented & add columns for em 
    # (face value, not accounting for overlap & conflict yet)

    # possibly a bool for ppl who wrote in stuff that fits any of these categories, 
    # vs ppl who wrote in only other stuff

    pass

def cross_reference(input_df:pd.DataFrame): #TODO

    # cross reference categories (conflicting responses, combo responses (ex "trans" + "woman"), etc)
        # make columns of mutually exclusive categories
    
    # Q. do we cross reference tickbox labels here (= would need to join) or later?
        # -> make a third file combining write ins with tickbox labels 
        # to update tickbox categories in there?

        # but write ins themselves may not contain conflicts with tickbox labels, 
        # so we should join it for making mutually exclusive categories properly

    pass

if __name__ == "__main__":
    read_write_ins_data = df_from_csv("data/separated_questions/q2_label_write_ins.csv")

    # running full file
    # new_df = make_write_in_columns(read_write_ins_data)

    # running partial file
    new_df = make_write_in_columns(read_write_ins_data.head(100))

    new_df.to_csv(path_or_buf="data/cleaned_q2_with_new_columns/q2_clean_01.csv")