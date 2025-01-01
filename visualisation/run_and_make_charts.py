from utils.csv_reader import df_from_csv
from visualisation.make_pronoun_charts import make_pronoun_charts

# pronouns
pronoun_df = df_from_csv("data/cleaned_q9_with_new_columns/q9_clean_01.csv")
make_pronoun_charts(pronoun_df)