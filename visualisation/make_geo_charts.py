import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from re import sub

def english_speaking_or_no(input_df:pd.DataFrame):
    """
    takes the location df as read from the q35 file

    returns a new column with a new column that specifies whether the country is 
    english speaking, non-english speaking, or was not specified
    """

    english_speaking_countries = [  
        "United States",
        "United Kingdom",
        "Australia",
        "New Zealand",
        "Canada",
        "Ireland",
        # and a buncha islands not in our list
    ]
    not_specified = [
        'Prefer not to say', 
        "['country aggregated']", 
        "None"
    ]

    new_df = input_df.copy().set_index("UserID")

    new_df["english_or_no"] = "english_speaking" # default
    new_df["english_or_no"] = new_df["english_or_no"].mask(
        (
            new_df["q35_Location"] != "United States") & (
            new_df["q35_Location"] != "United Kingdom") & (
            new_df["q35_Location"] != "Australia") & (
            new_df["q35_Location"] != "New Zealand") & (
            new_df["q35_Location"] != "Canada") & (
            new_df["q35_Location"] != "Ireland") & (
            new_df["q35_Location"] != 'Prefer not to say') & (
            new_df["q35_Location"] != "['country aggregated']") & (
            new_df["q35_Location"] != "None"
        ), 
        other="non_english_speaking"
    )
    new_df["english_or_no"] = new_df["english_or_no"].mask(
        (
            new_df["q35_Location"] == 'Prefer not to say') | (
            new_df["q35_Location"] == "['country aggregated']") | (
            new_df["q35_Location"] == "None"
        ), 
        other="not_specified"
    )

    return new_df

def add_other_countries(country_srs:pd.Series, total_len:int, percent_cutoff:float=0.5):
    """
    util to adjust geo data dict based on data case

    it groups any countries that make up less than 0.5% of the dataset together
    """ # TODO figure out how this will work with label df instead of a series??
    
    # grouping together smallest represented countries to remove clutter
    small_countries = 0
    new_country_srs = pd.Series()
    for country in country_srs.index:
        country_percent = country_srs[country]/total_len * 100
        if country_percent < percent_cutoff:
            small_countries += country_srs[country]
        else:
            new_country_srs[country] = country_srs[country]
    new_country_srs[f"other countries (<{percent_cutoff}%)"] = small_countries

    return new_country_srs

def make_geo_charts(input_df:pd.DataFrame, data_case:str):
    """
    takes input df from q35

    makes pie chart about the countries most represented among respondants
    """

    if data_case == "total":
        new_df = input_df.copy().set_index("UserID")
        new_srs = new_df["q35_Location"] # countries column
    elif data_case == "english_speaking_countries":
        new_df = english_speaking_or_no(input_df)
        new_srs = new_df["english_or_no"] # english or no column

    folder = "visualisation/charts/countries_"
    suffix = "(Gender Census 2024)"

    # fixing list values back to strings smh
    for i in range(len(new_srs)):
        item = new_srs.iloc[i]
        if type(item) != str:
            new_srs.iloc[i] = str(item)

    # we should be able to just group by the country column 
    # (which is the only column other than the index)
    # & count
    country_srs = new_srs.groupby(by=new_srs.values).count().sort_values(ascending=False)

    if data_case == "total": # adding "other countries" for any countries under 0.5%
        country_srs = add_other_countries(country_srs, len(input_df))

    # make a pie chart
    labels = country_srs.index
    values = country_srs.values
    if data_case == "total":
        colour_dict = { # assigning continent specific colours to shown countries
            "Canada":"orangered",
            "United States":"crimson", # red for danger lmao 
            "Brazil":"tomato",

            "United Kingdom":"royalblue", 
            "France":"darkblue", 
            "Norway":"indigo", 
            "Sweden":"mediumslateblue", 
            "Poland":"cornflowerblue", 
            "Germany":"powderblue",
            "Finland":"teal",
            "Russia":"aquamarine",
            "Austria":"skyblue",
            "Spain":"blue",
            "Italy":"cadetblue",
            "Ireland":"steelblue",
            "Netherlands":"lightsteelblue",

            "China":"mediumseagreen",
            "Japan":"olivedrab", 
            "South Korea":"yellowgreen", 
            "Thailand":"green", 

            "Australia":"gold", 
            "New Zealand":"darkgoldenrod",

            "other countries (<0.5%)":"darkgrey",
            "Prefer not to say":"grey",
        }
        filler_colours = px.colors.qualitative.Pastel + px.colors.qualitative.Pastel + px.colors.qualitative.Pastel
        colours = []
        for i in range(len(labels)):
            if labels[i] not in colour_dict.keys():
                colours.append(filler_colours[i])
            else:
                colours.append(colour_dict[labels[i]])
    elif data_case == "english_speaking_countries":
        colours = ["royalblue", "deeppink", "lightgrey"]
    
    fig = go.Figure(data=[
        go.Pie(
            labels=labels, values=values, 
            textposition="inside",
            textinfo="label+percent",
            marker_colors=colours
        )
    ])

    data_case_edit = sub(r"_"," ", data_case)
    chart_title = f"Respondants' locations ({data_case_edit}) {suffix}"

    fig.update_layout(
        uniformtext_minsize=10,
        uniformtext_mode="hide",
        title=chart_title
    )

    fig.write_image(
        f"{folder}{data_case}.png",
        height=800,
        width=800,
    )
