def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    max=people["Javohir"]
    name='Javohir'
    for key,val in people.items():
        if max<val:
            max=val
            name=key

    return name

people = {"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16}
oldest(people=people)