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

# TODO:

    # how many respondants are trans/not nb, nb/not trans, trans & nb, neither? (pie)

    # possibly repeat for each of "queer", "genderqueer", "gnc" 
    # (and possibly human/person + no self-descr) user subsets

    # possibly check what labels our very few cis-claiming respondants use

    # how many respondants use ONLY nb/nb umbrella labels, vs how many use multiple/only other labels
        # bc that number is relevant to compare to our total nb/nb umbrella users
        # cause I wanna be able to point out that nb labels are inextricably linked to transness & queerness, 
        # they are not a separate concept, you rarely can be identifying as nb without identifying as some 
        # other variety of gender queer, unlike straight trans & cis gc queer ppl who can ID as those things 
        # without the additional queerness
            # -> to my point re nb is just the gay version of being trans/
            # some of the gnc gays you already don't pay attention to
    # maybe we can have one chart be just how many ppl use any of the tickboxes only / didn't tick any
    # and one abt how many ppl of the ones under nb umbrella only use one label
        # to demonstrate these are still generally synonymous, they are not individual IDs

# I want to do a buncha refactoring to make this more stream lined already please

# then move on to write ins & pronoun crossovers!