from utils.csv_reader import df_from_csv
from visualisation.make_pronoun_charts import make_pronoun_charts
from visualisation.make_label_tickbox_charts import make_label_tickbox_charts
from visualisation.make_crossover_charts import make_pronouns_by_labels
from visualisation.make_geo_charts import make_geo_charts

# # pronouns
# pronoun_df = df_from_csv("data/cleaned_q9_with_new_columns/q9_clean_01.csv")
# make_pronoun_charts(pronoun_df)

# # tickbox labels
# tickbox_label_df = df_from_csv("data/cleaned_q1_with_new_columns/q1_clean_01.csv")
# make_label_tickbox_charts(tickbox_label_df)

# # pronouns x tickboxes
# pronouns_x_labels = pronoun_df.join(tickbox_label_df, lsuffix="left", rsuffix="right")
# make_pronouns_by_labels(pronouns_x_labels, "pronouns")
# make_pronouns_by_labels(pronouns_x_labels, "aligned_pronouns")

# countries
geo_df = df_from_csv("data/separated_questions/q35_location.csv")
make_geo_charts(geo_df, "total")
make_geo_charts(geo_df, "english_speaking_countries")