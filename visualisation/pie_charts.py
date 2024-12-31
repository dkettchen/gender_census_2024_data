import pandas as pd
import plotly.express as px

def make_pie(input_srs:pd.Series, data_case:str):
    """
    make pie chart
    """

    fig = px.pie(input_srs, values=0, names=input_srs.index)

    return fig