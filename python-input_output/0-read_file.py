#!/usr/bin/python3
"""
This is the 0-read_file module
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The path to the file to be read.
    """
    with open(filename, mode="r", encoding="UTF-8") as file:
        for line in file:
            print(line, end='')
