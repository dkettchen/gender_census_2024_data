import pandas as pd

def read_data_from_excel(filepath:str):
    """
    takes a filepath

    reads from a double header excel file

    returns a df with its data
    """
    df = pd.read_excel(filepath, header=[0,1])
    return df