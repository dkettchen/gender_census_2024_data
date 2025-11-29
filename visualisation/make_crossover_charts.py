import pandas as pd
from visualisation.chart_import_data import case_get_lists
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from visualisation.vis_utils_file import make_colour_list, make_alignment_srs
from visualisation.make_geo_charts import english_speaking_or_no
from visualisation.chart_pie import make_pie
from re import sub

# pronouns for transmascs, transfemmes, unspecified trans, unspecified cis-trans, & cis respondants
def make_pronouns_by_labels(input_df:pd.DataFrame, data_case:str):
    """
    makes multiplot pie chart of pronouns used by the following groups of respondants:

    -cis
    -transfemme
    -transmasc
    -unspecified cis/trans (do not use cis or trans)
    -unspecified trans (use trans but didn't specify direction)

    data_cases currently implemented: "pronouns", "aligned_pronouns"
    currently they work for tickbox labels
    """
    #TODO: add case to be able to reuse for write in data later

    new_df = input_df.copy()

    folder = "visualisation/charts/combo_data_"
    suffix = "(Gender Census 2024)"
    
    # groups we want:
    groups_we_want = {
        "is_transmasc_tickbox": "transmasc",
        "is_transfemme_tickbox": "transfemme",
        "conflicted_transmasc/transfem_tickbox": "unspecified_trans",
        "unspecified_transmasc/transfem_tickbox": "unspecified_trans",

        "is_cis_tickbox": "cis",
        "conflicted_cis/trans_tickbox": "unspecified_cis_trans",
        "unspecified_cis/trans_tickbox": "unspecified_cis_trans",
    }

    # make a column of groups we want
    new_df["trans_status"] = None
    for group in groups_we_want:
        new_df["trans_status"] = new_df["trans_status"].mask(
            new_df[group] == "Yes", other=groups_we_want[group]
        )

    # get that column & relevant pronoun columns
    get_list = ["trans_status"] + case_get_lists["pronoun_pie"]

    # get, group by group column & count
    new_df = new_df.get(get_list).groupby(by="trans_status").count().transpose()
    #print(new_df)


    # make subplots
    fig = make_subplots(rows=2, cols=3, specs=[
        [{'type':'domain'}, {'type':'domain'}, {'type':'domain'}],
        [{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]
    ])

    # add pies for each column
    row = 1
    col = 1
    for column in new_df.columns:
        current_column_srs = new_df[column].sort_values()
        
        if data_case == "aligned_pronouns": # making aligments & colour_case
            current_column_srs = make_alignment_srs(current_column_srs, "pronouns")
            colour_case = "alignments"
        elif data_case == "pronouns": # colour_case
            colour_case = "pronouns"
        colours = make_colour_list(current_column_srs.index, colour_case)
        
        if "unspecified" in column:
            column = sub("_", "/", column) # turning cis_trans into cis/trans
            group_title = column[:11] + "<br>" + column[12:] # breaking & ommitting _ in the middle
        else: group_title = column
        
        fig.add_trace(
            go.Pie(
                labels=current_column_srs.index, 
                values=current_column_srs.values, 
                hole=.4,
                title=group_title,
                marker_colors=colours,
                textinfo="text+label", textposition="inside",
                titlefont_size = 15
            ), row, col
        )

        # incrementing
        if col == 3:
            col = 1
            row += 1
        else:
            col += 1

    fig.update_layout(
        title_text=f"Pronouns by label category {suffix}",
        uniformtext_minsize=10, 
        uniformtext_mode="hide",
        showlegend=False,
    )

    # making file_title
    if data_case == "pronouns":
        file_title = "pronouns_by_tickbox_labels"
    elif data_case == "aligned_pronouns":
        file_title = "pronoun_alignment_by_tickbox_labels"

    fig.write_image(
        f"{folder}{file_title}.png",
        height=900,
        width=1300,
    )


# labels per survey origin - ie one for tumblr, one for reddit, etc 
# -> to demonstrate birthsex bias among other things


# identities per country
    # english speaking countries vs non-english speaking countries, bc we're asking abt english language

# pronouns -> apparently not significantly different, 
# cause ppl were good & followed the brief of "in english" huh
def make_non_english_pronouns(pronoun_df:pd.DataFrame, country_df:pd.DataFrame):

    language_df = english_speaking_or_no(country_df)

    english_pronoun_df = pronoun_df.set_index("UserID").join(language_df, lsuffix="left", rsuffix="right")

    get_list = ["english_or_no"] + case_get_lists["pronoun_pie"]
    new_df = english_pronoun_df.get(get_list).groupby(by="english_or_no").count().transpose()
    
    for column in new_df.columns:
        total_len = new_df[column].agg("sum")
        new_df[column] = new_df[column].apply(lambda x: round((x/total_len)*100, 2))

    fig = make_pie(new_df["non_english_speaking"], "pronoun_pie_non_en")

    folder = "visualisation/charts/"
    file_title = "pronoun_pie_non_en"

    fig.write_image(
        f"{folder}{file_title}.png",
        height=900,
        width=1300,
    )