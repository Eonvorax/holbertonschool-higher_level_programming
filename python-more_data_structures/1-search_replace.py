#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    Args:
    - my_list: the initial list
    - search: the element to replace in the list
    - replace: the new element

    Returns:
    - A new list with all occurrences of `search` replaced by `replace`

    Example:
    >>> search_replace([1, 2, 3, 2, 4, 2], 2, 5)
    [1, 5, 3, 5, 4, 5]
    """
    new_list = [replace if item == search else item for item in my_list]
    return new_list
