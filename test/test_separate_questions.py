from src.separate_questions import separate_questions
from utils.excel_reader import read_data_from_excel
import pytest
import pandas as pd
from data.raw_data.column_reference import all_columns as questions

@pytest.fixture(scope="class")
def data_head():
    raw_data_df = read_data_from_excel("data/test_data/head_raw_data.xlsx")
    return raw_data_df

# @pytest.fixture(scope="class")
# def data_tail():
#     raw_data_df = read_data_from_excel("data/test_data/tail_raw_data.xlsx")
#     return raw_data_df

# don't rly need to test for input mutation bc we're reading from a file & inputting the read data df
# -> don't matter if the read data is mutated bc the actual file won't be touched by this func

class TestSeparate:

    def test_returns_dataframe(self,data_head):
        result = separate_questions(data_head, "q1")
        assert type(result) == pd.DataFrame

    def test_df_not_empty(self,data_head):
        result = separate_questions(data_head, "q1")
        assert len(result) != 0

    def test_df_same_length_as_input_minus_empty_rows(self,data_head):
        result = separate_questions(data_head, "q1")
        assert len(result) == 20

    def test_df_less_columns_than_input(self,data_head):
        result = separate_questions(data_head, "q1")
        assert len(result.columns) < len(data_head.columns)

    def test_df_has_user_id_index(self,data_head):
        result = separate_questions(data_head, "q1")
        # (have to fill na to avoid nan != nan error smh)
        assert list(result.index) == list(data_head.dropna(how="all")[("UserID","Unnamed: 0_level_1")])

    def test_df_contains_only_columns_of_requested_question(self,data_head):
        for item in [
            "timestamp","q1","q2","q3","q7","q9","q34","q35","q36","q37"
        ]:
            result = separate_questions(data_head, item)
            assert list(result.columns) == questions[item]

    def test_df_contains_same_data_as_equivalent_input_columns(self,data_head):
        for item in [
            "timestamp","q1","q2","q3","q7","q9","q34","q35","q36","q37"
        ]:
            result = separate_questions(data_head, item)
            for column in result.columns:
                assert list(
                    result.fillna(0)[column]
                ) == list(
                    data_head.dropna(how="all").fillna(0)[column]
                )