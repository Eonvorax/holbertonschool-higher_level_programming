#!/usr/bin/python3
"""
This is the 1-my_list module.

It contains a custom list class that inherits from the built-in list class.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Methods:
        print_sorted(self): Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
