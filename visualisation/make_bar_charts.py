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

    - "tickbox_label_total"
    - "tickbox_nb_labels"
    """

    # making colours
    if data_case in ["total_users","only_one_set","big_three_combos","it_and_neo_combos"]:
        colours = make_colour_list(input_srs.index, "pronouns")
    elif data_case in ["tickbox_label_total", "tickbox_nb_labels"]:
        colours = make_colour_list(input_srs.index, "tickbox_labels")

    # making labels
    if data_case in ["tickbox_nb_labels"]: # removing _tickbox & is_ & add _total to nb/nb_umbrella
        labels = []
        for column in input_srs.index:
            if "is_" not in column:
                new_column = column[:-8]
            else:
                new_column = column[3:-8]

            if new_column in ["nb", "nb_umbrella"]:
                new_column += "_total"
            
            labels.append(new_column)
    elif data_case == "tickbox_label_total": # removing _tickbox ending
        labels = [column[:-8] for column in input_srs.index]
    else:
        labels = input_srs.index
    
    # making values
    values = input_srs.values

    fig = go.Figure(data=[
        go.Bar(x=labels, y=values, marker_color=colours)
    ])

    if data_case not in ["total_users", "tickbox_label_total", "tickbox_nb_labels",]:
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
    elif data_case == "tickbox_label_total":
        title = f"% of respondants who ticked this label {suffix}"
    elif data_case == "tickbox_nb_labels":
        title = f"% of respondants who use nonbinary labels {suffix}"

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