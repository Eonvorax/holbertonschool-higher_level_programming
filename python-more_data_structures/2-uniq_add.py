#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Returns the sum of all unique elements in a list.

    Args:
    - my_list: a list of integers

    Returns:
    - The sum of all unique elements in the list.
    """
    return sum(set(my_list))
