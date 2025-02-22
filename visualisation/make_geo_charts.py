import pandas as pd
import plotly.graph_objects as go
from re import sub

def adjust_geo_data(country_srs:pd.Series, data_case:str, total_len:int):
    """
    util to adjust geo data dict based on data case

    if data_case="english_speaking_countries":
    - it groups the values by whether or not the country is majority english speaking

    if data_case="total":
    - it groups any countries that make up less than 0.5% of the dataset together
    """ # TODO figure out how this will work with label df instead of a series??
    
    # grouping by english speaking vs not english speaking countries
    if data_case == "english_speaking_countries":
        # wikipedia says these countries have 50%+ english as their native language
        english_speaking_countries = [  
            "United States",
            "United Kingdom",
            "Australia",
            "New Zealand",
            "Canada",
            "Ireland",
            # and a buncha islands not in our list
        ]

        # summing
        english_speakers = 0
        non_english_speakers = 0
        not_specified = 0
        for country in country_srs.index:
            if country in english_speaking_countries:
                english_speakers += country_srs[country]
            elif country in ['Prefer not to say', "['country aggregated']", "None"]:
                not_specified += country_srs[country]
            else:
                non_english_speakers += country_srs[country]
        
        # making new srs
        new_country_srs = pd.Series(
            index=["english-speaking", "non-english-speaking", "not specified"],
            data=[english_speakers, non_english_speakers, not_specified]
        )

    # grouping together smallest represented countries to remove clutter
    elif data_case == "total":
        small_countries = 0
        new_country_srs = pd.Series()
        percent_cutoff = 0.5
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

    new_srs = input_df.copy().set_index("UserID")["q35_Location"]

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

    country_srs = adjust_geo_data(country_srs, data_case, len(input_df))

    # make a pie chart
    labels = country_srs.index
    values = country_srs.values

    fig = go.Figure(data=[
        go.Pie(
            labels=labels, values=values, 
            textposition="inside",
            textinfo="label+percent"
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
