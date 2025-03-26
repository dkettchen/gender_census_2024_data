import pandas as pd
from visualisation.chart_bar import make_simple_bar

# total, grouped by source
    # group by labels
    # count to get totals
# make a bar chart? or pie chart? (if they're mutually exclusive)

# over time, adding up as time goes on -> can be only websites bc stuff like "my friend send it" 
# won't have anything to do w each other, unlike sharing on socials
    # add time stamp (we could do this before inputting into this func already, 
    # to reuse the read data later)
    # create running total of relevant labels
# make line chart
    # annotate bump from when it was posted on r/tumblr thingy bc those should be close together in time
    # if u want & it seems relevant/is look-up-able, annotate when it was mentionned on podcasts etc?

def make_source_charts(input_df:pd.DataFrame):
    
    folder = "visualisation/charts/survey_sources_"

    # total grouped by source
    # group by labels & count
    total_sources_srs = input_df.copy().groupby("origin").count()[
        "timestamp_for_sorting"
    ].sort_values(ascending=False)
    total_sources_srs = total_sources_srs.apply(lambda x: round((x/len(input_df))*100, 2))
    total_sources_srs = total_sources_srs.where(total_sources_srs > 1).dropna(how="all")
    # bar chart
    total_sources_fig = make_simple_bar(total_sources_srs, "sources")
    total_sources_fig.write_image(
        f"{folder}total.png",
        height=600,
        width=800,
    )

    # biggest categories over time
        # line chart


    pass