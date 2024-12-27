#TODO: (mission statement)
# take raw data
# separate questions (relevant ones) into their own files
# rename columns to be more useable (ie removing question name in favour of file name)
import pandas as pd
from data.raw_data.column_reference import all_columns as questions # columns to collect per question
from utils.excel_reader import read_data_from_excel
from utils.csv_writer import make_csv_file

# separate out question
def separate_questions(input_df:pd.DataFrame, question_no:str):
    """
    takes an input df as read from the raw excel file (currently only 2024)
    and a question number

    valid question_nos: 
    - "q1" label (tick boxes)
    - "q2" label (write ins)
    - "q3" title (values)
    - "q7" title (tick boxes)
    - "q9" pronouns (tick boxes)
    - "q34" parent words (tick boxes)
    - "q35" location (values)
    - "q36" age (values)
    - "q37" how did u find this survey (write ins)

    returns a new df with only the columns of the question requested
    """
    # copy input df
    new_df = input_df.copy()

    # list of columns to get
    question_columns = questions[question_no]

    # make sure we get the index from the user id
    index = questions["user_id"]
    #TODO: check what the index sitch is atm
    # if not user id yet -> make it that

    # including timestamps as a means of sorting if need be idk
    timestamps = questions["timestamp"]
    columns_to_get = question_columns + timestamps

    # get columns
    question_df = new_df.get(columns_to_get)

    # return new separated df
    return question_df

#TODO rename columns to remove question name (or simplify it?)
def rename_columns(input_df:pd.DataFrame):
    new_df = input_df.copy()

    # remove q part of column name

    return new_df

#TODO turn into list of lists
def make_list_of_lists(input_df:pd.DataFrame):
    pass

# write new file (ideally csv)

if __name__ == "__main__":
    # read data from excel raw file to input_df
    raw_data_df = read_data_from_excel("data/raw_data/[GC2024] Unprocessed data.xlsx")

    for question in [
        ("q1", "label_tick_boxes"),
        ("q2", "label_write_ins"),
        ("q3", "title_values"),
        ("q7", "title_tick_boxes"),
        ("q9", "pronouns"),
        ("q34", "parent_words"),
        ("q35", "location"),
        ("q36", "age"),
        ("q37", "how_did_you_find_survey"),
    ]:
        # separate out correct columns
        separated_qs = separate_questions(raw_data_df, question[0])

        # rename
        renamed_df = rename_columns(separated_qs)

        # list of lists
        q_list = make_list_of_lists(renamed_df)

        # write file
        make_csv_file(q_list, f"data/separated_questions/{question[0]}_{question[1]}.csv")
