import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from visualisation.vis_utils import make_colour_list

def make_pie(input_srs:pd.Series, data_case:str):
    """
    make pie chart
    """

    colours = make_colour_list(input_srs.index, "pronouns")

    labels = input_srs.index
    values = input_srs.values
    text = [str(number) + "%" for number in input_srs.values]

    suffix = "(Gender Census 2024)"
    if data_case == "pronoun_pie":
        title = f"Pronoun sets used by respondants (order insensitive) {suffix}"

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