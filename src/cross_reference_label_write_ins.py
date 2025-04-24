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
    'a_bi_fluid_flux_neu_gender' : [
        'agender_tickbox',
        'agender_user',
        'bigender_tickbox', 
        'bigender_user', 
        'genderfluid_tickbox', 
        'genderfluid_user',
        'genderflux_user', 
        'neutral_user', 
    ],
    "nb_umbrella" : [
        'enby_tickbox', 
        'nonbinary_tickbox',
        'nb_user', 
        'agender_tickbox',
        'agender_user',
        'bigender_tickbox', 
        'bigender_user', 
        'genderfluid_tickbox', 
        'genderfluid_user',
        'genderflux_user', 
        'neutral_user', 
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
    "mlm_labels" : [
        'achillean_user', 
        'bear_user', 
        'twink_user',
        'fag_tickbox', 
        'fag_user', 
    ],
    "wlw_labels" : [
        'dyke_user', 
        'lesbian_user',
        'sapphic_user', 
        'butch_tickbox',
        'butch_user', 
    ],
    "gay_homo_bi_pan" : [ # have male & female specific ones
        'gay_user', 
        'homo_user', 
        'bi_pan_user', 
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

[ # new unified columns
    "trans_unified",
    "transmasc_unified",
    "transfemme_unified",
    "cis_unified",
    "any_female_aligned_unified",
    "any_male_aligned_unified",
    "female_aligned_unified",
    "male_aligned_unified",
    "nb_unified",
    "agender_genderless_unified",
    "bigender_pangender_unified",
    "genderfluid_unified",
    "binary_unified",
    "person_human_unified",
    "butch_unified",
    "fag_unified",
    "gnc_unified",
    "genderqueer_unified",
    "queer_unified"
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

def mutually_exclusive(input_df:pd.DataFrame): #TODO

    new_df = input_df.copy()

    # make mutually exclusive categories
        # -> conflicted vs one vs the other vs neither
        # trans, cis
        # afab, amab
        # transmasc, transfemme (must pass above trans exclusive category too)
        # male aligned, female aligned (incl conflicted), -> add conflicted to both?
        # mlm, wlw, conflicted queer, fagdyke, etc categories
        # non-male, non-female

    ## alignments

    # any unconflicted female aligned (ie must contain non-conflicted, even if also conflicted_female_aligned)
    new_df["is_female_aligned"] = "Yes"
    new_df['is_female_aligned'] = new_df['is_female_aligned'].where(
        ( # must be female aligned
            new_df["female_aligned_unified"] == "Yes") & ( # can't only be conflicted aligned
            new_df["non_female_aligned_user"] != "Yes"
        ) & ( # must not be male aligned
            new_df["any_male_aligned_unified"] != "Yes") & (
            new_df["mlm_labels_unified"] != "Yes") & (
            new_df["transmasc_unified"] != "Yes") & (
            new_df["femboy_user"] != "Yes") & (
            new_df["he_user"] != "Yes"
        ) & ( # must not be both/neither/conflicted
            new_df["both_user"] != "Yes") & (
            new_df["neither_user"] != "Yes") & (
            new_df["dykefag_user"] != "Yes") & (
            new_df["faggotry_for_women_user"] != "Yes") & (
            new_df["lesbianism_for_men_user"] != "Yes") & (
            new_df["conflicted_queer_user"] != "Yes"
        )
    )
    # any unconflicted male aligned (ie must contain non-conflicted, even if also conflicted_male_aligned)
    new_df["is_male_aligned"] = "Yes"
    new_df['is_male_aligned'] = new_df['is_male_aligned'].where(
        ( # must be male aligned
            new_df["male_aligned_unified"] == "Yes") & ( # can't only be conflicted aligned
            new_df["non_male_aligned_user"] != "Yes"
        ) & ( # must not be female aligned
            new_df["any_female_aligned_unified"] != "Yes") & (
            new_df["wlw_labels_unified"] != "Yes") & (
            new_df["transfemme_unified"] != "Yes") & (
            new_df["she_user"] != "Yes"
        ) & ( # must not be both/neither/conflicted
            new_df["both_user"] != "Yes") & (
            new_df["neither_user"] != "Yes") & (
            new_df["dykefag_user"] != "Yes") & (
            new_df["faggotry_for_women_user"] != "Yes") & (
            new_df["lesbianism_for_men_user"] != "Yes") & (
            new_df["conflicted_queer_user"] != "Yes"
        )
    )

    # any conflicted female aligned (ie must only contain conflicted_female_aligned)
    new_df["is_conflicted_female_aligned"] = "Yes"
    new_df['is_conflicted_female_aligned'] = new_df['is_conflicted_female_aligned'].where(
        ( # must be female aligned
            new_df["conflicted_female_aligned_user"] == "Yes") & ( # must only be conflicted aligned
            new_df["non_female_aligned_user"] != "Yes"
        ) & ( # must not be male aligned
            new_df["any_male_aligned_unified"] != "Yes") & (
            new_df["mlm_labels_unified"] != "Yes") & (
            new_df["transmasc_unified"] != "Yes") & (
            new_df["femboy_user"] != "Yes") & (
            new_df["he_user"] != "Yes"
        ) & ( # must not be both/neither/conflicted
            new_df["both_user"] != "Yes") & (
            new_df["neither_user"] != "Yes") & (
            new_df["dykefag_user"] != "Yes") & (
            # new_df["faggotry_for_women_user"] != "Yes") & ( # this is technically female aligned right
            new_df["lesbianism_for_men_user"] != "Yes") & (
            new_df["conflicted_queer_user"] != "Yes"
        )
    )
    # any conflicted male aligned (ie must only contain conflicted_male_aligned)
    new_df["is_conflicted_male_aligned"] = "Yes"
    new_df['is_conflicted_male_aligned'] = new_df['is_conflicted_male_aligned'].where(
        ( # must be male aligned
            new_df["conflicted_male_aligned_user"] == "Yes") & ( # must only be conflicted aligned
            new_df["non_male_aligned_user"] != "Yes"
        ) & ( # must not be female aligned
            new_df["any_female_aligned_unified"] != "Yes") & (
            new_df["wlw_labels_unified"] != "Yes") & (
            new_df["transfemme_unified"] != "Yes") & (
            new_df["she_user"] != "Yes"
        ) & ( # must not be both/neither/conflicted
            new_df["both_user"] != "Yes") & (
            new_df["neither_user"] != "Yes") & (
            new_df["dykefag_user"] != "Yes") & (
            new_df["faggotry_for_women_user"] != "Yes") & (
            # new_df["lesbianism_for_men_user"] != "Yes") & ( # this is technically male aligned right
            new_df["conflicted_queer_user"] != "Yes"
        )
    )

    # any non-male aligned
    new_df["is_non_male_aligned"] = "Yes"
    new_df['is_non_male_aligned'] = new_df['is_non_male_aligned'].where(
        ( # must only be non-male (which includes explicitly female aligned folks)
            (new_df["non_male_aligned_user"] == "Yes") | (new_df["is_female_aligned"] == "Yes")
        ) & (
            new_df["non_female_aligned_user"] != "Yes"
        ) & ( # must not be male aligned
            new_df["any_male_aligned_unified"] != "Yes") & (
            new_df["mlm_labels_unified"] != "Yes") & (
            new_df["transmasc_unified"] != "Yes") & (
            new_df["femboy_user"] != "Yes") & (
            new_df["he_user"] != "Yes"
        ) & ( # must not be both/neither/conflicted
            new_df["both_user"] != "Yes") & (
            new_df["neither_user"] != "Yes") & (
            new_df["dykefag_user"] != "Yes") & (
            new_df["faggotry_for_women_user"] != "Yes") & (
            new_df["lesbianism_for_men_user"] != "Yes") & (
            new_df["conflicted_queer_user"] != "Yes"
        )
    )
    # any non-female aligned
    new_df["is_non_female_aligned"] = "Yes"
    new_df['is_non_female_aligned'] = new_df['is_non_female_aligned'].where(
        ( # must only be non-female (which includes explicitly male aligned folks)
            (new_df["non_female_aligned_user"] == "Yes") | (new_df["is_male_aligned"] == "Yes")
        ) & (
            new_df["non_male_aligned_user"] != "Yes"
        ) & ( # must not be female aligned
            new_df["any_female_aligned_unified"] != "Yes") & (
            new_df["wlw_labels_unified"] != "Yes") & (
            new_df["transfemme_unified"] != "Yes") & (
            new_df["she_user"] != "Yes"
        ) & ( # must not be both/neither/conflicted
            new_df["both_user"] != "Yes") & (
            new_df["neither_user"] != "Yes") & (
            new_df["dykefag_user"] != "Yes") & (
            new_df["faggotry_for_women_user"] != "Yes") & (
            new_df["lesbianism_for_men_user"] != "Yes") & (
            new_df["conflicted_queer_user"] != "Yes"
        )
    )

    # also not seeing the point of conflicted male/female/non_male/female for now

    # unspecified alignment
    new_df["unspecified_alignment"] = "Yes"
    new_df["unspecified_alignment"] = new_df["unspecified_alignment"].where(
        ( # must not be any of the previous categories
            new_df["is_female_aligned"] != "Yes") & (
            new_df["is_male_aligned"] != "Yes") & (
            new_df["is_conflicted_female_aligned"] != "Yes") & (
            new_df["is_conflicted_male_aligned"] != "Yes") & (
            new_df["is_non_male_aligned"] != "Yes") & (
            new_df["is_non_female_aligned"] != "Yes"
        )
    )

    # any less explicit alignments can be added later 
    # (and other statuses will need to be changed accordingly, ie unspecified etc)
    
    ## trans status

    new_df["is_trans"] = "Yes"
    new_df['is_trans'] = new_df['is_trans'].where(
        ( # must be trans
            (
                new_df["trans_unified"] == "Yes" # labelled as such
            ) | ( # or non-male amab or non-female afab if not labelled as trans
                (new_df["is_non_male_aligned"] == "Yes") & (
                    new_df["amab_user"] == "Yes") & (new_df["afab_user"] != "Yes"
                )
            ) | (
                (new_df["is_non_female_aligned"] == "Yes") & (
                    new_df["afab_user"] == "Yes") & (new_df["amab_user"] != "Yes"
                )
            )
        ) & ( # and not be cis
            new_df["cis_unified"] != "Yes"
        )
    )
    new_df["is_cis"] = "Yes"
    new_df['is_cis'] = new_df['is_cis'].where(
        (
            (
                new_df["cis_unified"] == "Yes"
            ) | ( # or male-aligned amab or female-aligned afab if not labelled as cis
                (new_df["is_male_aligned"] == "Yes") & (
                    new_df["amab_user"] == "Yes") & (new_df["afab_user"] != "Yes"
                )
            ) | (
                (new_df["is_female_aligned"] == "Yes") & (
                    new_df["afab_user"] == "Yes") & (new_df["amab_user"] != "Yes"
                )
            )
        ) & ( # and not be trans
            new_df["trans_unified"] != "Yes"
        )
    )

    # we ignored conflicted in gathering, so not bothering with it

    new_df["unspecified_trans_status"] = "Yes"
    new_df['unspecified_trans_status'] = new_df['unspecified_trans_status'].where(
        (new_df["is_cis"] != "Yes") & (new_df["is_trans"] != "Yes")
    )

    ## trans direction 

    new_df["is_transmasc"] = "Yes"
    new_df['is_transmasc'] = new_df['is_transmasc'].where(
        (
            new_df["is_trans"] == "Yes" # must be trans
        ) & ( # must be transmasc
            ( # ie transmasc labelled, afab, or non-female aligned
                new_df["transmasc_unified"] == "Yes") | (
                new_df["afab_user"] == "Yes") | (
                new_df["is_non_female_aligned"] == "Yes"
            )
        ) & ( # must not be transfemme, amab, or female aligned
            new_df["transfemme_unified"] != "Yes") & (
            new_df["amab_user"] != "Yes") & (
            new_df["any_female_aligned_unified"] != "Yes"
        )
    )
    new_df["is_transfemme"] = "Yes"
    new_df['is_transfemme'] = new_df['is_transfemme'].where(
        (
            new_df["is_trans"] == "Yes" # must be trans
        ) & ( # must be transfemme
            ( # ie transfemme labelled, amab, or non-male aligned
                new_df["transfemme_unified"] == "Yes") | (
                new_df["amab_user"] == "Yes") | (
                new_df["is_non_male_aligned"] == "Yes"
            )
        ) & ( # must not be transmasc, afab, or male aligned
            new_df["transmasc_unified"] != "Yes") & (
            new_df["afab_user"] != "Yes") & (
            new_df["any_male_aligned_unified"] != "Yes"
        )
    )

    # we ignored conflicted in gathering, so not bothering with it

    new_df["unspecified_trans_direction"] = "Yes"
    new_df['unspecified_trans_direction'] = new_df['unspecified_trans_direction'].where(
        (
            new_df["is_trans"] == "Yes") & ( # must be trans
            new_df["is_transfemme"] != "Yes") & (
            new_df["is_transmasc"] != "Yes"
        )
    )

    ## birthsex

    new_df["is_afab"] = "Yes"
    new_df['is_afab'] = new_df['is_afab'].where(
        ( # must be afab
            ( # excluding transmasc intersex folks unless they explicitly use afab
                (new_df["is_transmasc"] == "Yes") & (new_df["intersex_user"] != "Yes") 
            ) | (
                new_df["afab_user"] == "Yes"
            )
        ) & ( # must not be amab
            new_df["transfemme_unified"] != "Yes") & (
            new_df["amab_user"] != "Yes"
        )
    )
    new_df["is_amab"] = "Yes"
    new_df['is_amab'] = new_df['is_amab'].where(
        ( # must be amab
            ( # excluding transfemme intersex folks unless they explicitly use amab
                (new_df["is_transfemme"] == "Yes") & (new_df["intersex_user"] != "Yes") 
            ) | (
                new_df["amab_user"] == "Yes"
            )
        ) & ( # must not be afab
            new_df["transmasc_unified"] != "Yes") & (
            new_df["afab_user"] != "Yes"
        )
    )

    ## wlw/mlm
    # (we're including words like twink & butch that aren't actually sexuality related respectively 
    # but originate from those communities)
    
    new_df["is_wlw_aligned"] = "Yes"
    new_df['is_wlw_aligned'] = new_df['is_wlw_aligned'].where(
        ( # must have wlw label
            (new_df["wlw_labels_unified"] == "Yes") | ( # explicitly wlw labels or female-aligned gays
                (new_df["gay_homo_bi_pan_unified"] == "Yes") & (new_df["is_female_aligned"] == "Yes")
            )
        ) & ( # must not have mlm label or non-female or conflicted alignment
            new_df["mlm_labels_unified"] != "Yes") & ( 
            new_df["any_male_aligned_unified"] != "Yes") & (
            new_df["is_non_female_aligned"] != "Yes") & (
            new_df["is_transmasc"] != "Yes") & (
            new_df["lesbianism_for_men_user"] != "Yes") & ( # no male lesbians
            new_df["faggotry_for_women_user"] != "Yes" # is a mlm label conflict
        ) & ( # no nb lesbians unless explicitly female aligned
            (new_df["is_female_aligned"] == "Yes") | (new_df["nb_umbrella_unified"] != "Yes")
        )
    )
    new_df["is_mlm_aligned"] = "Yes"
    new_df['is_mlm_aligned'] = new_df['is_mlm_aligned'].where(
        ( # must have mlm label
            (new_df["mlm_labels_unified"] == "Yes") | ( # explicitly mlm labels or male-aligned gays
                (new_df["gay_homo_bi_pan_unified"] == "Yes") & (new_df["is_male_aligned"] == "Yes")
            )
        ) & ( # must not have wlw label or non-male or conflicted alignment
            new_df["wlw_labels_unified"] != "Yes") & (
            new_df["any_female_aligned_unified"] != "Yes") & (
            new_df["is_non_male_aligned"] != "Yes") & (
            new_df["is_transfemme"] != "Yes") & (
            new_df["lesbianism_for_men_user"] != "Yes") & ( # is a wlw label conflict
            new_df["faggotry_for_women_user"] != "Yes" # no female faggots
        ) & ( # no nb gays unless explicitly male aligned
            (new_df["is_male_aligned"] == "Yes") | (new_df["nb_umbrella_unified"] != "Yes")
        )
    )
    # TODO conflicted & unspecified?

    # TODO 
    # - anything else?
    # - test run?

    new_df = new_df.fillna("No")

    return new_df

def cross_reference(input_df:pd.DataFrame): #TODO

    # cross reference (after mutually exclusive categories) -> if it's not categorised this way yet
        # trans, female aligned; trans, amab; female aligned, amab -> transfemme
        # trans, male aligned; trans, afab; male aligned, afab -> transmasc
        # female aligned, afab; cis, afab; cis, female aligned -> cis female aligned
        # male aligned, amab; cis, amab; cis, male aligned -> cis male aligned
        # female aligned, gay/bi -> wlw
        # male aligned, gay/bi -> mlm

        # nb, not female aligned, wlw -> nb lesbian
        # nb, not male aligned, mlm -> nb gay
        # male aligned, wlw -> lesbianism for men
        # female aligned, mlm -> faggotry for women

        # non-male; female-aligned -> non-man
        # non-female; male_aligned -> non-woman
        # no alignment, any nb label -> unaligned nb
        # intersex, male-aligned -> intersex male-aligned
        # intersex, female-aligned -> intersex female-aligned
        # intersex, unaligned nb -> intersex unaligned
        # femboy, any form of transfemme -> transfemme femboy
        # femboy, any form of transmasc -> transmasc femboy
        # femboy, unspecified trans -> unspecified trans femboy
        # femboy, any form of not trans -> non-trans femboy

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

    mutually_exclusive_1 = mutually_exclusive(unified_df)
    
    # cross refence

    mutually_exclusive_1.to_csv(path_or_buf="data/cleaned_q2_with_new_columns/q2_cross_referenced_01.csv")




