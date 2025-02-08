import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from visualisation.vis_utils import make_colour_list, make_labels
from visualisation.chart_import_data import bar_titles, pronoun_cases, tickbox_label_cases

def make_simple_bar(input_srs:pd.Series, data_case:str):
    """
    makes simple bar chart
    """

    # making colours
    if data_case in pronoun_cases:
        colour_case = "pronouns"
    elif data_case in tickbox_label_cases:
        colour_case = "tickbox_labels"
    colours = make_colour_list(input_srs.index, colour_case)

    # making labels
    labels = make_labels(input_srs.index, data_case)

    # making values
    values = input_srs.values

    # making fig
    fig = go.Figure(data=[go.Bar(x=labels, y=values, marker_color=colours)])

    # setting range
    if data_case in [ # full range
        "total_users", 
        "tickbox_label_total", 
        "tickbox_nb_labels",
        "tickbox_non_trans",
        "tickbox_non_nb",
        "tickbox_non_nb_trans",
        "tickbox_trans_labels",
        "tickbox_queer_labels",
    ]:
        range = [0, 100]
    elif data_case in [ # for minuscule values sub-10%
        "tickbox_only_one_label", 
        "tickbox_only_one_label_syn"
    ]:
        range = [0, 10]
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