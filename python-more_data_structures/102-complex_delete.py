#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to delete keys from.
        value: The value to search for in the dictionary.

    Returns:
        The modified dictionary with the specified keys removed.
    """
    if not a_dictionary or not value:
        return a_dictionary

    # Creating a list of the keys to delete
    keys_to_delete = []
    # Going through the dictionary
    for key, val in a_dictionary.items():
        if val == value:
            # Found key to delete later, adding it to the list
            keys_to_delete.append(key)

    # Deleting all keys on the deletion list
    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
