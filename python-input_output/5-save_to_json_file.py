#!/usr/bin/python3
"""
This is the 5-save_to_json_file module
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write the JSON representation of an object to a file.

    Args:
        my_obj (object): The object to be written to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
