#!/usr/bin/python3

"""
This is the 3-say_my_name module
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a string with the first and last name provided.

    Args:
        first_name (str): The first name to be printed.
        last_name (str): The last name to be printed.
            (defaults to an empty string)

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
