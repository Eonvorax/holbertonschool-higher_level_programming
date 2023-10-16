#!/usr/bin/python3

"""
This is the module 2-is_same_class

This module contains a function that checks if an object is exactly
of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class,
    otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of the specified class,
        otherwise False.
    """
    return (type(obj) is a_class)
