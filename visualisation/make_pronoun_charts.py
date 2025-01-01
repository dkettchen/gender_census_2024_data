import pandas as pd
from visualisation.make_bar_charts import make_simple_bar, make_grouped_bar
from visualisation.make_prepped_df import count_df
from visualisation.make_pie_charts import make_pie

def make_pronoun_charts(input_df:pd.DataFrame):
    """
    runs pronoun chart code on input df, which must contain relevant columns 
    (as edited from raw by src/make_pronoun_combos.py)

    writes files to visualisation/charts/
    """

    pronoun_df = input_df.copy()

    folder = "visualisation/charts/pronoun_"
    
    # total users per pronoun as per original data (incl any users)
    total_users_df = count_df(pronoun_df, "total_users")
    total_fig = make_simple_bar(total_users_df, "total_users")
    total_fig.write_image(
        f"{folder}total_users.png",
        height=800,
        width=800,
    )

    # only one set/type users
    only_set_df = count_df(pronoun_df, "only_one_set")
    only_set_fig = make_simple_bar(only_set_df, "only_one_set")
    only_set_fig.write_image(
        f"{folder}single_set_users.png",
        height=800,
        width=800,
    )

    # big three combos (she/they, he/they, she/he, she/he/they)
    big_three_df = count_df(pronoun_df, "big_three_combos")
    big_three_fig = make_simple_bar(big_three_df, "big_three_combos")
    big_three_fig.write_image(
        f"{folder}big_three_combo_users.png",
        height=800,
        width=800,
    )

    # combos with it and neo pronouns
    it_and_neo_df = count_df(pronoun_df, "it_and_neo_combos")
    it_and_neo_fig = make_simple_bar(it_and_neo_df, "it_and_neo_combos")
    it_and_neo_fig.write_image(
        f"{folder}it_and_neo_combo_users.png",
        height=800,
        width=800,
    )


    # all new categories as a pie chart
    pie_df = count_df(pronoun_df, "pronoun_pie")
    pie_fig = make_pie(pie_df, "pronoun_pie")
    pie_fig.write_image(
        f"{folder}pie.png",
        height=800,
        width=1000,
    )

    # pie chart by alignment
    pie_df = count_df(pronoun_df, "aligned_pronoun_pie")
    pie_fig = make_pie(pie_df, "aligned_pronoun_pie")
    pie_fig.write_image(
        f"{folder}alignment_pie.png",
        height=800,
        width=800,
    )
