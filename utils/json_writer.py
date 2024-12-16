from json import dump

def write_json_files(data_dict, folder_name):
    """
    takes a dictionary of file name keys (without suffix) and list values to be printed
    and a folder name (ending in "/")

    writes the data on the keys to files in the given folder, 
    with the corresponding file name from the key
    """

    for key in data_dict:
        file_path = f"{folder_name}{key}.json"
        data = data_dict[key]

        with open(file_path, "w") as new_file:
            dump(data, new_file, indent=4)