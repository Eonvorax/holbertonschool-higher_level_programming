#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Args:
        sentence (str): The input string.

    Returns:
        A tuple with two elements:
        - The length of the input string.
        - The 1st character of the string, or None if the string is empty.
    """
    if len(sentence) == 0:
        return (len(sentence), None)
    return (len(sentence), sentence[0])
