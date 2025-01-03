import pandas as pd
from utils.csv_reader import df_from_csv

# check just tick boxes first?
def make_tickbox_columns(input_df:pd.DataFrame):
    """
    takes input_df with raw question 1 data

    returns a new df with updated columns
    """

    # rename existing tick boxes

    # creating renaming dict
    column_list = list(input_df.columns)
    renaming_dict = {}
    for item in column_list:
        if item == "UserID":
            continue

        if "q1" in item:
            new_item = item[3:]
        
        # simplifying non-simple column
        if "a person" in new_item:
            new_item = "a person/human/[my name]/just me"
        elif "I do not describe myself" in new_item:
            new_item = "no self-description"
        elif "fluid" in new_item:
            new_item = "genderfluid"
        elif new_item == "queer (in relation to gender)":
            new_item = "queer"
        elif "questioning" in new_item:
            new_item = "questioning/unknown"
        
        # marking as tickbox columns
        renaming_dict[item] = new_item + "_tickbox"

    # renaming new df
    new_df = input_df.copy().reset_index().rename(columns=renaming_dict)


    # adding mutually exclusive, conflicted & unspecified columns

    # adding is_trans tickbox column combining trans & transgender & transmasc/transfemme columns
        # if (any of those columns) and not (cis column) -> is trans
    new_df["is_trans_tickbox"] = "Yes"
    new_df["is_trans_tickbox"] = new_df["is_trans_tickbox"].where(
        (
            (new_df["trans_tickbox"] == "Yes") | (
            new_df["transgender_tickbox"] == "Yes") | (
            new_df["transmasculine_tickbox"] == "Yes") | (
            new_df["transfeminine_tickbox"] == "Yes")
        ) & (
            new_df["cisgender_tickbox"] != "Yes"
        ) 
    )
    # adding is_cis tickbox column
        # if cis and not trans/transgender -> is cis
    new_df["is_cis_tickbox"] = "Yes"
    new_df["is_cis_tickbox"] = new_df["is_cis_tickbox"].where(
        (
            (new_df["trans_tickbox"] != "Yes") | (
            new_df["transgender_tickbox"] != "Yes") | (
            new_df["transmasculine_tickbox"] != "Yes") | (
            new_df["transfeminine_tickbox"] != "Yes")
        ) & (
            new_df["cisgender_tickbox"] == "Yes"
        ) 
    )
    # adding conflicted cis/trans column
        # if cis and trans/transgender -> is conflicted cis/trans
    new_df["conflicted_cis/trans_tickbox"] = "Yes"
    new_df["conflicted_cis/trans_tickbox"] = new_df["conflicted_cis/trans_tickbox"].where(
        (
            (new_df["trans_tickbox"] == "Yes") | (
            new_df["transgender_tickbox"] == "Yes") | (
            new_df["transmasculine_tickbox"] == "Yes") | (
            new_df["transfeminine_tickbox"] == "Yes")
        ) & (
            new_df["cisgender_tickbox"] == "Yes"
        ) 
    )
    # adding unspecified cis/trans column
        # if not cis and not trans/transgedner -> is unspecified cis/trans
    new_df["unspecified_cis/trans_tickbox"] = "Yes"
    new_df["unspecified_cis/trans_tickbox"] = new_df["unspecified_cis/trans_tickbox"].where(
        (new_df["trans_tickbox"] != "Yes") & (
        new_df["transgender_tickbox"] != "Yes") & (
        new_df["transmasculine_tickbox"] != "Yes") & (
        new_df["transfeminine_tickbox"] != "Yes") & (
        new_df["cisgender_tickbox"] != "Yes") 
    )

    # only demigirl/only demiboy/both demigirl & demiboy (not cross referencing transmasc/-fem)
    new_df["is_only_demigirl_tickbox"] = "Yes"
    new_df["is_only_demigirl_tickbox"] = new_df["is_only_demigirl_tickbox"].where(
        (new_df["demigirl_tickbox"] == "Yes") & (
        new_df["demiboy_tickbox"] != "Yes")
    )
    new_df["is_only_demiboy_tickbox"] = "Yes"
    new_df["is_only_demiboy_tickbox"] = new_df["is_only_demiboy_tickbox"].where(
        (new_df["demigirl_tickbox"] != "Yes") & (
        new_df["demiboy_tickbox"] == "Yes")
    )
    new_df["conflicted_demigirl/demiboy_tickbox"] = "Yes"
    new_df["conflicted_demigirl/demiboy_tickbox"] = new_df["conflicted_demigirl/demiboy_tickbox"].where(
        (new_df["demigirl_tickbox"] == "Yes") & (new_df["demiboy_tickbox"] == "Yes")
    )

    # clean transmasc/transfemme columns:
    # if not transfemme, and not (only demigirl) -> is transmasc
    new_df["is_transmasc_tickbox"] = "Yes"
    new_df["is_transmasc_tickbox"] = new_df["is_transmasc_tickbox"].where(
        (new_df["transmasculine_tickbox"] == "Yes") & (
        new_df["transfeminine_tickbox"] != "Yes") & (
        new_df["is_only_demigirl_tickbox"] != "Yes")
    )
    # if not transmasc, and not (only demiboy) -> is transfemme
    new_df["is_transfemme_tickbox"] = "Yes"
    new_df["is_transfemme_tickbox"] = new_df["is_transfemme_tickbox"].where(
        (new_df["transfeminine_tickbox"] == "Yes") & (
        new_df["transmasculine_tickbox"] != "Yes") & (
        new_df["is_only_demiboy_tickbox"] != "Yes")
    )
    # add a column of "ppl who don't understand that transmasc/transfemme are directions, 
    # not abt expression or alignment smh and claim both"
        # if transmasc & transfemme, or transmasc & only demigirl, or transfemme & only demiboy 
        # -> conflicted transmasc/transfem
    new_df["conflicted_transmasc/transfem_tickbox"] = "Yes"
    new_df["conflicted_transmasc/transfem_tickbox"] = new_df["conflicted_transmasc/transfem_tickbox"].where(
        ((new_df["transmasculine_tickbox"] == "Yes") & ( # transmasc & transfemme
        new_df["transfeminine_tickbox"] == "Yes")) | (
        (new_df["transmasculine_tickbox"] == "Yes") & ( # transmasc & only demigirl
        new_df["is_only_demigirl_tickbox"] == "Yes")) | (
        (new_df["transfeminine_tickbox"] == "Yes") & ( # transfem & only demiboy
        new_df["is_only_demiboy_tickbox"] == "Yes"))
    )
    # if is_trans, but not specified transmasc/transfemme -> is trans unspecified transmasc/transfem
    new_df["unspecified_transmasc/transfem_tickbox"] = "Yes"
    new_df["unspecified_transmasc/transfem_tickbox"] = new_df["unspecified_transmasc/transfem_tickbox"].where(
        (new_df["is_trans_tickbox"] == "Yes") & ( # it has qualified by having trans or transgender
            (new_df["transmasculine_tickbox"] != "Yes") & ( # but does not contain transmasc
            new_df["transfeminine_tickbox"] != "Yes") # or transfemme specification
        )
    )

    # only butch, only fag, both butch & fag
    new_df["is_only_butch_tickbox"] = "Yes"
    new_df["is_only_butch_tickbox"] = new_df["is_only_butch_tickbox"].where(
        (new_df["butch_tickbox"] == "Yes") & (
        new_df["fag_tickbox"] != "Yes")
    )
    new_df["is_only_fag_tickbox"] = "Yes"
    new_df["is_only_fag_tickbox"] = new_df["is_only_fag_tickbox"].where(
        (new_df["butch_tickbox"] != "Yes") & (
        new_df["fag_tickbox"] == "Yes")
    )
    new_df["conflicted_fag/butch_tickbox"] = "Yes"
    new_df["conflicted_fag/butch_tickbox"] = new_df["conflicted_fag/butch_tickbox"].where(
        (new_df["butch_tickbox"] == "Yes") & (new_df["fag_tickbox"] == "Yes")
    )

    # adding is_nb tickbox column combining nonbinary & enby columns
    # if (either of those columns) -> is nb
    new_df["is_nb_tickbox"] = "Yes"
    new_df["is_nb_tickbox"] = new_df["is_nb_tickbox"].where(
        (new_df["nonbinary_tickbox"] == "Yes") | (
        new_df["enby_tickbox"] == "Yes")
    )
    # adding is_nb_umbrella tickbox column
    # if nb, agender, bigender, gender fluid -> is nb umbrella
    new_df["is_nb_umbrella_tickbox"] = "Yes"
    new_df["is_nb_umbrella_tickbox"] = new_df["is_nb_umbrella_tickbox"].where(
        (new_df["is_nb_tickbox"] == "Yes") | (
        new_df["agender_tickbox"] == "Yes") | (
        new_df["bigender_tickbox"] == "Yes") | (
        new_df["genderfluid_tickbox"] == "Yes")
    )
    # adding binary nbs columns
    # if nb/enby + binary -> nb binary
    new_df["is_binary_nb_tickbox"] = "Yes"
    new_df["is_binary_nb_tickbox"] = new_df["is_binary_nb_tickbox"].where(
        (new_df["is_nb_tickbox"] == "Yes") & (new_df["binary_tickbox"] == "Yes")
    )
    # if nb, agender, bigender, gender fluid + binary -> nb umbrella binary
    new_df["is_binary_nb_umbrella_tickbox"] = "Yes"
    new_df["is_binary_nb_umbrella_tickbox"] = new_df["is_binary_nb_umbrella_tickbox"].where(
        (new_df["is_nb_umbrella_tickbox"] == "Yes") & (new_df["binary_tickbox"] == "Yes")
    )

    # add tickbox specified afab/amab/unspecified birthsex columns
    # auto disqualified if conflicted cis/trans or transmasc/transfemme
    # afab if transmasc, trans only demiboy, cis only demigirl, cis only butch
    new_df["is_afab_tickbox"] = "Yes"
    new_df["is_afab_tickbox"] = new_df["is_afab_tickbox"].where(
        (
            (new_df["conflicted_cis/trans_tickbox"] != "Yes") & (
            new_df["conflicted_transmasc/transfem_tickbox"] != "Yes")
        ) & (
            (
                (new_df["is_transmasc_tickbox"] == "Yes") # all transmascs
            ) | (
                (new_df["unspecified_transmasc/transfem_tickbox"] == "Yes") & (
                new_df["is_only_demiboy_tickbox"] == "Yes") # all remaining trans demiboys
            ) | (
                (new_df["is_cis_tickbox"] == "Yes") & ( # all cis demigirls
                new_df["is_only_demigirl_tickbox"] == "Yes")
            ) | (
                (new_df["is_cis_tickbox"] == "Yes") & ( # all cis butches
                new_df["is_only_butch_tickbox"] == "Yes") 
            )
        )
    )
    # amab if transfem, trans only demigirl, cis only demiboy, cis only fag
    new_df["is_amab_tickbox"] = "Yes"
    new_df["is_amab_tickbox"] = new_df["is_amab_tickbox"].where(
        (
            (new_df["conflicted_cis/trans_tickbox"] != "Yes") & (
            new_df["conflicted_transmasc/transfem_tickbox"] != "Yes")
        ) & (
            (
                (new_df["is_transfemme_tickbox"] == "Yes") # all transfemmes
            ) | (
                (new_df["unspecified_transmasc/transfem_tickbox"] == "Yes") & (
                new_df["is_only_demigirl_tickbox"] == "Yes") # all remaining trans demigirls
            ) | (
                (new_df["is_cis_tickbox"] == "Yes") & ( # all cis demiboys
                new_df["is_only_demiboy_tickbox"] == "Yes")
            ) | (
                (new_df["is_cis_tickbox"] == "Yes") & ( # all cis fags
                new_df["is_only_fag_tickbox"] == "Yes") 
            )
        )
    )

    new_df = new_df.set_index("UserID").fillna("None")
    new_df.pop("index")
    

    return new_df

# write ins separately
def make_write_in_columns(input_df:pd.DataFrame):
    
    # shorten df to only ppl who did write things in (ie dropna)
        # so we only check for percent *of* ppl who wrote stuff in
    
    # make column for everyone in this shorter df to denote they did write stuff in

    # go through various categories, make columns for em
        # read from files (maybe a helper func to read em all and put em in a dict or smth)
    # implement a way to check all write in columns effectively re if they're in xyz list

    # drop original write in columns

    # check for column combos to add to various columns 
    # (ex cross referencing to find more cis/aligned trans ppl, etc)
    pass

# join dfs & cross reference write ins for tick box labels for combo info
def combine_info(tick_box_df, write_in_df):
    pass



# columns
# - use helper to check if stuff is in lists
    # - make helper ✅
# - make straight up count columns first
# - figure out best order for making cross referenced columns
# - count no of write ins before removing og columns


# things to check for:
# - write ins vs no write ins
# - average no of write ins per person (total and write ins only)
# - box label counts ticked (by write ins vs no write ins vs total)
# - tick box label numbers alone vs plus write in additions
# - total trans no vs not trans no (incl write ins)
# - how likely trans ppl were to write in
# - repeat for other tick box labels (bc obv all write in dependant labels like intersex or dyke will be 100%)
# - what not trans no IDs as (of tick box labels, of write in labels)
# - what trans no IDs as (ditto)
# - what nb ppl ID as
# - what non nb ppl ID as
# - what ppl of x label were most likely to also ID as (eg top 5-10 labels per each or smth)
# - all write in category numbers (per write ins, per total unless there's such few write ins)
# - birthsexes (discernable by tick boxes, of write ins, discernable by write ins + tick boxes)
# - what each birthsex was most likely to also ID as
# - alignements (ditto)
# - queer labels ditto?
# - distribution of: transmasc, transfemme, intersex transmasc, intersex transfemme, 
# intersex unspec/nontrans male, intersex unspec/nontrans female, intersex unspecified, 
# cis male, cis female, amab unspec, afab unspec, fully unspecified 
# (of write ins alone, vs with tick boxes)

if __name__ == "__main__":
    read_tickbox_data = df_from_csv("data/separated_questions/q1_label_tick_boxes.csv")

    # running full file
    new_df = make_tickbox_columns(read_tickbox_data)

    # # running partial file
    # new_df = make_tickbox_columns(read_tickbox_data.head(100))

    new_df.to_csv(path_or_buf="data/cleaned_q1_with_new_columns/q1_clean_01.csv")