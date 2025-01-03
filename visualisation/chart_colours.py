pronoun_colours = {
    "she_user":"deeppink",
    "he_user":"royalblue",
    "they_user":"purple",
    "it_user":"green",
    "neopronoun_user":"yellow",
    "any_user":"black",

    "questioning":"silver",
    "avoid_pronouns/name_as_pronoun":"grey",

    "questioning_only":"silver",
    "avoid_pronouns/use_name_only":"grey",

    "she_only":"deeppink",
    "he_only":"royalblue",
    "they_only":"purple",
    "it_only":"green",
    "neopronoun_only":"yellow",

    "she/they":"mediumvioletred",
    "he/they":"slateblue",
    "she/he":"violet",
    "she/he/they_any":"black",

    "she/it":"olive",
    "he/it":"lightseagreen ",
    "they/it":"saddlebrown",
    
    "she/[neo]":"orange",
    "he/[neo]":"limegreen",
    "they/[neo]":"chocolate",

    "she/it/[neo]":"tan",
    "he/it/[neo]":"darkseagreen",
    "they/it/[neo]":"darkgoldenrod",
    "it/[neo]":"greenyellow",
}

alignment_colours = {
    "female_aligned":"mediumvioletred",
    "male_aligned":"slateblue",
    "unaligned":"purple",
}

# for reference of what they ended up being called
tickbox_labels = [
    "a person/human/[my name]/just me_tickbox",
    "agender_tickbox",
    "bigender_tickbox",
    "binary_tickbox",
    "butch_tickbox",
    "cisgender_tickbox",
    "demiboy_tickbox",
    "demigirl_tickbox",
    "enby_tickbox",
    "fag_tickbox",
    "gender non-conforming_tickbox",
    "genderfluid_tickbox",
    "genderqueer_tickbox",
    "nonbinary_tickbox",
    "queer_tickbox",
    "questioning/unknown_tickbox",
    "trans_tickbox",
    "transfeminine_tickbox",
    "transgender_tickbox",
    "transmasculine_tickbox",
    "no self-description_tickbox",
]
other_tickbox_labels = {
    "cis_trans" : [
        "is_trans_tickbox",
        "is_cis_tickbox",
        "conflicted_cis/trans_tickbox",
        "unspecified_cis/trans_tickbox",
    ],
    "demiboy_demigirl": {
        "is_only_demigirl_tickbox":"mediumvioletred",
        "is_only_demiboy_tickbox":"slateblue",
        "conflicted_demigirl/demiboy_tickbox":"violet",
    },
    "transmasc_transfem": [
        "is_transmasc_tickbox",
        "is_transfemme_tickbox",
        "conflicted_transmasc/transfem_tickbox",
        "unspecified_transmasc/transfem_tickbox",
    ],
    "butch_fag": [
        "is_only_butch_tickbox",
        "is_only_fag_tickbox",
        "conflicted_fag/butch_tickbox",
    ],
    "nb": [
        "is_nb_tickbox",
        "is_nb_umbrella_tickbox",
    ],
    "birthsexes": [
        "is_afab_tickbox",
        "is_amab_tickbox",
    ],
    
    # idk if I'll keep the binary nb ones bc barely anyone ticked it
    # but then make nb labels binary exclusive or leave as is?
    "binary_nb": [
        "is_binary_nb_tickbox",
        "is_binary_nb_umbrella_tickbox",
    ]

}