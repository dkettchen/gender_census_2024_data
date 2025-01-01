import pandas as pd

# check just tick boxes first?
def make_tickbox_columns(input_df:pd.DataFrame):

    # rename existing tick boxes

    # replace trans/transgender columns w a general is trans 
    # (if trans/transgender/transmasc/transfemme (and not cisgender) = is trans)

    # clean transmasc & transfemme columns
    # transmasc unless transfemme, or demigirl without demiboy
    # transfemme unless transmasc, or demiboy without demigirl

    # add a column of "ppl who don't understand that transmasc/transfemme are directions, 
    # not abt expression or alignment smh and claim both"

    # add only demigirl (unless transmasc), only demiboy (unless transfemme), 
    # and demigirl & demiboy columns

    # is nonbinary (enby/nonbinary (and not binary))
    # uses nb umbrella label (is nb, agender, bigender, gender fluid (and not binary))

    # add afab/amab/unspecified birthsex columns for tickboxes
        # afab:
            # transmasculine
            # trans demiboy
            # cis demigirl
            # cis butch
        # amab:
            # transfeminine
            # trans demigirl
            # cis demiboy
            # cis fag
    pass

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