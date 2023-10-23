#!/usr/bin/python3
"""
This is the base module
"""


class Base:
    """
    A class representing the base of all other classes in this project.

    Attributes:
        __nb_objects (int): keeps track of the number of Base instances.
        id (int): the id of the Base instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        Args:
            id (int): The id of the instance.
            If None, it will be set to __nb_objects

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
