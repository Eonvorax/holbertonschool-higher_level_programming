#!/usr/bin/python3
"""
This is the 6-load_from_json_file module
"""

import json


def load_from_json_file(filename):
    """
    Load JSON data from a file and return a Python object.

    Args:
        filename (str): The name of the file to load from.

    Returns:
        A Python object representing the JSON data in the file.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.loads(file.read())
