from utils.read_txt import read_txt
from src.collect_key_words import collect_key_words_from_q2
from src.sort_categories import find_case

raw_data = read_txt("q2")
key_word_dict = collect_key_words_from_q2(raw_data)

# male_list = find_case(key_word_dict["man/boy/male"], "male_aligned")
# non_male_list = find_case(key_word_dict["man/boy/male"], "non_male_aligned")
# confl_male_list = find_case(key_word_dict["man/boy/male"], "conflicted_male_aligned")

female_list = find_case(key_word_dict["woman/girl/female"], "female_aligned")
# non_female_list = find_case(key_word_dict["woman/girl/female"], "non_female_aligned")
# confl_female_list = find_case(key_word_dict["woman/girl/female"], "conflicted_female_aligned")

print(female_list)