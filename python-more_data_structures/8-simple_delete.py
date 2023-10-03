#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key from a dictionary.

    Args:
        a_dictionary (dict): The dictionary to delete the key from.
        key (str): The key to delete from the dictionary.

    Returns:
        dict: The updated dictionary (unchanged if the key was not found)
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
