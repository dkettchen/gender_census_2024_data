import pandas as pd

def english_speaking(input_df:pd.DataFrame):
    """
    adds a column "english_or_no" with status of whether location is 
    english-speaking, non-english-speaking or unspecified

    returns a new df
    """
    input_df["english_or_no"] = None

    new_df = input_df.copy()

    # default due to most populous
    new_df["english_or_no"] = "english_speaking"
    # unspecified
    new_df["english_or_no"] = new_df["english_or_no"].mask(
        (
            new_df["q35_Location"] == 'Prefer not to say') | (
            new_df["q35_Location"] == "['country aggregated']") | (
            new_df["q35_Location"] == "None"
        ), 
        other="not_specified"
    )
    # non-english speakers
    new_df["english_or_no"] = new_df["english_or_no"].mask(
        (
            new_df["q35_Location"] != "United States") & (
            new_df["q35_Location"] != "United Kingdom") & (
            new_df["q35_Location"] != "Australia") & (
            new_df["q35_Location"] != "New Zealand") & (
            new_df["q35_Location"] != "Canada") & (
            new_df["q35_Location"] != "Ireland") & (
            new_df["english_or_no"] != "not_specified"
        ), 
        other="non_english_speaking"
    )

    return new_df

def other_countries(input_srs:pd.Series, total_len:int, percent_cutoff:float=0.5):
    """
    takes a series of float values and a total length, 
    as well as optionally a percent_cutoff (default 0.5)

    returns a new series where any values below the cutoff 
    have been summed up into one "Other countries (<{cutoff}%)" value
    """
    country_srs = input_srs.copy()

    small_countries_sum = country_srs.where(country_srs < 0.5).dropna(how="all").sum()
    big_countries_srs = country_srs.where(country_srs >= 0.5).dropna(how="all")

    big_countries_srs[f"Other countries (<{percent_cutoff}%)"] = small_countries_sum

    return big_countries_srs

# ref
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