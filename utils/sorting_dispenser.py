from src.sort_male_and_female_aligned import (
    is_male_aligned, is_non_male_aligned, is_conflicted_male_aligned,
    is_female_aligned, is_non_female_aligned, is_conflicted_female_aligned,
)
from src.sort_presenting_passing import is_present_passing
from src.sort_both_and_neither import is_both, is_neither
from src.sort_birth_assignments import is_agab
from src.sort_femme_and_masc import is_femme, is_masc, is_futch
from src.sort_androgyny import is_androgyne, is_androgynous

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
