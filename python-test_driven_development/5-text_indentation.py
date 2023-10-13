#!/usr/bin/python3
"""
This is the 5-text_indentation module
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each of these characters: (., ?, :)

    Args:
        text (str): the text to be formatted and printed

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # line buffer (empty at the start)
    line = ""
    for char in text:
        # adding character to the buffer
        line += char
        # checking for special case :
        if char in ('.', '?', ':'):
            # Printing 2 newlines after the character
            print(f"{line}".strip() + "\n")
            # resetting line buffer
            line = ""
    # printing line buffer leftovers
    print(line.strip(), end="")
