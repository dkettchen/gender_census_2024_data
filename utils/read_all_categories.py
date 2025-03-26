from json import load
from os import listdir

def read_all_categories(folder:str):
    """
    reads from all json files in given folder (should end in "/")

    returns a dict with the file names as the keys and the contents as the list value
    """

    all_file_names = listdir(folder)

    data_dict = {}

    for item in all_file_names:
        if item[-5:] != ".json":
            continue
        filepath = f"{folder}{item}"
        with open(filepath, "r") as json_file:
            read_file = load(json_file)
        
        data_dict[item[:-5]] = read_file

    return data_dict