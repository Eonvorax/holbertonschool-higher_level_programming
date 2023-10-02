#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list.

    Args:
        my_list (list): The input list of integers.

    Returns:
        The biggest integer in the input list, or None if the list is empty.
    """
    max = None
    if my_list:
        max = my_list[0]
        for element in my_list:
            if max < element:
                max = element
    return max
