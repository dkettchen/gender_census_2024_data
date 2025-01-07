import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from visualisation.vis_utils import make_colour_list, make_labels

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

def make_simple_bar(input_srs:pd.Series, data_case:str):
    """
    makes simple bar chart

    data_cases:
    - "total_users"
    - "only_one_set"
    - "big_three_combos"
    - "it_and_neo_combos"

    - "tickbox_label_total"
    - "tickbox_nb_labels"
    - "tickbox_non_trans"
    - "tickbox_non_nb"
    - "tickbox_non_nb_trans"
    """

    # making colours
    if data_case in ["total_users","only_one_set","big_three_combos","it_and_neo_combos"]:
        colour_case = "pronouns"
    elif "tickbox" in data_case:
        colour_case = "tickbox_labels"
    colours = make_colour_list(input_srs.index, colour_case)

    # making labels
    labels = make_labels(input_srs.index, data_case)

    # making values
    values = input_srs.values

    # making fig
    fig = go.Figure(data=[
        go.Bar(x=labels, y=values, marker_color=colours)
    ])

    # setting range
    if data_case in [ # full range
        "total_users", 
        "tickbox_label_total", 
        "tickbox_nb_labels",
    ]:
        range = [0, 100]
    else: # default to 50% range
        range = [0, 50]

    # make title
    suffix = "(Gender Census 2024)" # make this variable once we implement multiple year options
    title_portion = bar_titles[data_case]
    title = f"{title_portion}{suffix}"

    # updating stuff
    fig.update_yaxes(range=range)
    fig.update_layout(
        showlegend=False,
        title=title
    )

    return fig

def make_grouped_bar(input_srs:pd.Series, data_case:str):
    """
    makes grouped bar chart
    """
    fig = px.bar(input_srs, barmode="group")

    return fig