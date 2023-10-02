#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
        my_list (list): The input list.
        idx (int): The index of the item to delete.

    Returns:
        The modified input list, with the item at the specified index deleted.
        If the index is negative or out of range, the function returns the
        original list without any modification.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
