#!/usr/bin/python3

"""
This is the module 4-inherits_from
"""


def inherits_from(obj, a_class):
    """
    Determines if an object is an instance of a subclass of a_class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
        False otherwise.
    """
    return (type(obj) is not a_class and isinstance(obj, a_class))
