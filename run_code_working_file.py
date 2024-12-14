from utils.read_txt import read_txt
from src.collect_key_words import collect_key_words_from_q2
from src.sort_categories import sort_men

raw_data = read_txt("q2")
key_word_dict = collect_key_words_from_q2(raw_data)
men_sorted = sort_men(key_word_dict)