import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from visualisation.vis_utils import make_colour_list, make_labels
from visualisation.chart_import_data import pronoun_cases, alignment_cases, tickbox_label_cases, pie_titles

def make_pie(input_srs:pd.Series, data_case:str):
    """
    make pie chart
    """

    # making colours
    if data_case in pronoun_cases:
        colour_case = "pronouns"
    elif data_case in alignment_cases:
        colour_case = "alignments"
    elif data_case in tickbox_label_cases:
        colour_case = "tickbox_labels"
    else:
        colour_case = "other_stuff"
    
    colours = make_colour_list(input_srs.index, colour_case)

    # making labels
    labels = make_labels(input_srs.index, data_case, "pie")
    
    # making other variables
    values = input_srs.values
    text = [str(number) + "%" for number in input_srs.values]

    # making titles
    suffix = "(Gender Census 2024)" # to be made variable later when multiple year options
    title_portion = pie_titles[data_case]
    title = f"{title_portion}{suffix}"

    # making fig
    fig = go.Figure(data=[
        go.Pie(labels=labels, values=values, text=text, marker_colors=colours, 
               textinfo="text+label", textposition="inside")
    ])

    # updating layout
    fig.update_layout(
        uniformtext_minsize=14, 
        uniformtext_mode="hide",
        title = title
    )

    # hiding legend
    if data_case in [
        "tickbox_nb_no_nb",
        "tickbox_nb_no_nb_umbrella",
        "tickbox_insanity"
    ]:
        fig.update_layout(
            showlegend=False
        )

    return fig