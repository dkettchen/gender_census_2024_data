import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from visualisation.vis_utils import make_colour_list

def make_pie(input_srs:pd.Series, data_case:str):
    """
    make pie chart
    """

    if data_case == "pronoun_pie":
        colour_case = "pronouns"
    elif data_case == "aligned_pronoun_pie":
        colour_case = "alignments"
    colours = make_colour_list(input_srs.index, colour_case)

    labels = input_srs.index
    values = input_srs.values
    text = [str(number) + "%" for number in input_srs.values]

    suffix = "(Gender Census 2024)"
    if data_case == "pronoun_pie":
        title = f"Pronoun sets used by respondants (order insensitive) {suffix}"
    elif data_case == "aligned_pronoun_pie":
        title = f"% of respondants using aligned/unaligned pronoun sets {suffix}"

    fig = go.Figure(data=[
        go.Pie(labels=labels, values=values, text=text, marker_colors=colours, 
               textinfo="text+label", textposition="inside")
    ])

    fig.update_layout(
        uniformtext_minsize=14, 
        uniformtext_mode="hide",
        title = title
    )

    return fig