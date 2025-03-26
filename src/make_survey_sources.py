import pandas as pd
from json import load
from utils.csv_reader import df_from_csv
from utils.read_all_categories import read_all_categories

# TODO:
    # lgbt category (and several others) currently contain items that are already covered 
    # by other categories -> fix in og sorting code please
        # -make separate category for lgbtqia fandom wiki bc it was mentionned multiple times
        # -remove any other website mentions we already have categories for
        # -remove word of mouth from queer loved ones mentions too
        # -keep prides & unspecified groups basically
    # -check other categories for doubles smh

file_names_websites = {
    "ai": "AI",
    "anime feminist": "Anime Feminist (website)",
    "bluesky": "Bluesky (social media)",
    "cohost": "Cohost (social media)",
    "discord": "Discord (messenger/social media)",
    "dreamwidth": "Dreamwidth (social media)",
    "eunuch": "Eunuch Archive (forum/social media)",
    "facebook": "Facebook (social media)",
    "fetlife" : "FetLife (BDSM social media)",
    "forum": "any other Forum",
    "gender census": "Gender Census",
    "gender reveal": "Tuck Woodstock's Gender Reveal (podcast)",
    "goodreads": "Goodreads (book website)",
    "insta": "Instagram (social media)",
    "irc": "IRC (messenger)",
    "lemmy": "Lemmy (forum/social media)",
    "lex": "Lex (queer dating app)",
    "limonnur": "Limonnur (forum??)",
    "linkedin": "LinkedIn (social media)",
    "mastodon": "Fediverse (Mastodon, etc) (social media)",
    "matrix": "Matrix (software??)",
    "melonland": "MelonLand (forum)",
    "neocities": "Neocities (website hosting)",
    "nonbinary wiki": "Nonbinary Wiki (wiki website)",
    "patreon": "Patreon (crowdfunding website)",
    "pillowfort": "Pillowfort (social media)",
    "pinterest": "Pinterest (social media)",
    "pronouns page": "Pronoun Page (website)",
    "quotev": "Quotev (poll website)",
    "reddit": "Reddit (social media)",
    "scratch": "Scratch (website)",
    "signal": "Signal (messenger)",
    "slack": "Slack (messenger)",
    "snapchat": "Snapchat (messenger)",
    "spacehey": "Spacehey (social media)",
    "substack": "Substack (newsletter website)",
    "t4t": "T4T (dating app/social media)",
    "teams": "Teams (messenger)",
    "telegram": "IM group (Telegram, WhatsApp, etc) (messenger)",
    "threads": "Threads (social media)",
    "tiktok": "TikTok (social media)",
    "tumblr": "Tumblr (social media)",
    "twitch": "Twitch (live-streaming website)",
    "twitter": "Twitter (social media)",
    "wattpad": "Wattpad (writing-publishing/fanfic website)",
    "whatsapp": "IM group (Telegram, WhatsApp, etc) (messenger)",
    "wikipedia": "Wikipedia (wiki website)",
    "yikyak": "Yik Yak (social media)",
    "youtube": "YouTube (social media)",
    "duckduckgo": "DuckDuckGo (search engine)",
    "google": "Google (search engine)"
}
file_names_word_of_mouth = [
    "word of mouth",
    "clinician",
    "family",
    "friend",
    "partner",
]
file_names_locations = {
    "lgbt": "LGBT+ group/etc",
    "school": "School/Uni",
    "work": "Work",
}

def make_survey_source_charts(input_df:pd.DataFrame):

    # get sorted bits from files
    data_dict = read_all_categories("data/cleaned_q37_write_ins/")

    # copying input df
    source_df = input_df.copy().set_index("UserID")#["q37_Survey_Origin"]

    source_df["origin"] = "Other"

    # websites first
    for key in file_names_websites:
        for item in data_dict[key]:
            source_df["origin"] = source_df["origin"].mask(
                (source_df["origin"] == "Other") & (
                source_df["q37_Survey_Origin"] == item),
                other=file_names_websites[key]
            )
            source_df["origin"] = source_df["origin"].mask(
                (source_df["origin"] != file_names_websites[key]) & (
                source_df["q37_Survey_Origin"] == item),
                other=source_df["origin"] + f" & {file_names_websites[key]}"
            )
    
    # offline locations second
    for key in file_names_locations:
        for item in data_dict[key]:
            source_df["origin"] = source_df["origin"].mask(
                (source_df["origin"] == "Other") & (
                source_df["q37_Survey_Origin"] == item),
                other=file_names_locations[key]
            )
            source_df["origin"] = source_df["origin"].mask(
                (source_df["origin"] != file_names_locations[key]) & (
                source_df["q37_Survey_Origin"] == item),
                other=source_df["origin"] + f" & {file_names_locations[key]}"
            )

    for key in file_names_word_of_mouth:
        for item in data_dict[key]:
            source_df["origin"] = source_df["origin"].mask(
                (source_df["origin"] == "Other") & (
                source_df["q37_Survey_Origin"] == item),
                other="Word of Mouth"
            )
    
    #print(source_df.tail(40))
    return source_df


if __name__ == "__main__":
    source_df = df_from_csv("data/separated_questions/q37_how_did_you_find_survey.csv")

    new_df = make_survey_source_charts(source_df)

    new_df.to_csv(path_or_buf="data/cleaned_q37_with_new_columns/q37_clean_01.csv")
