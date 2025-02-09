import pandas as pd
from visualisation.chart_pie import make_pie
from visualisation.chart_bar import make_simple_bar
from visualisation.chart_prep_dfs import count_df

def make_survey_source_charts(input_df:pd.DataFrame):

    source_df = input_df.copy()
    # adjust input df to be useable
        # how to categorise ones that have two listed?
        # read from cleaned files?? -> that have sorted the repeats
        # replace repeats with common label

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
