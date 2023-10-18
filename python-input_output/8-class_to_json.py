#!/usr/bin/python3
"""
This is the 8-class_to_json module
"""


def class_to_json(obj):
    """
    Returns a dictionary description of a simple data structure
    (list, dictionary, string, integer and boolean)
    """
    return obj.__dict__
