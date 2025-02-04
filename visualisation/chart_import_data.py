# titles for bar charts based on data cases
bar_titles = {
    "total_users":"Total % of respondants who use this pronoun set ",
    "only_one_set":"% of respondants who use only this pronoun set ",
    "big_three_combos":"% of respondants who use a combo of she, he, and they (order insensitive) <br>",
    "it_and_neo_combos":"% of respondants who use she, he, or they w/ it or neopronouns (order insensitive) <br>",
    "tickbox_label_total":"% of respondants who ticked this label ",
    "tickbox_nb_labels":"% of respondants who ticked nonbinary umbrella labels ",
    "tickbox_non_trans":"Most popular tickbox labels of non-trans respondants ",
    "tickbox_non_nb":"Most popular tickbox labels of respondants who don't use nonbinary umbrella labels <br>",
    "tickbox_non_nb_trans":"Most popular tickbox labels of respondants who use neither trans nor nonbinary labels <br>"
}

# titles for pie charts based on data cases
pie_titles = {
    "pronoun_pie":"Pronoun sets used by respondants (order insensitive) ",
    "aligned_pronoun_pie":"% of respondants using aligned/unaligned pronoun sets ",
    "tickbox_trans_cis_labels":"% of respondants who did/did not indicate cis or trans status via tickboxes <br>",
    "tickbox_trans_direction_labels":"% of trans respondants who did/did not specify their direction via tickboxes <br>",
    "tickbox_nb_no_nb":"% of respondants who did/did not tick nonbinary/enby ",
    "tickbox_nb_no_nb_umbrella":"% of respondants who did/did not tick nonbinary, enby, genderfluid, agender, <br>or bigender ",
    "tickbox_trans_nb": "% of respondants who did/did not tick trans and/or nonbinary labels <br>"
}

# get lists for count df based on data cases
case_get_lists = {
    #"case" : ["get", "list"],
    "total_users":[
        "she_user",
        "he_user",
        "they_user",
        "it_user",
        "neopronoun_user",
        "any_user",

        "questioning",
        "avoid_pronouns/name_as_pronoun",
    ],
    "only_one_set":[
        "she_only",
        "he_only",
        "they_only",
        "it_only",
        "neopronoun_only",
        "avoid_pronouns/use_name_only",
        "questioning_only",
    ],
    "big_three_combos":[
        "he/they",
        "she/they",
        "she/he",
        "she/he/they_any"
    ],
    "it_and_neo_combos":[
        "he/it",
        "she/it",
        "they/it",
        "he/[neo]",
        "she/[neo]",
        "they/[neo]",
        "she/it/[neo]",
        "he/it/[neo]",
        "they/it/[neo]",
        "it/[neo]",
    ],
    "pronoun_pie":[ # also "aligned_pronoun_pie", this one is just combo of only, big three, & it/neo above
        "she_only",
        "he_only",
        "they_only",
        "it_only",
        "neopronoun_only",
        "he/they",
        "she/they",
        "she/he",
        "she/he/they_any",
        "he/it",
        "she/it",
        "they/it",
        "he/[neo]",
        "she/[neo]",
        "they/[neo]",
        "she/it/[neo]",
        "he/it/[neo]",
        "they/it/[neo]",
        "it/[neo]",
        "avoid_pronouns/use_name_only",
        "questioning_only",
    ],

    "tickbox_label_total":[
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
    ],
    "tickbox_nb_labels":[
        "agender_tickbox",
        "bigender_tickbox",
        "enby_tickbox",
        "genderfluid_tickbox",
        "nonbinary_tickbox",
        "is_nb_tickbox",
        "is_nb_umbrella_tickbox",
    ],
    "tickbox_trans_cis_labels":[
        "is_trans_tickbox",
        "is_cis_tickbox",
        "conflicted_cis/trans_tickbox",
        "unspecified_cis/trans_tickbox",
    ],
    "tickbox_trans_direction_labels":[
        "is_transmasc_tickbox",
        "is_transfemme_tickbox",
        "conflicted_transmasc/transfem_tickbox",
        "unspecified_transmasc/transfem_tickbox",
    ],
    "tickbox_nb_no_nb":[
        "is_nb_tickbox"
    ],
    "tickbox_nb_no_nb_umbrella":[
        "is_nb_umbrella_tickbox"
    ],
    "tickbox_non_trans":[ # everything other than trans labels we've excluded already + nb_umbrella total
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
        "no self-description_tickbox",

        "is_nb_umbrella_tickbox",
    ],
    "tickbox_non_nb":[ # everything other than nb umbrella labels we've excluded already
        "a person/human/[my name]/just me_tickbox",
        "binary_tickbox",
        "butch_tickbox",
        "cisgender_tickbox",
        "demiboy_tickbox",
        "demigirl_tickbox",
        "fag_tickbox",
        "gender non-conforming_tickbox",
        "genderqueer_tickbox",
        "queer_tickbox",
        "questioning/unknown_tickbox",
        "trans_tickbox",
        "transfeminine_tickbox",
        "transgender_tickbox",
        "transmasculine_tickbox",
        "no self-description_tickbox",

        "is_trans_tickbox",
    ],
    "tickbox_non_nb_trans":[ # everything other than nb umbrella labels we've excluded already
        "a person/human/[my name]/just me_tickbox",
        "binary_tickbox",
        "butch_tickbox",
        "cisgender_tickbox",
        "demiboy_tickbox",
        "demigirl_tickbox",
        "fag_tickbox",
        "gender non-conforming_tickbox",
        "genderqueer_tickbox",
        "queer_tickbox",
        "questioning/unknown_tickbox",
        "no self-description_tickbox",
    ],
    "tickbox_trans_nb": ["only_trans", "only_nb", "trans_and_nb", "neither_trans_nor_nb"]

}


# pronoun data cases
pronoun_cases = [
    "total_users",
    "only_one_set",
    "big_three_combos",
    "it_and_neo_combos",
    "pronoun_pie",
]
# alignment colours for alignment cases!
alignment_cases = [
    "aligned_pronoun_pie", # exception for pronouns bc alignment colours
]
# tickbox label data cases
tickbox_label_cases = [
    "tickbox_label_total",
    "tickbox_nb_labels",
    "tickbox_trans_cis_labels",
    "tickbox_trans_direction_labels",
    "tickbox_nb_no_nb",
    "tickbox_nb_no_nb_umbrella",
    "tickbox_non_trans",
    "tickbox_non_nb",
    "tickbox_non_nb_trans",
]