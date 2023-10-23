#!/usr/bin/python3
"""
This is the base module
"""

from json import dumps
"""To convert objects to json"""


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
                If the list is empty or None, returns "[]".
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return dumps(list_dictionaries)
