from src.separate_questions import separate_questions, rename_columns
from utils.excel_reader import read_data_from_excel
import pytest
import pandas as pd

@pytest.fixture(scope="class")
def data_head():
    raw_data_df = read_data_from_excel("data/test_data/head_raw_data.xlsx")
    return raw_data_df

class TestRenameColumns:

    def test_returns_df(self,data_head):
        separated_df = separate_questions(data_head, "q1")
        result = rename_columns(separated_df, "q1")
        assert type(result) == pd.DataFrame

    def test_df_has_same_shape_as_input(self,data_head):
        separated_df = separate_questions(data_head, "q1")
        result = rename_columns(separated_df, "q1")
        assert result.shape == separated_df.shape

    def test_df_has_same_data_as_original(self,data_head):
        separated_df = separate_questions(data_head, "q1")
        result = rename_columns(separated_df, "q1")
        for index in range(len(result.columns)):
            result_column = list(result.columns)[index]
            separated_column = list(separated_df.columns)[index]
            assert list(result[result_column]) == list(separated_df[separated_column])

    def test_column_names_have_been_changed(self,data_head):
        separated_df = separate_questions(data_head, "q1")
        result = rename_columns(separated_df, "q1")
        assert list(result.columns) != list(separated_df.columns)

    def test_column_names_have_only_one_level(self,data_head):
        separated_df = separate_questions(data_head, "q1")
        result = rename_columns(separated_df, "q1")
        for item in result.columns:
            assert type(item) == str

    def test_question_names_were_dropped(self,data_head):
        separated_df = separate_questions(data_head, "q1")
        result = rename_columns(separated_df, "q1")
        for item in result.columns:
            assert "Q1. Which" not in item

    def test_column_names_have_been_appropriately_renamed(self,data_head):
        for item in [
            "timestamp","q1","q2","q3","q7","q9","q34","q35","q36","q37"
        ]:
            separated_df = separate_questions(data_head, item)
            result = rename_columns(separated_df, item)
            for column in result.columns:
                assert item + "_" in column

