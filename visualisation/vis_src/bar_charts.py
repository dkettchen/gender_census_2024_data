import pandas as pd
import plotly.graph_objects as go
from visualisation.vis_utils.import_data import titles
from visualisation.vis_utils.colour_palettes import colours as palette

def make_simple_bar(input_dict:dict, data_case:str):
    """
    makes simple bar chart
    """

    # making labels
    labels = list(input_dict.keys())

    # get colours
    if data_case == "write_ins_intersections":
        colours = [palette["intersections"][c] for c in labels]

    # making values
    values = list(input_dict.values())

    # making fig
    fig = go.Figure(data=[go.Bar(
        x=labels, y=values, 
        marker_color=colours
    )])

    # setting range
    range = [0, 100]

    # make title
    suffix = "(Gender Census 2024)" # make this variable if and when we implement multiple year options
    title_portion = titles[data_case]
    title = f"{title_portion}{suffix}"

    # updating stuff
    if data_case not in ["write_ins_intersections"]:
        fig.update_yaxes(range=range)
    fig.update_layout(
        showlegend=False,
        title=title
    )

    return fig
