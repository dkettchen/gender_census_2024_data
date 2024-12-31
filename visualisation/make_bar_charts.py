import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from visualisation.vis_utils import make_colour_list

def make_simple_bar(input_srs:pd.Series, data_case:str):
    """
    makes simple bar chart

    data_cases:
    - "total_users"
    - "only_one_set"
    - "big_three_combos"
    - "it_and_neo_combos"
    """
    colours = make_colour_list(input_srs.index, "pronouns")

    labels = input_srs.index
    values = input_srs.values

    fig = go.Figure(data=[
        go.Bar(x=labels, y=values, marker_color=colours)
    ])

    if data_case != "total_users":
        range = [0, 50]
    else:
        range = [0, 100]

    suffix = "(Gender Census 2024)"

    if data_case == "total_users":
        title = f"Total % of respondants who use this pronoun set {suffix}"
    elif data_case == "only_one_set":
        title = f"% of respondants who use only this pronoun set {suffix}"
    elif data_case == "big_three_combos":
        title = f"% of respondants who use a combo of she, he, and they (order insensitive) <br>{suffix}"
    elif data_case == "it_and_neo_combos":
        title = f"% of respondants who use she, he, or they w/ it or neopronouns (order insensitive) <br>{suffix}"

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