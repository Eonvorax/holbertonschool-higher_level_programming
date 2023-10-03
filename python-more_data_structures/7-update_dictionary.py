#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Update or add a key-value pair to a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key: The key to update or add.
        value: The value to associate with the key.

    Returns:
        The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
