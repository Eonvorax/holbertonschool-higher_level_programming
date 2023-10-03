#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the highest integer value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to search.

    Returns:
        The key with the highest integer value in the dictionary.
        If the dictionary is empty, returns None.
    """
    if not a_dictionary:
        return None

    max_value = 0
    max_key = None
    for key, value in a_dictionary.items():
        if max_value is None or value > max_value:
            max_value = value
            max_key = key

    return max_key
