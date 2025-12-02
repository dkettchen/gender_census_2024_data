def percent(num:float|int, length:int):
    """
    returns given number as percent of given length
    """
    return round((num / length) * 100, 2)