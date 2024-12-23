from utils.read_txt import read_txt
from src.collect_key_words import collect_key_words_from_q2
from src.find_case import find_case
from utils.json_writer import write_json_files

raw_data = read_txt("q2")
key_word_dict = collect_key_words_from_q2(raw_data)

# male_list = find_case(key_word_dict["man/boy/male"], "male_aligned")
# non_male_list = find_case(key_word_dict["man/boy/male"], "non_male_aligned")
# confl_male_list = find_case(key_word_dict["man/boy/male"], "conflicted_male_aligned")

# female_list = find_case(key_word_dict["woman/girl/female"], "female_aligned")
# non_female_list = find_case(key_word_dict["woman/girl/female"], "non_female_aligned")
# confl_female_list = find_case(key_word_dict["woman/girl/female"], "conflicted_female_aligned")

# binaries_list = key_word_dict["man/boy/male"] + key_word_dict["woman/girl/female"]

# male_passing_list = find_case(binaries_list, "male_passing")
# female_passing_list = find_case(binaries_list, "female_passing")

# both_and_neither_list = binaries_list + key_word_dict["both"] + key_word_dict["neither"]

# both_list = find_case(both_and_neither_list, "both")
# neither_list = find_case(both_and_neither_list, "neither")

# birth_assignments_list = binaries_list + key_word_dict["both"] \
#     + key_word_dict["trans"] + key_word_dict["transmasc"] + key_word_dict["transfemme"] \
#     + key_word_dict["afab"] + key_word_dict["amab"]

# afab_list = find_case(birth_assignments_list, "afab")
# amab_list = find_case(birth_assignments_list, "amab")

femme_list = find_case(key_word_dict["femme"], "femme") # femboy should be caught in this already =.=
masc_list = find_case(key_word_dict["masc"], "masc")

presentation_list = key_word_dict["femme"] + key_word_dict["masc"] \
                    + key_word_dict["futch"] #+ key_word_dict["androgynous"]
futch_list = find_case(presentation_list, "futch")

# print(confl_female_list)

data_dict = {
    # "male_aligned" : male_list,
    # "non_male_aligned" : non_male_list,
    # "conflicted_male_aligned" : confl_male_list,

    # "female_aligned" : female_list,
    # "non_female_aligned" : non_female_list,
    # "conflicted_female_aligned" : confl_female_list,

    # "male_present_passing": male_passing_list,
    # "female_present_passing": female_passing_list,

    # "both": both_list,
    # "neither": neither_list,

    # "afab" : afab_list,
    # "amab" : amab_list,

    "femme" : femme_list,
    "masc" : masc_list,
    "futch" : futch_list,
}

write_json_files(data_dict, "data/cleaned_q2_write_ins/")