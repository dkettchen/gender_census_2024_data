import pandas as pd
import plotly.express as px

def make_simple_bar(input_series:pd.Series, data_case:str):
    """
    makes simple bar chart
    """
    fig = px.bar(input_series, text_auto=True)
    fig.update_yaxes(range=[0, 100])
    fig.update_layout(
        showlegend=False,
    )

    return fig

def make_grouped_bar(input_series:pd.Series, data_case:str):
    """
    makes grouped bar chart
    """
    fig = px.bar(input_series, barmode="group")

    return fig