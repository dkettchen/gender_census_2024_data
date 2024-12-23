from src.sort_male_and_female_aligned import (
    is_male_aligned, is_non_male_aligned, is_conflicted_male_aligned,
    is_female_aligned, is_non_female_aligned, is_conflicted_female_aligned,
)
from src.sort_presenting_passing import is_present_passing
from src.sort_both_and_neither import is_both, is_neither
from src.sort_birth_assignments import is_agab
from src.sort_femme_and_masc import is_femme, is_masc, is_futch
from src.sort_androgyny import is_androgyne, is_androgynous
from src.sort_crossdressers import is_crossdresser, is_femboy
from src.sort_neurodiversity import is_autistic, is_neurodivergent, is_plural
from src.sort_other_listed_labels import is_genderfluid, is_genderflux, is_genderqueer, is_queer, is_gnc, is_nb
from src.sort_person_human_non_human import is_non_person_human, is_person_human

# helper func to dispense the correct function based on data case! ✅
def checking_func_dispenser(data_case:str):
    """
    returns appropriate helper function depending on data case
    """
    if data_case == "male_aligned":
        return is_male_aligned
    elif data_case == "non_male_aligned":
        return is_non_male_aligned
    elif data_case == "conflicted_male_aligned":
        return is_conflicted_male_aligned
    elif data_case == "female_aligned":
        return is_female_aligned
    elif data_case == "non_female_aligned":
        return is_non_female_aligned
    elif data_case == "conflicted_female_aligned":
        return is_conflicted_female_aligned
    elif data_case == "male_passing" or data_case == "female_passing":
        return is_present_passing
    elif data_case == "both":
        return is_both
    elif data_case == "neither":
        return is_neither
    elif data_case == "afab" or data_case == "amab":
        return is_agab
    elif data_case == "femme":
        return is_femme
    elif data_case == "masc":
        return is_masc
    elif data_case == "futch":
        return is_futch
    elif data_case == "androgynous":
        return is_androgynous
    elif data_case == "androgyne":
        return is_androgyne
    elif data_case == "crossdresser":
        return is_crossdresser
    elif data_case == "femboy":
        return is_femboy
    elif data_case == "autistic":
        return is_autistic
    elif data_case == "neurodivergent":
        return is_neurodivergent
    elif data_case == "plural":
        return is_plural
    elif data_case == "genderqueer":
        return is_genderqueer
    elif data_case == "genderfluid":
        return is_genderfluid
    elif data_case == "genderflux":
        return is_genderflux
    elif data_case == "queer":
        return is_queer
    elif data_case == "gnc":
        return is_gnc
    elif data_case == "nb":
        return is_nb
    elif data_case == "human/person":
        return is_person_human
    elif data_case == "non-human/-person":
        return is_non_person_human
    #TODO: add queer, trans & cis funcs
