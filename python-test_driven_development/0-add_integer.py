#!/usr/bin/python3
"""
This is the 0-add_integer module

This module contains the add_integer function
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int): integer a
        b (int): integer b

    Raises:
        TypeError exception if a or b are not integers or floats

    Returns:
        The sum of a and b

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
