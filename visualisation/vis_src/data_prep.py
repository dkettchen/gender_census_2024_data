import pandas as pd
from visualisation.vis_utils.get_pronoun_alignment import get_pronoun_alignment
from visualisation.vis_utils.count import count
from visualisation.vis_utils.import_data import case_get_lists
from visualisation.vis_utils.geo_utils import english_speaking, other_countries
from visualisation.vis_utils.make_percent import percent
from visualisation.vis_utils.make_subset import subset
from re import sub

def prep_pronoun_data(input_df:pd.DataFrame):
    """
    takes a df with data from question 9 (pronouns)

    returns a dict with descriptive keys and Series values containing the relevant data

    pronoun data includes:
    - "% of respondants who use this pronoun"
    - "Pronoun sets used by respondants (%)"
    - "% of respondants who only use one pronoun"
    - "% of respondants who use a combination of the big three"
    - "% of respondants whose multi-pronoun set includes it and/or neo pronouns"
    - "Alignment of pronoun sets used by respondants (%)"
    """
    
    pronoun_df = input_df.copy()

    data = {}

    # total users per pronoun as per original data (incl any users)
    data["% of respondants who use this pronoun"] = count(pronoun_df, "total_pronoun_users")

    # all combination categories
    all_combos = count(pronoun_df, "all_pronoun_combos")
    data["Pronoun sets used by respondants (%)"] = all_combos

    # sub sets of all pronoun combos
    # only one set/type users
    data["% of respondants who only use one pronoun"] = all_combos.where(
        all_combos.index.str.contains("_only")
    ).dropna(how="all") # count_df(pronoun_df, "only_one_set")
    # big three combos (she/they, he/they, she/he, she/he/they)
    data["% of respondants who use a combination of the big three"] = all_combos.where(
        ~all_combos.index.str.contains(
            "_only"
        ) & ~all_combos.index.str.contains(
            "it"
        ) & ~all_combos.index.str.contains(
            "neo"
        )
    ).dropna(how="all") # count_df(pronoun_df, "big_three_combos")
    # combos with it and neo pronouns
    data["% of respondants whose multi-pronoun set includes it and/or neo pronouns"] = all_combos.where(
        ~all_combos.index.str.contains(
            "_only"
        ) & (all_combos.index.str.contains(
            "it"
        ) | all_combos.index.str.contains(
            "neo"
        ))
    ).dropna(how="all") # count_df(pronoun_df, "it_and_neo_combos")

    # by alignment
    data["Alignment of pronoun sets used by respondants (%)"] = get_pronoun_alignment(all_combos)
    # count_df(pronoun_df, "aligned_pronoun_pie")

    return data

def prep_label_tickbox_data(input_df:pd.DataFrame):
    """
    takes a df with data from question 1 (tickbox labels)

    returns a dict with descriptive keys and Series values containing the relevant data

    tickbox label data includes:
    - "% of respondants who ticked this label"
    - "% of respondants who use nb umbrella labels"
    - "Trans status (%)"
    - "Transition direction of trans respondants (%)"
    - "Nb umbrella label use (%)"
    - "Top labels (used by > 1/5) of {
        trans|nb|non-trans|non-nb|trans-nb|neither trans nor nb
    } respondants ({x}% of total) (%)"
    - "Trans and nb intersection (%)"
    """

    tickbox_df = input_df.copy()

    # prep subset dfs
    trans_df = subset(tickbox_df,"is_trans_tickbox").dropna(how="all")
    nb_df = subset(tickbox_df,"is_nb_umbrella_tickbox").dropna(how="all")

    data = {}

    # total users per tickbox label (as is)
    data["% of respondants who ticked this label"] = count(tickbox_df, "tickbox_label_total")

    # nb label users vs total nb umbrella label users
    # nb labels vs other nb umbrella labels (comparison in each label's numbers)
    data["% of respondants who use nb umbrella labels"] = count(tickbox_df, "tickbox_nb_labels")

    # trans, cis, conflicted, unspecified
    data["Trans status (%)"] = count(tickbox_df, "tickbox_trans_cis_labels")

    # transmasc, transfemme, unspecified trans
    data["Transition direction of trans respondants (%)"] = count(trans_df, "tickbox_trans_direction_labels")

    # what labels nb users use
    for category in case_get_lists["tickbox_nb_and_umbrella"]:
        nb_df[category] = "Yes"
    nb_df["uses_both"] = nb_df["uses_both"].where( # nb yes, nb umb yes
        (nb_df["is_nb_tickbox"] == "Yes") & (nb_df["is_a_bi_fluid_gender_tickbox"] == "Yes")
    )
    nb_df["only_uses_nb"] = nb_df["only_uses_nb"].where( # nb yes, nb umb no
        (nb_df["is_nb_tickbox"] == "Yes") & (nb_df["is_a_bi_fluid_gender_tickbox"] != "Yes")
    )
    nb_df["only_uses_agender/bigender/genderfluid"] = nb_df["only_uses_agender/bigender/genderfluid"].where( # nb no, nb umb yes
        (nb_df["is_nb_tickbox"] != "Yes") & (nb_df["is_a_bi_fluid_gender_tickbox"] == "Yes")
    )
    data["Nb umbrella label use (%)"] = count(nb_df, "tickbox_nb_and_umbrella")

    # prep for later
    trans_and_nb = pd.Series(index=["trans_only", "nb_only", "trans_and_nb", "neither_trans_nor_nb"])

    # most popular labels for relevant sub-sets of respondants
    for c in ["trans", "non-trans", "nb_umbrella", "non-nb_umbrella", "trans-nb", "neither trans nor nb"]: 
        # prep subsets
        if "trans" in c and "nb" in c:
            if "neither" in c:
                df = tickbox_df.where(
                    (tickbox_df["is_trans_tickbox"] != "Yes") & (
                    tickbox_df["is_nb_umbrella_tickbox"] != "Yes")
                ).dropna(how="all")
                # add this as well while we have the df
                trans_and_nb["neither_trans_nor_nb"] = round((len(df) / len(tickbox_df)) * 100, 2)
            else:
                df = subset(trans_df,"is_nb_umbrella_tickbox").dropna(how="all")
                # add this as well while we have the df
                trans_and_nb["trans_and_nb"] = round((len(df) / len(tickbox_df)) * 100, 2)
        elif "non-" in c:
            df = subset(tickbox_df,f"is_{c[4:]}_tickbox",False).dropna(how="all")
        elif c == "trans":
            df = trans_df
        elif c == "nb_umbrella":
            df = nb_df

        # remove _umbrella bit so we can reuse it for labels
        if "nb_umbrella" in c: c = c[:-9]

        # count total labels for this subset
        srs = count(df, "tickbox_label_total")

        # only include labels used by over 1/5 of subset
        srs = srs.where(srs > 20).dropna(how="all")

        # calculate percent of total respondants this subset makes up
        total_percent = round((len(df) / len(tickbox_df)) * 100, 2)

        # add to data dict
        data[f"Top labels (used by > 1/5) of {c} respondants ({total_percent}% of total) (%)"] = srs

    # add other values
    trans_and_nb["trans_only"] = percent(
        len(subset(trans_df,"is_nb_umbrella_tickbox",False).dropna(how="all")),
        len(tickbox_df)
    )
    trans_and_nb["nb_only"] = percent(
        len(subset(nb_df,"is_trans_tickbox",False).dropna(how="all")),
        len(tickbox_df)
    )

    # how many respondants are trans/not nb, nb/not trans, trans+nb, neither (with umbrella)
    data["Trans and nb intersection (%)"] = trans_and_nb.sort_values(ascending=False)

    return data

def prep_pronouns_by_labels(label_df:pd.DataFrame, pronoun_df:pd.DataFrame):
    """
    takes dfs with data from question 1 (tickbox labels) and question 9 (pronouns)

    returns a dict with descriptive keys and Series values containing the relevant data

    it checks for the following label categories:
    - cis
    - transmasc
    - transfemme
    - unspecified trans/cis status
    - trans but unspecified direction

    the returned data includes
    - pronoun sets used by respondants of the relevant category (%)
    - the alignment of those pronoun sets (%)
    """

    # join dfs
    pronouns_x_labels = pronoun_df.join(label_df, lsuffix="left", rsuffix="right")

    # prep df with label categories

    # groups we want:
    categories = {
        # trans directions
        "is_transmasc_tickbox": "transmasc",
        "is_transfemme_tickbox": "transfemme",
        # unspecified trans direction
        "conflicted_transmasc/transfem_tickbox": "unspecified_trans",
        "unspecified_transmasc/transfem_tickbox": "unspecified_trans",
        # cis
        "is_cis_tickbox": "cis",
        # unspecified trans/cis status
        "conflicted_cis/trans_tickbox": "unspecified_cis_trans",
        "unspecified_cis/trans_tickbox": "unspecified_cis_trans",
    }

    # make a column of groups we want
    pronouns_x_labels["trans_status"] = None
    for column_name in categories:
        pronouns_x_labels["trans_status"] = pronouns_x_labels["trans_status"].mask(
            pronouns_x_labels[column_name] == "Yes", # check column in question
            other=categories[column_name] # mark with category label
        )

    data = {}
    
    # count pronoun sets per each category
    get_list = ["trans_status"] + case_get_lists["all_pronoun_combos"]
    pronoun_sets = pronouns_x_labels.get(get_list).groupby(by="trans_status").count().transpose()

    # separate, process & save them to our data dict with descriptive labels
    for column in pronoun_sets.columns:
        if "_" in column:
            label = ""
            suffix = " of unspecified"
            if "cis" in column:
                suffix += " trans/cis status"
            else:
                label += " trans"
                suffix += " direction"
        else:
            label = " " + column
            suffix = ""
        
        # get total number of this category
        total_respondants = pronoun_sets[column].sum()
        # get their pronoun sets
        label_sets = pronoun_sets[column].sort_values(ascending=False).apply(
            percent, args=[total_respondants]
        )
        # pronoun sets
        data[f"Pronoun sets used by{label} respondants{suffix}"] = label_sets
        # pronoun alignments
        data[f"Pronoun alignments of{label} respondants{suffix}"] = get_pronoun_alignment(label_sets)

    return data

def prep_geo_data(input_df:pd.DataFrame):
    """
    takes a df with data from question 35 (location)

    returns a dict with descriptive keys and Series values containing the relevant data

    location data includes (in %):
    - "Location of respondants (total)"
    - "Location of respondants (english-speaking)"
    """

    geo_df = input_df.copy().set_index("UserID")

    total_geo_srs = geo_df["q35_Location"] # countries column
    english_geo_srs = english_speaking(geo_df)["english_or_no"]

    total_respondants = len(geo_df)
    data = {}

    for data_case in ["total", "english-speaking"]:
        if data_case == "total":
            srs = total_geo_srs
        else:
            srs = english_geo_srs
        
        srs = srs.dropna(how="all")
        
        # fixing list values back to strings smh
        for i in range(len(srs)):
            item = srs.iloc[i]
            if type(item) != str:
                srs.iloc[i] = str(item)

        country_srs = srs.groupby(by=srs.values).count().sort_values(ascending=False)
        country_srs = country_srs.apply(percent, args=[total_respondants])

        if data_case == "total": # adding "other countries" for any countries under 0.5%
            country_srs = other_countries(country_srs, total_respondants)

        data[f"Location of respondants ({data_case})"] = country_srs

    return data

def prep_survey_origin(input_df:pd.DataFrame):
    """
    takes a df with data from question 37 (survey origin) rejoined to timestamps for sorting

    returns a dict with descriptive keys and Series values containing the relevant data

    survey origin data includes:
    - "Where respondants found the survey (%)"
    """

    origin_df = input_df.copy()

    srs = origin_df.groupby("origin").count()["timestamp_for_sorting"]
    srs = srs.sort_values(ascending=False)
    srs = srs.apply(percent, args=[len(origin_df)])
    srs = srs.where(srs > 1).dropna(how="all")

    data = {}
    data["Where respondants found the survey (%)"] = srs

    return data

def prep_write_in_data(input_df:pd.DataFrame):
    write_ins_df = input_df.copy()

    print("Prepping subsets...")

    # how many ppl did/did not write in in the first place
    wrote_in_df = subset(write_ins_df,"wrote_in").dropna(how="all")
    useable_write_ins_df = subset(wrote_in_df,"useable_write_ins").dropna(how="all")
    # prepping subsets
        # all cis/trans ones are excluding detransitioners 
        # so we can make them their mutually exclusive own category
    cis_df = subset(write_ins_df,"is_cis").where(write_ins_df["detrans_user"] != "Yes").dropna(how="all")
    unspecified_trans_status_df = subset(write_ins_df,"unspecified_trans_status").where(write_ins_df["detrans_user"] != "Yes").dropna(how="all")
    trans_df = subset(write_ins_df,"is_trans").where(write_ins_df["detrans_user"] != "Yes").dropna(how="all")
    unspecified_direction_trans_df = subset(write_ins_df,"unspecified_trans_direction").where(write_ins_df["detrans_user"] != "Yes").dropna(how="all")
    transmasc_df = subset(write_ins_df, "is_transmasc").where(write_ins_df["detrans_user"] != "Yes").dropna(how="all")
    transfemme_df = subset(write_ins_df, "is_transfemme").where(write_ins_df["detrans_user"] != "Yes").dropna(how="all")
    detrans_df = subset(write_ins_df, "detrans_user").dropna(how="all")
    # specified assignments, excluding transmascs & transfemmes
    afab_df = subset(subset(write_ins_df,"is_afab"), "is_transmasc", False).dropna(how="all")
    amab_df = subset(subset(write_ins_df,"is_amab"), "is_transfemme", False).dropna(how="all")

    data = {}
    total_respondants = len(write_ins_df)

    print("How many write-ins did we get?")

    # how many ppl wrote in to begin with
    data["Write ins"] = pd.Series()
    data["Write ins"]["Respondants who wrote in (total)"] = len(wrote_in_df)
    data["Write ins"]["Respondants who wrote in something usable"] = len(useable_write_ins_df)
    
    print("How many intersections were written in?")

    data["Intersections"] = pd.Series()
    # how many used these labels
    for label in [
        "intersex_user",
        "autistic_user",
        "other_neurodivergent_user",
        "plural_user",
        "detrans_user",
    ]:
        data["Intersections"][sub("_", " ",label[:-5].capitalize())] = subset(wrote_in_df, label)["UserID"].count()

    print("Prepping for other dicts/series...")

    data["Total respondants"] = pd.Series()

    # categories & their sub labels
    key_dict = {
        "Alignments": {
            "Aligned respondants (total)":"UserID",
            "Aligned respondants (wrote in)":"wrote_in",
            "Female-aligned respondants":"is_female_aligned",
            "Male-aligned respondants":"is_male_aligned",
            "Conflicted female-aligned respondants":"is_conflicted_female_aligned",
            "Conflicted male-aligned respondants":"is_conflicted_male_aligned",
            "Non-male-aligned respondants (only non-alignment specified)":None,
            "Non-female-aligned respondants (only non-alignment specified)":None
        },
        "Conflicted queers":{
            "Conflicting queer labels":"conflicted_queer_user",
            "Dykefag":"dykefag_user",
            "Lesbianism for men":"lesbianism_for_men_user",
            "Faggotry for women":"faggotry_for_women_user"
        },
        "Sexuality":{
            "queer":"queer_unified",
            "same-sex-attracted labels":"gay_homo_bi_pan_unified",
            "mlm-aligned":"is_mlm_aligned",
            "wlw-aligned":"is_wlw_aligned",
            "gay":"gay_user",
            "lesbian":"lesbian_user",
            "dyke":"dyke_user",
            "bi/pan":"bi_pan_user",
            "ace/aro":"ace_aro_user",
            "twink":"twink_user",
            "bear":"bear_user",
        },
        "Expression":{
            "gnc":"is_gnc",
            "butch/masc":"butch_unified",
            "futch":"futch_user",
            "femme":"femme_user",
            "femboy":"femboy_user",
            "crossdresser":"crossdresser_user",
            "sissy":"sissy_user",
            "drag":"drag_user",
        },
        "Passing":{
            "female-presenting/-passing":"is_female_pass_pres",
            "male-presenting/-passing":"is_male_pass_pres",
            "trap":"trap_user", # trap is technically abt passing isn't it
        },
        "NB labels": {
            "nb":"nb_unified",
            "nb umbrella":"nb_umbrella_unified",
            "nb umbrella (minus nb)":"a_bi_fluid_flux_neu_gender_unified",
            "genderfluid":"genderfluid_unified",
            "genderflux":"genderflux_user",
            "demi":"demi_user",
            "neutral":"neutral_user",
            "agender/genderless":"agender_genderless_unified",
            "bi-/pangender":"bigender_pangender_unified",
        }
    }
    for key in key_dict:
        data[key] = {}
        for subkey in key_dict[key]:
            data[key][subkey] = pd.Series()

    for data_case in [
        "total", 
        "cis",
        "unspecified trans/cis status",
        "trans respondants",
        "unspecified trans direction",
        "transmasc",
        "transfemme",
        "detrans",
        "afabs (minus transmascs)",
        "amabs (minus transfemmes)",
    ]:
        print(f"Now running remaining items for case: {data_case}...")
        
        if data_case == "cis":
            df = cis_df
        elif data_case == "unspecified trans/cis status":
            df = unspecified_trans_status_df
        elif data_case == "trans respondants":
            df = trans_df
        elif data_case == "unspecified trans direction":
            df = unspecified_direction_trans_df
        elif data_case == "transmasc":
            df = transmasc_df
        elif data_case == "transfemme":
            df = transfemme_df
        elif data_case == "detrans":
            df = detrans_df
        elif data_case == "afabs (minus transmascs)":
            df = afab_df
        elif data_case == "amabs (minus transfemmes)":
            df = amab_df
        else: df = write_ins_df # total

        totals = df.count() # this will count all the columns in one go

        data["Total respondants"][data_case] = totals["UserID"]

        # how many ppl used aligned labels
        aligned_df = subset(df,"unspecified_alignment",False).dropna(how="all") # who did specify alignment
        aligned_totals = aligned_df.count() # ""

        # if data_case == "afabs (minus transmascs)":
        #     print(aligned_df.dropna(how="all", axis=1).get(
        #         [
        #             'UserID', 
        #         ]
        #     ))

        for categ in key_dict:
            if categ == "Alignments":
                for key in key_dict[categ]:
                    if key_dict[categ][key]:
                        # totals & which alignments
                        data[categ][key][data_case] = aligned_totals[key_dict[categ][key]]
                        # cis respondants had the highest percent of alignments specified at ca 30% 
                        # vs 15% for unspecified status and 21% for trans respondants        

                data[categ]["Non-male-aligned respondants (only non-alignment specified)"][data_case] = aligned_df.where(
                    (aligned_df["is_non_male_aligned"] == "Yes") & (
                    aligned_df["is_female_aligned"] != "Yes") & ( # strictly only non-alignment specified
                    aligned_df["is_conflicted_female_aligned"] != "Yes")
                )["UserID"].count()
                data[categ]["Non-female-aligned respondants (only non-alignment specified)"][data_case] = aligned_df.where(
                    (aligned_df["is_non_female_aligned"] == "Yes") & (
                    aligned_df["is_male_aligned"] != "Yes") & ( # strictly only non-alignment specified
                    aligned_df["is_conflicted_male_aligned"] != "Yes")
                )["UserID"].count()

                ## TODO we have some leaks among our trans respondants' alignments: 
                # 9 unspecified alignment ppl still have some alignments?? how and why???
                # TODO we also have some afabs/amabs that have an alignment that would indicate that they're trans, 
                # yet they're not counted as transmasc/transfemme??
            else:
                for key in key_dict[categ]:
                    data[categ][key][data_case] = totals[key_dict[categ][key]]
                    # conflicted queer labels
                        # devastating numbers lmao 
                        # 70% of our male lesbians are *explicitly identifyable as transmascs*
                        # unspecified trans direction in second with 18%
                        # unspecified trans/cis status in third with 10%
                            # my guess is that these are also going to turn out transmasc let's be real
                        # we have only 1 transfemme and 2 cis respondants who used male lesbian terms

                        # TODO have we crossreferenced alignment w lesbian etc 
                        # labels yet to identify any other male lesbians etc?
                        ## TODO do we want to also check the nb lesbians?

                    # expression
                        # I was like huhhhh the non-transfemme amabs rly got high % for gnc and femme huh! 
                        # and then I remembered that 20 of them are literally femboys 
                        # which would auto-qualify them for those two categories
                        # and the totals are like 22 and 35 respectively, 
                        # like that's most of those, yeah no shit sherlock
                            # I guess we're learning that amab femboys are more likely to specify 
                            # their birth assignment than other non-transfemme amab ppl
                            # which is likely BC there are so goddamn many transmasc femboys out here
                            # -> the amab ones want to make sure they're represented accurately as such
                            # -> other labels have less need for specifying birth assignment
                                # ex lesbian etc would only require specification for trans ppl 
                                # -> no need for cis lesbians to specify birthsex 
                                # bc amab lesbians can't not be transfemme
                                    # I'd bet money that those two(2) def not transfemme amab specifiers 
                                    # that wrote in lesbian are also femboys
                        # generally tho
                        # - ppl who specified afab & amab status (outside of transmasc/-femme) are
                        # more likely to be gnc/have specified expression than our other categories
                        # - detransitioners have the highest rate of gnc-ity after 
                        # our non-transfemme amabs (due to the 20 femboys) (makes sense that gnc ppl 
                        # would be most likely to try transition & then figure out that it wasn't right 
                        # for them bc they're just gnc)
                        # -> part of this is probably bc specific gnc-ity (ex femme) is only specified by write-ins, 
                        # as are afab/amab/detrans status 
                            # -> ppl who were writing in anyway vs bigger number of ppl who didn't write in anything
                            # BUT even gnc total (which had a tickbox!) is highest for amabs & detransitioners!
                            # and afabs are on par w the transmascs (and a bit more than unspecified trans direction)

                    # passing
                        # passing/presentation specified by only handful of ppl 
                            # but a good number of ppl who present in line w their birthsex 
                            # also specified birthsex without being trans!
                        # and the only ppl who present as opposite of their birthsex 
                            # are also identifiably transmasc/transfemme respectively
                            # -> further corroborating trans-alignment in spite of copium 
                            # same as we already saw in pronouns
                        # high % of ppl who specified this also specified their birthsex if not trans

                    # nb labels
                        # TODO do we have demi unified w its tickboxes? numbers seem suspisciously low
                        # it's very funny to me to see that even among 
                        # gender census's limited birthsex info, 
                        # the afabs are still more likely to use 
                        # more niche/particular (nb etc) labels than the amabs lmao
                            # higher on most non-nb-itself nb umbrella labels
                            # transmascs usually closer to unspecified trans section than transfemmes
                                # -> further corroborating my suspicious that 
                                # unspecified section is mostly transmascs too

    print("Calculating percentages...")

    for categ in key_dict:
        rel_dict = data[categ]
        for label_key in rel_dict:
            srs = rel_dict[label_key]
            # percentage of total number of (this category of) respondants
                # -> if similar, the label is used about the same across categories
                # -> if any category sticks out (barring very low numbers), 
                # it means that label is more popular among that category
            per_srs = srs.mask(
                cond=srs != None,
                other=percent(srs, data["Total respondants"].loc[srs.index])
            )
            # percentage of this label's users this category of respondants makes up
                # -> of the ppl who use this label, these are the biggest chunk
                # -> based on sheer numbers, 
                # not balanced for how many of this category there were total
            label_per_srs = srs.apply(percent, args=[srs["total"]])
            new_df = pd.DataFrame(
                columns=["#", "% of total", "% of label"], 
                data={"#": srs, "% of total": per_srs, "% of label": label_per_srs,}
            )
            data[categ][label_key] = new_df

    return data



if __name__ == "__main__":
    from utils.csv_reader import df_from_csv

    # pronoun_df = df_from_csv("data/cleaned_q9_with_new_columns/q9_clean_01.csv")
    # print(prep_pronoun_data(pronoun_df))

    # tickbox_label_df = df_from_csv("data/cleaned_q1_with_new_columns/q1_clean_01.csv")
    # print(prep_label_tickbox_data(tickbox_label_df))

    # print(prep_pronouns_by_labels(tickbox_label_df, pronoun_df))

    # geo_df = df_from_csv("data/separated_questions/q35_location.csv")
    # print(prep_geo_data(geo_df))

    # source_df = df_from_csv("data/cleaned_q37_with_new_columns/q37_clean_01.csv").set_index("UserID")
    # timestamp_df = df_from_csv("data/separated_questions/timestamp_for_sorting.csv").set_index("UserID")
    # source_with_timestamp_df = source_df.join(timestamp_df, lsuffix="left", rsuffix="right")
    # print(prep_survey_origin(source_with_timestamp_df))

    # write_ins_df = df_from_csv("data/cleaned_q2_with_new_columns/q2_cross_referenced_01.csv")
    # print(
    # prep_write_in_data(write_ins_df)
    # )

    # TODO
    # we have an afab who's non-female aligned, is this smth we would be including in transmasc or nah?