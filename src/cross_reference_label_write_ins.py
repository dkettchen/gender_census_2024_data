import pandas as pd
from utils.csv_reader import df_from_csv

redundancies = {
    "trans" : [
        'trans_tickbox',
        'transfeminine_tickbox', 
        'transgender_tickbox',
        'transmasculine_tickbox', 
        'trans_user',
        'transfemme_user', 
        'transmasc_user',
    ],
    "transmasc" : [
        'transmasculine_tickbox', 
        'transmasc_user',
        # male aligned + trans
        # afab + trans
    ],
    "transfemme" : [
        'transfeminine_tickbox', 
        'transfemme_user', 
        # female aligned + trans
        # amab + trans
    ],
    "cis" : [
        'cisgender_tickbox', 
        'cis_user', 
    ],
    "any_female_aligned" : [
        'demigirl_tickbox',
        'conflicted_female_aligned_user',
        'female_aligned_user', 
    ],
    "any_male_aligned" : [
        'demiboy_tickbox', 
        'conflicted_male_aligned_user', 
        'male_aligned_user',
    ],
    "female_aligned" : [
        'demigirl_tickbox',
        'female_aligned_user', 
    ],
    "male_aligned" : [
        'demiboy_tickbox', 
        'male_aligned_user',
    ],
    "nb" : [
        'enby_tickbox', 
        'nonbinary_tickbox',
        'nb_user', 
    ],
    "agender_genderless" : [
        'agender_tickbox',
        'agender_user',
    ],
    "bigender_pangender" : [
        'bigender_tickbox', 
        'bigender_user', 
    ],
    "genderfluid" : [
        'genderfluid_tickbox', 
        'genderfluid_user',
    ],
    "binary" : [
        'binary_tickbox', 
        "binary_user",
    ],
    "person_human" : [
        'a person/human/[my name]/just me_tickbox', 
        'human_user', 
        'person_user', 
    ],
    "butch" : [
        'butch_tickbox',
        'butch_user', 
    ],
    "fag" : [ # excluding conflicted ones like fagdyke
        'fag_tickbox', 
        'fag_user', 
    ],
    "gnc" : [
        'gender non-conforming_tickbox',
        'gnc_user', 
    ],
    "genderqueer" : [
        'genderqueer_tickbox', 
        'genderqueer_user', 
    ],
    "queer" : [
        'queer_tickbox', 
        'queer_user',
    ],
}
og_labels = [
    { # tickbox base labels
        'a person/human/[my name]/just me_tickbox', # ✅
        'agender_tickbox', # ✅
        'bigender_tickbox', # ✅
        'binary_tickbox', # ✅
        'butch_tickbox', # ✅
        'cisgender_tickbox', # ✅
        'demiboy_tickbox', # ✅
        'demigirl_tickbox', # ✅
        'enby_tickbox', # ✅
        'fag_tickbox', # ✅
        'gender non-conforming_tickbox', # ✅
        'genderfluid_tickbox', # ✅
        'genderqueer_tickbox', # ✅
        'nonbinary_tickbox', # ✅
        'queer_tickbox', # ✅
        'questioning/unknown_tickbox', 
        'trans_tickbox', # ✅
        'transfeminine_tickbox', # ✅
        'transgender_tickbox', # ✅
        'transmasculine_tickbox', # ✅
        'no self-description_tickbox',
    },
    { # tickbox extra columns
        'is_trans_tickbox', 
        'is_cis_tickbox', 
        'conflicted_cis/trans_tickbox',
        'unspecified_cis/trans_tickbox', 
        'is_only_demigirl_tickbox',
        'is_only_demiboy_tickbox', 
        'conflicted_demigirl/demiboy_tickbox',
        'is_transmasc_tickbox', 
        'is_transfemme_tickbox',
        'conflicted_transmasc/transfem_tickbox',
        'unspecified_transmasc/transfem_tickbox', 
        'is_only_butch_tickbox',
        'is_only_fag_tickbox', 
        'conflicted_fag/butch_tickbox', 
        'is_nb_tickbox',
        'is_a_bi_fluid_gender_tickbox', 
        'is_nb_umbrella_tickbox',
        'is_binary_nb_tickbox', 
        'is_binary_nb_umbrella_tickbox',
        'is_afab_tickbox', 
        'is_amab_tickbox', 
        'total_tickboxes',
        'total_non_synonymous_tickboxes', 
        'total_nb_umbrella_tickboxes'
    },
    { # write in columns
        'all_write_ins', 
        'no_of_write_ins', 
        'wrote_in', 
        'useable_write_ins',

        'ace_aro_user', 
        'achillean_user', 
        'afab_user', 
        'agender_user', # ✅
        'amab_user', 
        'androgyne_user', 
        'androgynous_user', 
        'autistic_user',
        'bear_user', 
        'bi_pan_user', 
        'bigender_user', # ✅
        'binary_user', # ✅
        'both_user',
        'butch_user', # ✅
        'cis_user', # ✅
        'conflicted_female_aligned_user', # ✅
        'conflicted_male_aligned_user', # ✅
        'conflicted_queer_user',
        'crossdresser_user', 
        'demi_user', 
        'detrans_user', 
        'drag_user',
        'dyke_user', 
        'dykefag_user', 
        'fag_user', # ✅
        'faggotry_for_women_user',
        'female_aligned_user', # ✅
        'female_present_passing_user', 
        'femboy_user',
        'femme_user', 
        'futch_user', 
        'gay_user', 
        'genderfluid_user', # ✅
        'genderflux_user', 
        'genderqueer_user', # ✅
        'gnc_user', # ✅
        'he_user',
        'homo_user', 
        'human_user', # ✅
        'intersex_user', 
        'lesbian_user',
        'lesbianism_for_men_user', 
        'male_aligned_user', # ✅
        'male_present_passing_user', 
        'masc_user', 
        'nb_user', # ✅
        'neither_user',
        'neutral_user', 
        'non_female_aligned_user', 
        'non_male_aligned_user',
        'other_neurodivergent_user', 
        'person_user', # ✅
        'plural_user', 
        'queer_user', # ✅
        'sapphic_user', 
        'she_user', 
        'sissy_user', 
        'they_user', 
        'trans_user', # ✅
        'transfemme_user', # ✅
        'transmasc_user', # ✅
        'trap_user', 
        'twink_user'

    },
]

non_redundant_og_columns = [ # get columns we're not replacing
        'total_tickboxes',
        'total_non_synonymous_tickboxes', 
        'total_nb_umbrella_tickboxes',

        'questioning/unknown_tickbox', 
        'no self-description_tickbox',

        'all_write_ins', 
        'no_of_write_ins', 
        'wrote_in', 
        'useable_write_ins',

        'ace_aro_user', 
        'achillean_user', 
        'afab_user', 
        'amab_user', 
        'androgyne_user', 
        'androgynous_user', 
        'autistic_user',
        'bear_user', 
        'bi_pan_user', 
        'both_user',
        'conflicted_queer_user',
        'crossdresser_user', 
        'demi_user', 
        'detrans_user', 
        'drag_user',
        'dyke_user', 
        'dykefag_user', 
        'faggotry_for_women_user',
        'female_present_passing_user', 
        'femboy_user',
        'femme_user', 
        'futch_user', 
        'gay_user', 
        'genderflux_user', 
        'he_user',
        'homo_user', 
        'intersex_user', 
        'lesbian_user',
        'lesbianism_for_men_user', 
        'male_present_passing_user', 
        'masc_user', 
        'neither_user',
        'neutral_user', 
        'non_female_aligned_user', 
        'non_male_aligned_user',
        'other_neurodivergent_user', 
        'plural_user', 
        'sapphic_user', 
        'she_user', 
        'sissy_user', 
        'they_user', 
        'trap_user', 
        'twink_user',

        'conflicted_female_aligned_user', # ✅
        'conflicted_male_aligned_user', # ✅
    ]

def unify_redundancies(input_df:pd.DataFrame):
    """
    takes a df with write in columns and joined on tickbox columns

    unifies all redundant columns into one new combined column
    (ex trans, transmasc, transfemme, etc into one unified trans column)

    returns a new df with all the non-redundant columns from the input and the new unified columns,
    suffixed with "_unified"
    """

    new_df = input_df.copy().get(non_redundant_og_columns)

    # combine repeated tickbock labels
    for key in redundancies: # multi-column categories
        new_column_name = key + "_unified"

        # add new column for key
        new_df[new_column_name] = "No"

        # for each column in key's list
        for column in redundancies[key]:

            # for each row
            for row in new_df.index:
                # if column is Yes in row
                if input_df.loc[row, column] == "Yes":
                    # we change new column to Yes
                    new_df.loc[row, new_column_name] = "Yes"

    return new_df

def remove_column_endings(input_df:pd.DataFrame):
    """
    removes the "_user", "_unified", and "_tickbox" labels from column names

    returns a new df with renamed columns
    """

    new_df = input_df.copy()

    renaming_dict = {}
    for column in new_df.columns:
        if column[-5:] == "_user":
            removal = -5
        elif column[-8:] in ["_unified", "_tickbox"]:
            removal = -8
        else:
            removal = None
        if removal:
            renaming_dict[column] = column[:removal]

    new_df = new_df.rename(columns=renaming_dict)

    return new_df

def cross_reference(input_df:pd.DataFrame): #TODO

    # cross reference categories (conflicting responses, combo responses (ex "trans" + "woman"), etc)
        # make columns of mutually exclusive categories
    
    # Q. do we cross reference tickbox labels here (= would need to join) or later?
        # -> make a third file combining write ins with tickbox labels 
        # to update tickbox categories in there?

        # but write ins themselves may not contain conflicts with tickbox labels, 
        # so we should join it for making mutually exclusive categories properly

    pass

if __name__ == "__main__":
    # read in tickbox & write in data
    read_tickbox_data = df_from_csv("data/cleaned_q1_with_new_columns/q1_clean_01.csv").set_index("UserID")
    read_write_ins_data = df_from_csv("data/cleaned_q2_with_new_columns/q2_clean_01.csv").set_index("UserID")

    # join em
    write_ins_with_tickboxes = read_write_ins_data.join(read_tickbox_data)

    # # run all
    # unified_df = unify_redundancies(write_ins_with_tickboxes)

    # run part
    unified_df = unify_redundancies(write_ins_with_tickboxes.head(100))

    unified_df.to_csv(path_or_buf="data/cleaned_q2_with_new_columns/q2_unified_columns_01.csv")

    # unified_df.to_csv(path_or_buf="data/cleaned_q2_with_new_columns/q2_cross_referenced_01.csv")



