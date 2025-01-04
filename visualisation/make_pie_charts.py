import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from visualisation.vis_utils import make_colour_list

def make_pie(input_srs:pd.Series, data_case:str):
    """
    make pie chart
    """

    # making colours
    if data_case == "pronoun_pie":
        colour_case = "pronouns"
    elif data_case == "aligned_pronoun_pie":
        colour_case = "alignments"
    elif "tickbox" in data_case:
        colour_case = "tickbox_labels"
    colours = make_colour_list(input_srs.index, colour_case)

    # making labels
    if "tickbox" in data_case: # shortening labels
        labels = []
        for column in input_srs.index:
            if "unspecified" not in column and "conflicted" not in column:
                new_column = column[3:-8] # removing is_ and _tickbox
            elif "unspecified" in column:
                new_column = "unspecified"
            elif "conflicted" in column:
                new_column = "conflicted"
            labels.append(new_column)  
    else: # using index as is
        labels = input_srs.index
    
    # making other variables
    values = input_srs.values
    text = [str(number) + "%" for number in input_srs.values]

    # making titles
    suffix = "(Gender Census 2024)"
    if data_case == "pronoun_pie":
        title = f"Pronoun sets used by respondants (order insensitive) {suffix}"
    elif data_case == "aligned_pronoun_pie":
        title = f"% of respondants using aligned/unaligned pronoun sets {suffix}"
    elif data_case == "tickbox_trans_cis_labels":
        title = f"% of respondants who did/did not indicate cis or trans status via tickboxes {suffix}"
    elif data_case == "tickbox_trans_direction_labels":
        title = f"% of trans respondants who did/did not specify their direction via tickboxes {suffix}"

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