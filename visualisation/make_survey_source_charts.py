import pandas as pd
from visualisation.chart_bar import make_simple_bar

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
        # (optional, my point of "anything other than tumblr is severely underrepresented" 
        # has already been proven by total)
