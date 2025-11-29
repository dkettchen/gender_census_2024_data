import pandas as pd
from visualisation.chart_bar import make_simple_bar, make_grouped_bar
from visualisation.chart_prep_dfs import count
from visualisation.chart_pie import make_pie

def make_label_tickbox_charts(input_df:pd.DataFrame):
    """
    runs label tickbox chart code on input df, which must contain relevant columns 
    (as edited from raw by src/make_label_combos.py)

    writes files to visualisation/charts/
    """

    tickbox_df = input_df.copy()

    folder = "visualisation/charts/label_tickbox_"
    
    # total users per tickbox label (as is) (bars)
    total_users_df = count(tickbox_df, "tickbox_label_total")
    total_users_fig = make_simple_bar(total_users_df, "tickbox_label_total")
    total_users_fig.write_image(
        f"{folder}total_users.png",
        height=800,
        width=1500,
    )

    # nb label users vs total nb umbrella label users (2 bars)
    # nb labels vs other nb umbrella labels (comparison in each label's numbers) (bars)
    nb_users_df = count(tickbox_df, "tickbox_nb_labels")
    nb_users_fig = make_simple_bar(nb_users_df, "tickbox_nb_labels")
    nb_users_fig.write_image(
        f"{folder}nb_users.png",
        height=800,
        width=1500,
    )
    
    # trans, cis, conflicted, unspecified (pie)
    trans_cis_df = count(tickbox_df, "tickbox_trans_cis_labels")
    trans_cis_fig = make_pie(trans_cis_df, "tickbox_trans_cis_labels")
    trans_cis_fig.write_image(
        f"{folder}trans_cis_pie.png",
        height=800,
        width=800,
    )

    # transmasc, transfemme, unspecified trans (pie)
    trans_direction_df = count(tickbox_df, "tickbox_trans_direction_labels")
    trans_direction_fig = make_pie(trans_direction_df, "tickbox_trans_direction_labels")
    trans_direction_fig.write_image(
        f"{folder}trans_direction_pie.png",
        height=800,
        width=800,
    )

    # nb vs not nb (pie)
    nb_no_nb_df = count(tickbox_df, "tickbox_nb_no_nb")
    nb_no_nb_fig = make_pie(nb_no_nb_df, "tickbox_nb_no_nb")
    nb_no_nb_fig.write_image(
        f"{folder}nb_vs_no_nb_pie.png",
        height=800,
        width=800,
    )
    
    # nb umbrella vs not nb umbrella (pie)
    nb_no_nb_umbrella_df = count(tickbox_df, "tickbox_nb_no_nb_umbrella")
    nb_no_nb_umbrella_fig = make_pie(nb_no_nb_umbrella_df, "tickbox_nb_no_nb_umbrella")
    nb_no_nb_umbrella_fig.write_image(
        f"{folder}nb_vs_no_nb_umbrella_pie.png",
        height=800,
        width=800,
    )

    # of non-trans users what are their top used labels?
    non_trans_df = count(tickbox_df, "tickbox_non_trans")
    non_trans_fig = make_simple_bar(non_trans_df, "tickbox_non_trans")
    non_trans_fig.write_image(
        f"{folder}non_trans_users.png",
        height=800,
        width=800,
    )

    # of non-nb umbrella users what are their top used labels?
    non_nb_df = count(tickbox_df, "tickbox_non_nb")
    non_nb_fig = make_simple_bar(non_nb_df, "tickbox_non_nb")
    non_nb_fig.write_image(
        f"{folder}non_nb_users.png",
        height=800,
        width=800,
    )

    # of non-nb & non-trans users what are their remaining top labels? (bars)
    non_nb_trans_df = count(tickbox_df, "tickbox_non_nb_trans")
    non_nb_trans_fig = make_simple_bar(non_nb_trans_df, "tickbox_non_nb_trans")
    non_nb_trans_fig.write_image(
        f"{folder}non_nb_non_trans_users.png",
        height=800,
        width=800,
    )

    # how many respondants are trans/not nb, nb/not trans, trans+nb, neither (without umbrella) (pie)
    trans_nb_df = count(tickbox_df, "tickbox_trans_nb")
    trans_nb_fig = make_pie(trans_nb_df, "tickbox_trans_nb")
    trans_nb_fig.write_image(
        f"{folder}trans_nb_intersection.png",
        height=800,
        width=900,
    )

    # how many respondants are trans/not nb, nb/not trans, trans+nb, neither (with umbrella) (pie)
    trans_nb_umb_df = count(tickbox_df, "tickbox_trans_nb_umbrella")
    trans_nb_umb_fig = make_pie(trans_nb_umb_df, "tickbox_trans_nb_umbrella")
    trans_nb_umb_fig.write_image(
        f"{folder}trans_nb_umbrella_intersection.png",
        height=800,
        width=900,
    )

    # how many respondants ticked only one label, and if so which one (incl synonyms)
    only_one_label_df = count(tickbox_df, "tickbox_only_one_label")
    only_one_label_fig = make_simple_bar(only_one_label_df, "tickbox_only_one_label")
    only_one_label_fig.write_image(
        f"{folder}single_label_users.png",
        height=800,
        width=800,
    )

    # how many respondants ticked only one label, and if so which one (excl synonyms)
    only_one_label_df = count(tickbox_df, "tickbox_only_one_label_syn")
    only_one_label_fig = make_simple_bar(only_one_label_df, "tickbox_only_one_label_syn")
    only_one_label_fig.write_image(
        f"{folder}single_label_users_excl_synonyms.png",
        height=800,
        width=800,
    )

    # what other labels do our trans respondants use?
    trans_labels_df = count(tickbox_df, "tickbox_trans_labels")
    trans_labels_fig = make_simple_bar(trans_labels_df, "tickbox_trans_labels")
    trans_labels_fig.write_image(
        f"{folder}trans_users.png",
        height=800,
        width=800,
    )

    # what other labels do our queer respondants use?
    queer_labels_df = count(tickbox_df, "tickbox_queer_labels")
    queer_labels_fig = make_simple_bar(queer_labels_df, "tickbox_queer_labels")
    queer_labels_fig.write_image(
        f"{folder}queer_users.png",
        height=800,
        width=800,
    )

    # how many respondants are trans/nb/queer (all intersections) (pie)
    trans_nb_umb_df = count(tickbox_df, "tickbox_trans_nb_queer")
    trans_nb_umb_fig = make_pie(trans_nb_umb_df, "tickbox_trans_nb_queer")
    trans_nb_umb_fig.write_image(
        f"{folder}trans_nb_queer_intersection.png",
        height=800,
        width=900,
    )

    # what other labels do our queer respondants use?
    gnc_labels_df = count(tickbox_df, "tickbox_gnc_labels")
    gnc_labels_fig = make_simple_bar(gnc_labels_df, "tickbox_gnc_labels")
    gnc_labels_fig.write_image(
        f"{folder}gnc_users.png",
        height=800,
        width=800,
    )

    # # let's just check all the combos of tickbox labels ppl have ticked???
    # all_label_insanity_df = count_df(tickbox_df, "tickbox_insanity")
    # all_label_insanity_fig = make_pie(all_label_insanity_df, "tickbox_insanity")
    # all_label_insanity_fig.write_image(
    #     f"{folder}all_label_combos.png",
    #     height=800,
    #     width=800,
    # )
    # # update it wasn't worth it lmao too few same ticked answers rip

# TODO:
    # what is the percentage of gnc respondants among various label groups?
        # maybe as a multi-pie plot?
        # -> trans, nb, queer
    # possibly check what labels our very few cis-claiming respondants use
