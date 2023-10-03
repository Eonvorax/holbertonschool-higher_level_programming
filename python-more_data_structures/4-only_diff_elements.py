#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Returns a set containing only elements that are unique to each input set.

    Args:
    - set_1: the first input set
    - set_2: the second input set

    Returns:
    A set containing only the elements that are unique to each input set.
    """
    return set_1 ^ set_2
