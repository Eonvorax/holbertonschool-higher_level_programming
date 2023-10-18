#!/usr/bin/python3
"""
This is the 1-write_file module
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return (file.write(text))
