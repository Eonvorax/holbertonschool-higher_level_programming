#!/usr/bin/python3
"""
This is the 0-lookup module
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of strings representing the available attributes
        and methods of the object.
    """
    return dir(obj)
