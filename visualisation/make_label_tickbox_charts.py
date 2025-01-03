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

    nb_users_df = count_df(tickbox_df, "tickbox_nb_labels")
    nb_users_fig = make_simple_bar(nb_users_df, "tickbox_nb_labels")
    nb_users_fig.write_image(
        f"{folder}nb_users.png",
        height=800,
        width=1500,
    )
    

    # total users per new columns
        # trans, cis, conflicted, unspecified (pie)
        # transmasc, transfemme, unspecified trans (pie)
        # nb vs not nb (pie)
        # nb umbrella vs not nb umbrella (pie)
        # nb label users vs total nb umbrella label users (2 bars)
        # nb labels vs other nb umbrella labels (comparison in each label's numbers) (bars)

    # cross overs
        # top 5-10 labels per each label/category
        # 

    #
    