def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    dict_res={}

    for k, v in zip(key,value):
        dict_res[k]=v
    return dict_res

key = [1, 2, 3] 
value = ["one", "two", "three"]
create_dictionary(key=key,value=value)