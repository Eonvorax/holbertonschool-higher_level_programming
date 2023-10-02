#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list.

    Args:
        my_list (list): The input list of integers.

    Returns:
        A new list with the same size as the input list, where each element is:
        - True if the corresponding element in the input list is divisible by 2
        - False otherwise.
    """
    new_list = []
    for number in my_list:
        new_list.append((number % 2) == 0)
    return new_list
