import pandas as pd

def subset(input_df:pd.DataFrame, column:str, yes:bool=True):
    """
    returns requested subset of input_df 
    (where column == "Yes" if yes=True, else column != "Yes") 
    as a new df
    """
    if yes:
        return input_df.copy().where(input_df[column] == "Yes")
    else:
        return input_df.copy().where(input_df[column] != "Yes")
