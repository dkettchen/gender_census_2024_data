from re import split

def read_txt(data_case:str):
    """
    reads the relevant raw txt file for the unique values of the question in case

    returns a list of the separated out items from that file (minus question name, 
    trailing/leading white spaces, and any outside brackets)
    """
    # get file path
    data_case = data_case.lower()
    if data_case == "q2": # custom/unlisted words/phrases/labels
        filepath = "q2.txt"
    elif data_case == "q4_1": # a title not listed here (abbr)
        filepath = "q4_abbr.txt"
    elif data_case == "q4_2": # a title not listed here (full)
        filepath = "q4_full.txt"
    elif data_case == "q4_3": # a title not listed here (pronunciation)
        filepath = "q4_pronunciation.txt"
    elif data_case == "q8": # title not listed that u want ppl to use
        filepath = "q8.txt"
    elif data_case == "q35": # custom family mess
        filepath = "q35_1.txt"
    elif data_case == "q37": # how did u find this survey
        filepath = "q37.txt"

    # ease of changing folder
    folder = "data/raw_data/unique_values/"
    filepath = folder + filepath

    # read from file
    with open(filepath, "r") as txt_file:
        read_data = txt_file.read()
    
    # split rows
    split_strings = split(r"\n", read_data)

    shortened_list = []
    for item in split_strings:
        # leaving out any unneeded rows
        if len(item) == 0 or item[-1] in ["[", "]"] or item[:2] == "(Q":
            # there shouldn't be any actual values starting in "(Q", I checked via a print)
            continue
        
        new_item = item.strip() # removing trailing & leading white spaces
        # removing quotes & commas
        if new_item[0] in ["'", '"']:
            new_item = new_item[1:]
        if new_item[-1] == ",":
            new_item = new_item[:-1]
        if new_item[-1] in ["'", '"']:
            new_item = new_item[:-1]
        if (new_item[0] == "'" and new_item[-1] == "'" and "'" not in new_item[1:-1]) \
        or (new_item[0] == '"' and new_item[-1] == '"' and '"' not in new_item[1:-1]):
            new_item = new_item[1:-1]
        
        # append to list
        shortened_list.append(new_item)

    return sorted(list(set(shortened_list)))