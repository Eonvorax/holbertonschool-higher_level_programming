#!/usr/bin/python3
"""
This is the 2-append_write module
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file.

    Args:
        filename (str): The name of the file to write in
        text (str): The text to append to the file

    Returns:
        The number of characters written to the file.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return (file.write(text))
