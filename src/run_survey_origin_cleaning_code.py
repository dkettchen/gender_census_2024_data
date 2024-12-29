from utils.read_txt import read_txt
from src.sorting_q37_write_ins.collect_survey_origin_words import collect_key_words_from_q37
from src.find_case import find_case
from utils.json_writer import write_json_files
from utils.data_lists import social_media_list, other_social_media_words

raw_data = read_txt("q37")
key_word_dict = collect_key_words_from_q37(raw_data)

# making a list of all the items
all_collected_socials = []
for social_media in social_media_list + other_social_media_words:
    all_collected_socials += key_word_dict[social_media]

all_collected_socials = sorted(list(set(all_collected_socials)))

data_dict = {}

for social_media in social_media_list:
    sm_list = find_case(all_collected_socials, social_media)
    data_dict[social_media] = sm_list

write_json_files(data_dict, "data/cleaned_q37_write_ins/")

