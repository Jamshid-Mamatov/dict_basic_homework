def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    dict_res={}
    count_letter=0
    count_digit=0
    for i in txt:
        if i.isdigit():
            count_digit+=1
        if i.isalpha():           
            count_letter+=1
    dict_res['LETTERS']=count_letter
    dict_res['DIGITS']=count_digit
    return dict_res
