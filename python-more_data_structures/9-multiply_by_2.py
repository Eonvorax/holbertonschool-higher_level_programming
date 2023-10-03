#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Args:
    - a_dictionary: a dictionary with integer values

    Returns:
    - a new dictionary with all values multiplied by 2
    """
    new_dict = {}
    # Also works but the loop implementation seems more readable :
    # new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
