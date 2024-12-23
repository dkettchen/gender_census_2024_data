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

# femme_list = find_case(key_word_dict["femme"], "femme") # femboy should be caught in this already =.=
# masc_list = find_case(key_word_dict["masc"], "masc")

# presentation_list = key_word_dict["femme"] + key_word_dict["masc"] \
#                     + key_word_dict["futch"]
# futch_list = find_case(presentation_list, "futch")

# androgynous_list = find_case(key_word_dict["androgynous"], "androgynous")
# androgyne_list = find_case(key_word_dict["androgynous"], "androgyne")

# crossdresser_list = find_case(key_word_dict["crossdresser"], "crossdresser")

#TODO:

femboy_list = find_case(key_word_dict["femboy"], "femboy")

# autism_list = find_case(key_word_dict["autism"], "autistic")
# neurodiversity = key_word_dict["neurodiversity"] + key_word_dict["autism"]
# neuro_list = find_case(neurodiversity, "neurodivergent")
# plural_list = find_case(key_word_dict["DID"], "plural")

# genderqueer_list = find_case(key_word_dict["genderqueer"], "genderqueer")
# genderfluid_list = find_case(key_word_dict["genderfluid"], "genderfluid")
# genderflux_list = find_case(key_word_dict["genderflux"], "genderflux")
# queer_list = find_case(key_word_dict["queer"], "queer")
# gnc_list = find_case(key_word_dict["gnc"], "gnc")
# nb_list = find_case(key_word_dict["nb"], "nb")

# people_humans_list = find_case(key_word_dict["human/person"], "human/person")
# non_people_humans_list = find_case(key_word_dict["human/person"], "non-human/-person")


# queer words (wlw, mlm, dykefag) -> have not been put into dispenser yet!
# trans & cis -> have not been put into dispenser yet either


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

    # "femme" : femme_list,
    # "masc" : masc_list,
    # "futch" : futch_list,

    # "androgynous": androgynous_list,
    # "androgyne": androgyne_list,

    # "crossdresser": crossdresser_list,

    "femboy" : femboy_list,

    # "autistic" : autism_list,
    # "neurodivergent" : neuro_list,
    # "plural" : plural_list,

    # "genderqueer" : genderqueer_list,
    # "genderfluid" : genderfluid_list,
    # "genderflux" : genderflux_list,
    # "queer" : queer_list,
    # "gnc" : gnc_list,
    # "nb" : nb_list,

    # "human_person" : people_humans_list,
    # "non_human_person" : non_people_humans_list,
}

write_json_files(data_dict, "data/cleaned_q2_write_ins/")