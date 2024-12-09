from utils.csv_reader import read_data_from_csv, read_data_from_excel
import pytest
from utils.csv_writer import make_csv_file

# @pytest.fixture
# def raw_list():
#     raw_nested_list = read_data_from_csv("[GC2024] Unprocessed data - RAW DATA do not edit.csv")
#     make_csv_file(raw_nested_list[:10], "raw_data_head.csv")
#     return raw_nested_list

@pytest.fixture(scope="class")
def raw_excel_df():
    return read_data_from_excel("[GC2024] Unprocessed data.xlsx")

class TestData:
    # # check that it's not empty
    # def test_not_empty(self, raw_excel_df):
    #     assert len(raw_excel_df) != 0
    #     assert len(raw_excel_df.dropna(how="all")) != 0

    # def test_number_of_rows(self, raw_excel_df):
    #     assert len(raw_excel_df) == 48646 # I'm assuming that's the correct number for now

    # # check that all rows have same length (as columns we expect)
    # def test_length_of_rows(self, raw_excel_df):
    #     columns_num = len(raw_excel_df.columns)
    #     for row in raw_excel_df.itertuples():
    #         assert len(row) -1 == columns_num # minus 1 cause it seems to count the index as one


    # check what unique values each column contains (should usually be yes/no, find exceptions if any)
    def test_unique_values_for_columns(self, raw_excel_df):
        assert False

# check that if there are any none values, they are converted correctly
# check that if there are any parentheses, they are converted correctly
# check that if there are any numbers, they are converted correctly
