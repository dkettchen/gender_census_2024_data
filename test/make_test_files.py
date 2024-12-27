from utils.excel_reader import read_data_from_excel
import pandas as pd

# read from regular raw excel file # make df
raw_excel_data = read_data_from_excel("data/raw_data/[GC2024] Unprocessed data.xlsx")

# take head of df
head_df = raw_excel_data.copy().head(20)

# take tail too?
tail_df = raw_excel_data.copy().tail(20)

# write (each) into a new excel file in data/test_data/
head_df.to_excel("data/test_data/head_raw_data.xlsx")
tail_df.to_excel("data/test_data/tail_raw_data.xlsx")