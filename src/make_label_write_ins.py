import pandas as pd
from utils.csv_reader import df_from_csv
from utils.read_all_categories import read_all_categories

def make_write_in_columns(input_df:pd.DataFrame):
    new_df = collect_write_in_columns(input_df)
    return new_df

def collect_write_in_columns(input_df:pd.DataFrame):
    """
    collects all write ins from the 20 available columns

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

def assign_categories(input_df:pd.DataFrame):
    """
    takes an input_df with the following columns: ["UserID", "all_write_ins", "no_of_write_ins", "wrote_in"] 
    (an index column and all_write_ins:list are required)

    reads all label category json files from "data/cleaned_q2_write_ins/" and adds [category]_user column,
    denoting whether a label from that category is among the participant's label list
    
    ex ["probably male"] -> is in male_aligned category -> will have a "Yes" in "male_aligned_user" column

    it also adds a column named "useable_write_ins" to track whether any of the participant's write-ins 
    were found in the categories or if they only wrote in uncategorised (ie not particularly useful) labels
    (we're using a very broad definition of "useful" here 🤦‍♂️)

    returns a new df with the input and added columns
    """

    all_categories_dict = read_all_categories("data/cleaned_q2_write_ins/")

    new_df = input_df.copy()

    # getting all label lists
    label_list_column = new_df["all_write_ins"]

    # did they write in smth useable?
    new_df["useable_write_ins"] = "No" # default value

    # check all categories represented & add columns for em 
    # (face value, not accounting for overlap & conflict yet)
    for key in sorted(list(all_categories_dict.keys())): # going through all categories
        column_name = key + "_user" # making new column name
        new_df[column_name] = "No" # making blank default column

        for i in label_list_column.index: # going through all rows
            current_label_list = label_list_column.loc[i]
            for label in current_label_list: # checking all labels this participant uses
                if label in all_categories_dict[key]: # if they use a label from this category
                    new_df.loc[i, column_name] = "Yes"
                    if new_df.loc[i, "useable_write_ins"] == "No": 
                        new_df.loc[i, "useable_write_ins"] = "Yes" # they wrote in smth useable!

    return new_df

if __name__ == "__main__":
    read_write_ins_data = df_from_csv("data/separated_questions/q2_label_write_ins.csv")

    # running full file
    new_df = make_write_in_columns(read_write_ins_data)

    # running partial file
    # new_df = make_write_in_columns(read_write_ins_data.head(100))

    # making plain columns
    new_df = assign_categories(new_df)

    new_df.to_csv(path_or_buf="data/cleaned_q2_with_new_columns/q2_clean_01.csv")