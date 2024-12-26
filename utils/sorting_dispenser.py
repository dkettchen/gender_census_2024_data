from src.sorting_q2_write_ins.sort_male_and_female_aligned import (
    is_male_aligned, is_non_male_aligned, is_conflicted_male_aligned,
    is_female_aligned, is_non_female_aligned, is_conflicted_female_aligned,
)
from src.sorting_q2_write_ins.sort_presenting_passing import is_present_passing
from src.sorting_q2_write_ins.sort_both_and_neither import is_both, is_neither
from src.sorting_q2_write_ins.sort_birth_assignments import is_agab
from src.sorting_q2_write_ins.sort_femme_and_masc import is_femme, is_masc, is_futch
from src.sorting_q2_write_ins.sort_androgyny import is_androgyne, is_androgynous
from src.sorting_q2_write_ins.sort_crossdressers import is_crossdresser, is_femboy, is_sissy, is_trap
from src.sorting_q2_write_ins.sort_neurodiversity import is_autistic, is_neurodivergent, is_plural
from src.sorting_q2_write_ins.sort_other_listed_labels import is_genderfluid, is_genderflux, is_genderqueer, is_queer, is_gnc, is_nb
from src.sorting_q2_write_ins.sort_person_human_non_human import is_person, is_human
from src.sorting_q2_write_ins.sort_cis_binary import is_cis, is_binary
from src.sorting_q2_write_ins.sort_trans import is_trans, is_transfemme, is_transmasc, is_detrans
from src.sorting_q2_write_ins.sort_intersex import is_intersex
from src.sorting_q2_write_ins.sort_queer_words import (
    is_conflicting_queer,
    is_lesbian, 
    is_achillean, 
    is_ace_aro, 
    is_bear, 
    is_bi_pan, 
    is_butch, 
    is_dyke, 
    is_sapphic, 
    is_fag, 
    is_gay,
    is_homosexual,
    is_twink,
    is_dykefag,
    is_lesbianism_for_men,
    is_faggotry_for_women,
)
from src.sorting_q2_write_ins.sort_agender_and_neutral import is_genderless, is_neutral, is_demi
from src.sorting_q2_write_ins.sort_pronouns import is_he, is_she, is_they
from src.sorting_q2_write_ins.sort_bigender import is_genderfull

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
        "sissy" : is_sissy,
        "trap" : is_trap,

        "autistic" : is_autistic,
        "neurodivergent" : is_neurodivergent,
        "plural" : is_plural,

        "genderqueer" : is_genderqueer,
        "genderfluid" : is_genderfluid,
        "genderflux" : is_genderflux,
        "queer" : is_queer,
        "gnc" : is_gnc,
        "nb" : is_nb,
        "agender" : is_genderless,
        "neutral" : is_neutral,
        "bigender" : is_genderfull,
        "demi" : is_demi,

        "human" : is_human,
        "person" : is_person,

        "trans" : is_trans,
        "transfemme" : is_transfemme,
        "transmasc" : is_transmasc,
        "detrans" : is_detrans,
        "cis" : is_cis,
        "intersex" : is_intersex,
        "binary" : is_binary,

        "lesbian" : is_lesbian,
        "dyke" : is_dyke,
        "butch" : is_butch,
        "sapphic" :is_sapphic,
        "gay" : is_gay,
        "achillean" : is_achillean,
        "twink" : is_twink,
        "bear" : is_bear,
        "homo" : is_homosexual,
        "fag" : is_fag,
        "conflicted_queer_labels" : is_conflicting_queer,
        "dykefag" : is_dykefag,
        "lesbianism_for_men" : is_lesbianism_for_men,
        "faggotry_for_women" : is_faggotry_for_women,
        "bi_pan" : is_bi_pan,
        "ace_aro" : is_ace_aro,

        "she" : is_she,
        "he" : is_he,
        "they" : is_they,
    }

    if data_case in func_dict:
        return func_dict[data_case]

