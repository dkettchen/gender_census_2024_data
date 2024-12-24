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
from src.sort_person_human_non_human import is_person, is_human
from src.sort_cis import is_cis
from src.sort_trans import is_trans, is_transfemme, is_transmasc, is_detrans
from src.sort_intersex import is_intersex
from src.sort_queer_words import is_wlw, is_mlm

# helper func to dispense the correct function based on data case! ✅
def checking_func_dispenser(data_case:str):
    """
    returns appropriate helper function depending on data case
    """

    func_dict = {
        "male_aligned" : is_male_aligned,
        "non_male_aligned" : is_non_male_aligned,
        "conflicted_male_aligned" : is_conflicted_male_aligned,

        "female_aligned" : is_female_aligned,
        "non_female_aligned" : is_non_female_aligned,
        "conflicted_female_aligned" : is_conflicted_female_aligned,

        "male_passing" : is_present_passing,
        "female_passing" : is_present_passing,

        "both" : is_both,
        "neither" : is_neither,

        "afab" : is_agab, 
        "amab" : is_agab,

        "femme" : is_femme,
        "masc" : is_masc,
        "futch" : is_futch,

        "androgynous" : is_androgynous,
        "androgyne" : is_androgyne,

        "crossdresser" : is_crossdresser,
        "femboy" : is_femboy,

        "autistic" : is_autistic,
        "neurodivergent" : is_neurodivergent,
        "plural" : is_plural,

        "genderqueer" : is_genderqueer,
        "genderfluid" : is_genderfluid,
        "genderflux" : is_genderflux,
        "queer" : is_queer,
        "gnc" : is_gnc,
        "nb" : is_nb,

        "human" : is_human,
        "person" : is_person,

        "trans" : is_trans,
        "transfemme" : is_transfemme,
        "transmasc" : is_transmasc,
        "detrans" : is_detrans,
        "cis" : is_cis,
        "intersex" : is_intersex,

        "wlw" : is_wlw,
        "mlm" : is_mlm,
    }

    #TODO: add queer funcs

    if data_case in func_dict:
        return func_dict[data_case]

