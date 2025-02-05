import pandas as pd
from visualisation.make_bar_charts import make_simple_bar, make_grouped_bar
from visualisation.make_prepped_df import count_df
from visualisation.make_pie_charts import make_pie

def make_label_tickbox_charts(input_df:pd.DataFrame):
    """
    runs label tickbox chart code on input df, which must contain relevant columns 
    (as edited from raw by src/make_label_combos.py)

    writes files to visualisation/charts/
    """

    tickbox_df = input_df.copy()

    folder = "visualisation/charts/label_tickbox_"
    
    # total users per tickbox label (as is) (bars)
    total_users_df = count_df(tickbox_df, "tickbox_label_total")
    total_users_fig = make_simple_bar(total_users_df, "tickbox_label_total")
    total_users_fig.write_image(
        f"{folder}total_users.png",
        height=800,
        width=1500,
    )

    # nb label users vs total nb umbrella label users (2 bars)
    # nb labels vs other nb umbrella labels (comparison in each label's numbers) (bars)
    nb_users_df = count_df(tickbox_df, "tickbox_nb_labels")
    nb_users_fig = make_simple_bar(nb_users_df, "tickbox_nb_labels")
    nb_users_fig.write_image(
        f"{folder}nb_users.png",
        height=800,
        width=1500,
    )
    
    # trans, cis, conflicted, unspecified (pie)
    trans_cis_df = count_df(tickbox_df, "tickbox_trans_cis_labels")
    trans_cis_fig = make_pie(trans_cis_df, "tickbox_trans_cis_labels")
    trans_cis_fig.write_image(
        f"{folder}trans_cis_pie.png",
        height=800,
        width=800,
    )

    # transmasc, transfemme, unspecified trans (pie)
    trans_direction_df = count_df(tickbox_df, "tickbox_trans_direction_labels")
    trans_direction_fig = make_pie(trans_direction_df, "tickbox_trans_direction_labels")
    trans_direction_fig.write_image(
        f"{folder}trans_direction_pie.png",
        height=800,
        width=800,
    )

    # nb vs not nb (pie)
    nb_no_nb_df = count_df(tickbox_df, "tickbox_nb_no_nb")
    nb_no_nb_fig = make_pie(nb_no_nb_df, "tickbox_nb_no_nb")
    nb_no_nb_fig.write_image(
        f"{folder}nb_vs_no_nb_pie.png",
        height=800,
        width=800,
    )
    
    # nb umbrella vs not nb umbrella (pie)
    nb_no_nb_umbrella_df = count_df(tickbox_df, "tickbox_nb_no_nb_umbrella")
    nb_no_nb_umbrella_fig = make_pie(nb_no_nb_umbrella_df, "tickbox_nb_no_nb_umbrella")
    nb_no_nb_umbrella_fig.write_image(
        f"{folder}nb_vs_no_nb_umbrella_pie.png",
        height=800,
        width=800,
    )

    # of non-trans users what are their top used labels?
    non_trans_df = count_df(tickbox_df, "tickbox_non_trans")
    non_trans_fig = make_simple_bar(non_trans_df, "tickbox_non_trans")
    non_trans_fig.write_image(
        f"{folder}non_trans_users.png",
        height=800,
        width=800,
    )

    # of non-nb umbrella users what are their top used labels?
    non_nb_df = count_df(tickbox_df, "tickbox_non_nb")
    non_nb_fig = make_simple_bar(non_nb_df, "tickbox_non_nb")
    non_nb_fig.write_image(
        f"{folder}non_nb_users.png",
        height=800,
        width=800,
    )

    # of non-nb & non-trans users what are their remaining top labels? (bars)
    non_nb_trans_df = count_df(tickbox_df, "tickbox_non_nb_trans")
    non_nb_trans_fig = make_simple_bar(non_nb_trans_df, "tickbox_non_nb_trans")
    non_nb_trans_fig.write_image(
        f"{folder}non_nb_non_trans_users.png",
        height=800,
        width=800,
    )

    # how many respondants are trans/not nb, nb/not trans, trans+nb, neither (without umbrella) (pie)
    trans_nb_df = count_df(tickbox_df, "tickbox_trans_nb")
    trans_nb_fig = make_pie(trans_nb_df, "tickbox_trans_nb")
    trans_nb_fig.write_image(
        f"{folder}trans_nb_intersection.png",
        height=800,
        width=900,
    )

    # how many respondants are trans/not nb, nb/not trans, trans+nb, neither (with umbrella) (pie)
    trans_nb_umb_df = count_df(tickbox_df, "tickbox_trans_nb_umbrella")
    trans_nb_umb_fig = make_pie(trans_nb_umb_df, "tickbox_trans_nb_umbrella")
    trans_nb_umb_fig.write_image(
        f"{folder}trans_nb_umbrella_intersection.png",
        height=800,
        width=900,
    )

# TODO:
    # refactor & stream line stuff a bit better ✅
    # add label counts to column editing file ✅

    # how many respondants use only nb/nb umbrella labels, vs only other labels, vs multiple labels
        # -> to demonstrate that nb does not exist away from other queerness/transness 
        # unlike queerness & transness themself who can very much exist apart from each other/other labels
        # re nb is just like trans + gay n you don't need to pay us any mind 
        # just like you don't to the gnc gays or the gc trans

            # only uses 1 tickbox label total
            #   for each tickbox label
            # uses multiple labels:
            #   nb umbrella only (ie agender + nb + genderfluid etc)
            #   multi incl but not exclve nb umbrella (ie trans + nb + fag etc)
            #   multi - nb umbrella (ie trans + fag + queer but no nb labels involved)
            # didn't tick any labels
            # -> pie of these mutually exclusive categories

        # -> possibly other charts w smaller groups

            # of nb umbrella users who uses only 1 nb umbrella label (each label)
                # -> to show labels are still largely synonymous, not individual IDs

            # how many respondants only use 1 tickbox/don't use any of the provided labels

    # possibly repeat (mutually exclusive categories combo/not combo w nb) for each of "queer", "genderqueer", "gnc" 
    # (and possibly human/person + no self-descr) user subsets
    # possibly check what labels our very few cis-claiming respondants use


# then move on to write ins & pronoun crossovers!