from re import split

def is_in_binaries_list(input_str):
    """
    takes a string

    checks if the string contains any of the key words that were being caught 
    for the male & female categories

    if so returns True

    otherwise returns False
    """

    # making case insensitive
    lower_str = input_str.lower()

    for item in [ # if the item was caught in the male/female list 
        "girl","woman","lady","gal","female","chic","maiden",
        "mom","mum","miss","ms","daughter","sister","gxrl","wxman","womxn",

        "guy","dude","boy","boi","man","male","sir","lad","lord",
        "dad","mr","mister","son","bro","bloke","bxy","bruv",
    ]:
        if item in lower_str:
            return True
    
    if "ma" in lower_str and "am" in lower_str:
        return True
    
    return False

def caught_wrong_word(input_str:str, key_word, catch_word):
    """
    takes an input string that should contain the key word

    checks if input string contains catch word

    if so if the key word remains after removing the catch word

    if so it returns True

    otherwise it returns False
    """

    split_word = split(catch_word, input_str)
    for bit in split_word:
        if key_word in bit:
            return True
    return False

