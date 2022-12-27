def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    dict_res={}
    cities.sort()
    for k, v in zip(range(len(cities)),cities):

        dict_res[k]=v

    return dict_res

