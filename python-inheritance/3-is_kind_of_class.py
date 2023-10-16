#!/usr/bin/python3

"""
This is the module 3-is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise returns False.

    Args:
        obj (object): The object to check.
        a_class (class): The class or type to check against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
