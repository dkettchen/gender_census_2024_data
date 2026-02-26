import pandas as pd
import plotly.graph_objects as go
from visualisation.vis_utils.colour_palettes import colours as palette
from visualisation.vis_utils.import_data import titles
from re import sub

def make_pie(input_dict:dict, data_case:str):
    """
    make pie chart
    """

    # making labels
    if data_case in [
        "lesbianism_for_men",
        "faggotry_for_women",
    ]:
        labels = [l for l in list(input_dict.keys()) if l in palette["five_categories"]]
    else:
        labels = list(input_dict.keys())
    
    # making colours
    if data_case in [
        "lesbianism_for_men",
        "faggotry_for_women",
    ]:
        colours = [palette["five_categories"][l] for l in labels]
    elif "Trans-aligned" in data_case:
        colours = [palette["alignments"][l] for l in labels]
    elif "alignment" in data_case:
        colours = [palette["alignments"][l] for l in labels]
    elif "pronoun" in data_case.lower():
        colours = [palette["pronouns"][l] for l in labels]

    # making other variables
    values = [input_dict[l] for l in labels]
    # text = [str(number) + "%" for number in values]

    # making titles
    suffix = "(Gender Census 2024)" # to be made variable later when multiple year options
    if data_case in titles:
        title_portion = titles[data_case]
    else:
        title_portion = data_case + " "
    title = f"{title_portion}{suffix}"

    # making fig
    fig = go.Figure(data=[
        go.Pie(labels=labels, values=values, 
               marker_colors=colours, 
               textinfo="label+value+percent", textposition="inside", insidetextorientation="horizontal")
    ])

    # updating layout
    fig.update_layout(
        uniformtext_minsize=12, 
        uniformtext_mode="hide",
        title = title
    )

    # hiding legend
    if data_case in [
    ]:
        fig.update_layout(
            showlegend=False
        )

    return fig