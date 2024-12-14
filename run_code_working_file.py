from utils.read_txt import read_txt
from src.collect_key_words import collect_key_words_from_q2
from src.sort_categories import find_case

raw_data = read_txt("q2")
key_word_dict = collect_key_words_from_q2(raw_data)
male_aligned_list = find_case(key_word_dict["man/boy/male"], "male_aligned")
print(male_aligned_list)