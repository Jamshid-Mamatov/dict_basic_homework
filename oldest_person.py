def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    
    max=0
    for key,val in people.items():
        if max<val:
            max=val
            name=key

    return name
