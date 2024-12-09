from utils.csv_reader import read_data_from_csv, read_data_from_excel, df_from_csv
from utils.csv_writer import make_csv_file

# import from csv file
def make_raw_df():
    raw_df = df_from_csv("[GC2024] Unprocessed data - RAW DATA do not edit.csv")
    return raw_df

# def find_unique_values(raw_excel_df):
#     #initial_set = set()
#     for column in raw_excel_df.columns[-5:-1]:
#         #if column[0] == 'Q35. If there are any words that you would like your children to use for you when speaking English that were not listed above, please feel free to enter them here.':
#             # unique_values = list(raw_excel_df[column].unique())
#             # if not (len(unique_values) == 2 and "No" in unique_values and "Yes" in unique_values):
#             #     print(f"{column}: {unique_values},")


#     #     if column[0] == 'Q8. Tell us about any titles not listed above that you want people to use for you, in any order.Please DO NOT type anything other than your title(s). (No definitions, explanations, unabbreviations or pronunciation guides, please.)':
#             # unique_values = raw_excel_df[column].unique()
#             # for value in unique_values:
#             #     initial_set.add(value)
#     #unique_values = list(initial_set)
#     #     # else: 
#             unique_values = raw_excel_df[column].unique()
#             #if not (len(unique_values) == 2 and "No" in unique_values and "Yes" in unique_values):
#             print(f"{column}: {unique_values},")
#     #print(f"'Q35. If there are any words that you would like your children to use for you when speaking English that were not listed above, please feel free to enter them here.': {unique_values},")


# check what values we have
    # test??
# replace yes no values w true false or 1 0 or yes none

# write new csv file

if __name__ == "__main__":
    raw_excel_data = read_data_from_excel("[GC2024] Unprocessed data.xlsx")
    # find_unique_values(raw_excel_data)
