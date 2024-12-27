# (mission statement)
    # take raw data ✅
    # separate questions (relevant ones) into their own files ✅
    # rename columns to be more useable (ie removing question name in favour of file name) ✅

import pandas as pd
from data.raw_data.column_reference import all_columns as questions # columns to collect per question
from utils.excel_reader import read_data_from_excel

# test these with a mock df ✅
    # make a mock df excel file ✅

# separate out question - TESTED ✅
def separate_questions(input_df:pd.DataFrame, question_no:str):
    """
    takes an input df as read from the raw excel file (currently only 2024)
    and a question number

    valid question_nos: 
    - "timestamp"
    - "q1" label (tick boxes)
    - "q2" label (write ins)
    - "q3" title (values)
    - "q7" title (tick boxes)
    - "q9" pronouns (tick boxes)
    - "q34" parent words (tick boxes)
    - "q35" location (values)
    - "q36" age (values)
    - "q37" how did u find this survey (write ins)

    returns a new df 
    with the userID column as index, 
    only the columns of the question requested, 
    any fully empty rows removed, 
    and all none values filled with a "None" string (for csv later)
    """
    # copy input df
    new_df = input_df.copy().dropna(how="all") # removing empty rows

    # list of columns to get
    question_columns = questions[question_no]

    # make sure we get the index from the user id
    index = questions["user_id"]
    new_df = new_df.set_index(index) # gotta fillna to avoid nan in index

    # get columns
    question_df = new_df.get(question_columns).fillna("None")

    # return new separated df
    return question_df

# rename columns to remove question name (or simplify it?) - TESTED ✅
def rename_columns(input_df:pd.DataFrame, question_no:str):
    """
    takes single question df, as output by separate_questions, and the corresponding question number

    returns a new df where the question level of the column names has been dropped
    and the remaining level has been renamed to include the question number 
    (at the beginning of its name) and to be more descriptively 
    or concisively labelled where appropriate
    """
    new_df = input_df.copy()

    # remove q part of column name incl index'
    dropped_df = new_df.reset_index().droplevel(level=0, axis=1)

    # prepping renaming dict
    renaming_dict = {}
    for column_name in dropped_df.columns:

        # custom renaming
        if column_name == "Answer" and question_no == "q3":
            new_column_name = "Title"
        elif column_name == "Unnamed: 140_level_1" and question_no == "q35":
            new_column_name = "Location"
        elif column_name == "Unnamed: 141_level_1" and question_no == "q36":
            new_column_name = "Age"
        elif column_name == "Unnamed: 142_level_1" and question_no == "q37":
            new_column_name = "Survey_Origin"
        elif column_name == "Unnamed: 1_level_1" and question_no == "timestamp":
            new_column_name = "for_sorting"
        elif question_no == "q9": # pronouns
            if "they/them/their/theirs/themself" in column_name:
                new_column_name = "they/them"
            elif "he/him/his/his/himself" in column_name:
                new_column_name = "he/him"
            elif "she/her/her/hers/herself" in column_name:
                new_column_name = "she/her"
            elif "it/it/its/its/itself" in column_name:
                new_column_name = "it/its"
            elif "Spivak - e/em/eir/eirs/emself" in column_name:
                new_column_name = "Spivak_e/em"
            elif "Elverson - ey/em/eir/eirs/emself" in column_name:
                new_column_name = "Elverson_ey/em"
            elif "ae/aer/aer/aers/aerself" in column_name:
                new_column_name = "ae/aer"
            elif "xe/xem/xyr/xyrs/xemself" in column_name:
                new_column_name = "xe/xem"
            elif "fae/faer/faer/faers/faeself" in column_name:
                new_column_name = "fae/faer"
            elif "ze/hir/hir/hirs/hirself" in column_name:
                new_column_name = "ze/hir"
            elif "ze/zir/zir/zirs/zirself" in column_name:
                new_column_name = "ze/zir"
            elif column_name == "Answer":
                new_column_name = "Pronoun_rules"
            else: 
                new_column_name = column_name
        else: 
            new_column_name = column_name

        # adding question no
        renaming_dict[column_name] = question_no + "_" + new_column_name

        # marking optional questions as such
        if question_no in ["q9", "q2"] and (
        new_column_name == "Pronoun_rules" or "Word/phrase" in new_column_name):
            renaming_dict[column_name] += "_(optional)"

    # renaming index too
    renaming_dict['Unnamed: 0_level_1'] = 'UserID'

    # renaming and re-setting the index
    renamed_df = dropped_df.rename(columns=renaming_dict).set_index("UserID")

    return renamed_df

if __name__ == "__main__":
    # read data from excel raw file to input_df
    raw_filepath = "data/raw_data/[GC2024] Unprocessed data.xlsx"
    test_filepath = "data/test_data/head_raw_data.xlsx"

    # raw_data_df = read_data_from_excel(test_filepath) # just first 20 rows
    raw_data_df = read_data_from_excel(raw_filepath) # full file of 48k+ rows

    for question in [ 
        ("timestamp", "for_sorting"), 
        ("q1", "label_tick_boxes"), ("q2", "label_write_ins"),
        ("q3", "title_values"), ("q7", "title_tick_boxes"),
        ("q9", "pronouns"), 
        ("q34", "parent_words"), 
        ("q35", "location"), ("q36", "age"), ("q37", "how_did_you_find_survey"),
    ]:
        
        # separate out correct columns
        separated_qs = separate_questions(raw_data_df, question[0])

        # rename
        renamed_df = rename_columns(separated_qs, question[0])

        # write file
        filepath = f"data/separated_questions/{question[0]}_{question[1]}.csv"
        renamed_df.to_csv(path_or_buf=filepath, header=True)
