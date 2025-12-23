import pandas as pd
import plotly.graph_objects as go
from visualisation.vis_utils.colour_palettes import colours as palette
from visualisation.vis_utils.import_data import titles

def make_pie(input_dict:dict, data_case:str):
    """
    make pie chart
    """

    # making labels
    labels = [l for l in list(input_dict.keys()) if l in palette["five_categories"]]
    
    # making colours
    colours = [palette["five_categories"][l] for l in labels]
    
    # making other variables
    values = [input_dict[l] for l in labels]
    # text = [str(number) + "%" for number in values]

    # making titles
    suffix = "(Gender Census 2024)" # to be made variable later when multiple year options
    title_portion = titles[data_case]
    title = f"{title_portion}{suffix}"

    # making fig
    fig = go.Figure(data=[
        go.Pie(labels=labels, values=values, 
            #    text=text, 
               marker_colors=colours, 
               textinfo="label", textposition="inside")
    ])

    # updating layout
    fig.update_layout(
        uniformtext_minsize=14, 
        uniformtext_mode="hide",
        title = title
    )

    # hiding legend
    # if data_case in [
    #     "tickbox_nb_no_nb",
    #     "tickbox_nb_no_nb_umbrella",
    #     "tickbox_insanity"
    # ]:
    #     fig.update_layout(
    #         showlegend=False
    #     )

    return fig