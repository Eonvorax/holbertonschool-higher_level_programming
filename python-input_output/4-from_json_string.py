#!/usr/bin/python3
"""
This is the 4-from_json_string module
"""

import json


def from_json_string(my_str):
    """
    Returns an Python object represented by the given JSON string.

    Args:
        my_str (str): A JSON string.

    Returns:
        The Python object represented by the JSON string.

    """
    return json.loads(my_str)
