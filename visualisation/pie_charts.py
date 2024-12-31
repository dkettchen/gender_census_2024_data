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

    fig = go.Figure(data=[
        go.Pie(labels=labels, values=values, text=text, marker_colors=colours, 
               textinfo="text+label", textposition="inside")
    ])

    fig.update_layout(uniformtext_minsize=8, uniformtext_mode="hide")

    return fig