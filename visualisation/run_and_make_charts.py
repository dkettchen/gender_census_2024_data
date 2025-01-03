from utils.csv_reader import df_from_csv
from visualisation.make_pronoun_charts import make_pronoun_charts
from visualisation.make_label_tickbox_charts import make_label_tickbox_charts

# pronouns
pronoun_df = df_from_csv("data/cleaned_q9_with_new_columns/q9_clean_01.csv")
make_pronoun_charts(pronoun_df)

# tickbox labels
tickbox_label_df = df_from_csv("data/cleaned_q1_with_new_columns/q1_clean_01.csv")
make_label_tickbox_charts(tickbox_label_df)