#!/usr/bin/python3
"""
This is the 4-print_square module
"""


def print_square(size):
    """
    Prints a square of a given size using the '#' character.

    Args:
        size (int): The size of the square to be printed.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for line in range(0, size):
        print("#" * size)
