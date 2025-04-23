from csv import reader
from re import split
from string import digits
import pandas as pd

# copied from ship data utils

def read_data_from_csv(filepath: str):
    """
    takes a filepath to a csv file
    
    returns a nested list of its contents, 
    with all useable lists and integers 
    converted back into the correct file type 
    (remaining values are strings)
    """
    with open(filepath, "r", newline="") as csv_file:
        read_data = reader(csv_file) # normal quote char for now, not quotechar="`"
        data_list = [row for row in read_data] #turns it into a list of lists of string values
        
    output_list = []
    for row in data_list:
        new_row = []
        for item in row:
            if len(item) == 0:
                continue
            if item[0] == "[": # if it's supposed to be a list
                split_item = split(r",\s", item) #splitting at commas
                split_item[0] = split_item[0][1:] #removing opening [
                split_item[-1] = split_item[-1][:-1] #removing closing ]
                new_item = []
                for bit in split_item:
                    if bit[0] == "'":
                        new_bit = bit[1:-1]
                    elif bit == "None":
                        new_bit = None
                    elif bit == "":
                        continue
                    elif bit.isdigit():
                        new_bit = int(bit)
                    else: new_bit = bit
                    new_item.append(new_bit)
                #     print(type(new_bit), new_bit)
                # print(row, new_row, filepath)


                # split_item = split(r"'", item)
                # new_item = [bit for bit in split_item if bit not in ["[", "]", ", "]]
                #     # we're turning it back into a list
            elif item == "None": #if it's supposed to be a none value
                new_item = None
            else:
                is_integer = True
                if item == ".":
                    is_integer = False # it's not a useable number
                    break
                for char in item:
                    if char not in digits and char != ".": # if any character is not a number or a decimal point
                        is_integer = False # it's not a useable number
                        break
                if is_integer:
                    if item[-2:] == ".0":
                        item = item[:-2]
                    elif "." in item:
                        print(row)
                    new_item = int(item) # if it's a useable number, we turn it into one
                else: new_item = item # otherwise the string is fine

            #we may add other type cases as need be later if relevant
            
            new_row.append(new_item)
        output_list.append(new_row)
    return output_list

def df_from_csv(filepath:str):
    """
    reads from filepath (must be csv file) (using read_data_from_csv util function)

    returns a df with the data contained, using the first row as its column titles
    """
    csv_data = read_data_from_csv(filepath)
    df = pd.DataFrame(csv_data[1:], columns=csv_data[0])
    return df
