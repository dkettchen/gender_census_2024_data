from utils.read_txt import read_txt
from src.sorting_q37_write_ins.collect_survey_origin_words import collect_key_words_from_q37
from src.find_case import find_case
from utils.json_writer import write_json_files

raw_data = read_txt("q37")
key_word_dict = collect_key_words_from_q37(raw_data)

