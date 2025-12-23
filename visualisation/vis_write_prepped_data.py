# write prepped data to files for quicker running

from vis_src.data_prep import (
    prep_label_tickbox_data, 
    prep_pronoun_data, 
    prep_pronouns_by_labels, 
    prep_geo_data, 
    prep_survey_origin, 
    prep_write_in_data
)
from utils.csv_reader import df_from_csv
from json import dump
import pandas as pd
from vis_utils.import_data import folders

def convert(input_dict:dict[pd.Series]):
    new_dict = {}
    for key in input_dict:
        new_dict[key] = input_dict[key].to_dict()
    return new_dict

# prep data
pronoun_df = df_from_csv("data/cleaned_q9_with_new_columns/q9_clean_01.csv")
pronoun_data = convert(prep_pronoun_data(pronoun_df))
with open("visualisation/prepped_data/pronouns.json", "w") as file:
    dump(pronoun_data, file, indent=4)

tickbox_label_df = df_from_csv("data/cleaned_q1_with_new_columns/q1_clean_01.csv")
tickbox_label_data = convert(prep_label_tickbox_data(tickbox_label_df))
with open("visualisation/prepped_data/tickbox_labels.json", "w") as file:
    dump(tickbox_label_data, file, indent=4)

pronouns_by_label_data = convert(prep_pronouns_by_labels(tickbox_label_df, pronoun_df))
with open("visualisation/prepped_data/pronouns_by_label.json", "w") as file:
    dump(pronouns_by_label_data, file, indent=4)

geo_df = df_from_csv("data/separated_questions/q35_location.csv")
geo_data = convert(prep_geo_data(geo_df))
with open("visualisation/prepped_data/location.json", "w") as file:
    dump(geo_data, file, indent=4)

source_df = df_from_csv("data/cleaned_q37_with_new_columns/q37_clean_01.csv").set_index("UserID")
timestamp_df = df_from_csv("data/separated_questions/timestamp_for_sorting.csv").set_index("UserID")
source_with_timestamp_df = source_df.join(timestamp_df, lsuffix="left", rsuffix="right")
source_data = convert(prep_survey_origin(source_with_timestamp_df))
with open("visualisation/prepped_data/survey_source.json", "w") as file:
    dump(source_data, file, indent=4)

write_ins_df = df_from_csv("data/cleaned_q2_with_new_columns/q2_cross_referenced_01.csv")
write_in_data = prep_write_in_data(write_ins_df)

converted_write_ins = {}
for key in write_in_data:
    curr_key = write_in_data[key]
    if type(curr_key) == pd.Series:
        converted_write_ins[key] = curr_key.to_dict()
    elif type(curr_key) == pd.DataFrame:
        converted_write_ins[key] = {}
        for column in curr_key.columns:
            converted_write_ins[key][column] = curr_key[column].to_dict()
    else:
        converted_write_ins[key] = {}
        for k in curr_key:
            converted_write_ins[key][k] = {}
            for column in curr_key[k].columns:
                converted_write_ins[key][k][column] = curr_key[k][column].to_dict()

json_folder = folders["json_files"]
with open(f"{json_folder}/write_ins.json", "w") as file:
    dump(converted_write_ins, file, indent=4)