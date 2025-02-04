# Cleaning write ins

## Labels

[src/run_label_write_in_cleaning_code.py](src/run_label_write_in_cleaning_code.py) runs cleaning for the label write ins and saves each collected and categorised list as a json file to [data/cleaned_q2_write_ins/](data/cleaned_q2_write_ins/)

Other files used:
- [utils/read_txt.py](utils/read_txt.py) to read from [data/raw_data/unique_values/q2.txt](data/raw_data/unique_values/q2.txt), which contains all unique write in labels as collected from the raw data
- [src/sorting_q2_write_ins/collect_key_words.py](src/sorting_q2_write_ins/collect_key_words.py) collects the word matches
- [utils/key_word_catches.py](utils/key_word_catches.py) catches any falsely collected words to be removed from the collected list
- [src/sorting_q2_write_ins/sort_](src/sorting_q2_write_ins/) functions determine whether or not a collected item qualifies as the relevant category (these are not 100% robust, so should only be used with the input they're given in the running file for now, as they may not categorise the rest correctly)
- [utils/sorting_helpers.py](utils/sorting_helpers.py) contains some helper functions to check if an item should be in the list collecting male and female words, and to check if a wrong word was caught
- [utils/sorting_dispenser.py](utils/sorting_dispenser.py) dispenses the correct sorting function from [src/sorting_q2_write_ins/](src/sorting_q2_write_ins/)
- [src/find_case.py](src/find_case.py) runs the relevant sorting func on the given collected list -> functions as abstraction for all the util and sorting functions used
- [utils/json_writer.py](utils/json_writer.py) contains a function to write the json files

## Survey origin

[src/run_survey_origin_cleaning_code.py](src/run_survey_origin_cleaning_code.py) runs cleaning for the "where did you find this survey" write ins and saves each collected and categorised list as a json file to [data/cleaned_q37_write_ins/](data/cleaned_q37_write_ins/)

it runs similarly to the label one, including reusing:
- [utils/read_txt.py](utils/read_txt.py) to read from [data/raw_data/unique_values/q37.txt](data/raw_data/unique_values/q37.txt)
- [utils/key_word_catches.py](utils/key_word_catches.py)
- [utils/sorting_helpers.py](utils/sorting_helpers.py)
- [utils/sorting_dispenser.py](utils/sorting_dispenser.py)
- [src/find_case.py](src/find_case.py)
- [utils/json_writer.py](utils/json_writer.py)

however it has its own collection and sorting file:
- [src/sorting_q37_write_ins/collect_survey_origin_words.py](src/sorting_q37_write_ins/collect_survey_origin_words.py)
- [src/sorting_q37_write_ins/sort_social_media.py](src/sorting_q37_write_ins/sort_social_media.py)

# Normalising and formatting raw data

## Separating questions

[src/separate_questions.py](src/separate_questions.py) runs code to separate the full raw data file's columns by each question and saves each question as a csv file to [data/separated_questions/](data/separated_questions/)

Other files used:
- [data/raw_data/column_reference.py](data/raw_data/column_reference.py) provides a dictionary containing lists of all two-level column names by question from the raw data
- [utils/excel_reader.py](utils/excel_reader.py) reads from an excel file and produces a df
- [test/make_test_files.py](test/make_test_files.py) makes smaller test data files of the head(20) and tail(20) of the raw data [data/test_data/](data/test_data/) to use in the testing files
- [test/test_rename_columns.py](test/test_rename_columns.py) and [test/test_separate_questions.py](test/test_separate_questions.py) contain tests for the functions in [src/separate_questions.py](src/separate_questions.py)

## Making pronoun combos

(WIP)

# Visualisation

[visualisation/run_and_make_charts.py](visualisation/run_and_make_charts.py) runs all the current chart code and writes pronoun set chart files in [visualisation/charts/](visualisation/charts) using plotly's kaleido

Other files used:
- [utils/csv_reader.py](utils/csv_reader.py) reads from [data/cleaned_q9_with_new_columns/q9_clean_01.csv](data/cleaned_q9_with_new_columns/q9_clean_01.csv)
- [visualisation/make_prepped_df.py](visualisation/make_prepped_df.py) preps the data for the relevant data_case
- [visualisation/make_bar_charts.py](visualisation/make_bar_charts.py) creates bar charts using plotly
- [visualisation/make_pie_charts.py](visualisation/make_pie_charts.py) creates pie charts using plotly

# Other relevant files

- Methodology document: [methodology.md](methodology.md)
- Reference for the original questions and their tick box answers: [questions.md](questions.md)
- Raw data excel file: data/raw_data/[GC2024] Unprocessed data.xlsx <!-- won't let me link it -->
- Repo "read me" file: [README.md](README.md)