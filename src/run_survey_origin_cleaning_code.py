from utils.read_txt import read_txt
from src.sorting_q37_write_ins.collect_survey_origin_words import collect_key_words_from_q37
from src.find_case import find_case
from utils.json_writer import write_json_files
from utils.data_lists import social_media_list

raw_data = read_txt("q37")
key_word_dict = collect_key_words_from_q37(raw_data)

# making a list of all the items
all_collected_socials = []
for social_media in social_media_list:
    all_collected_socials += key_word_dict[social_media]

all_collected_socials += key_word_dict["mail"] + key_word_dict["website"] \
    + key_word_dict["forum"] + key_word_dict["look"]

all_collected_socials = sorted(list(set(all_collected_socials)))

data_dict = {}

for social_media in social_media_list:
    sm_list = find_case(all_collected_socials, social_media)
    data_dict[social_media] = sm_list

for item in [
    ("video","youtube"), # adding videos to youtube
    ("thing of things","substack"), # adding thing of things to substack
]:
    new_item = item[0]
    old_item = item[1]

    addition_list = find_case(all_collected_socials, new_item)
    data_dict[old_item] += [item for item in addition_list if item not in data_dict[old_item]]

forum_list = find_case(all_collected_socials, "forum")
data_dict["forum"] = forum_list

write_json_files(data_dict, "data/cleaned_q37_write_ins/")

