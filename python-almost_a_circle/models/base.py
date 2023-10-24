#!/usr/bin/python3
"""
This is the base module
"""

from json import dumps, loads
from os.path import exists
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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        list_objs is first converted to a list of dictionaries.

        Args:
            list_objs: a list of objects from a cls subclass
            (Rectangle or Square)
        """
        list_dicts = []
        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as file:
            if list_objs:
                for obj in list_objs:
                    # Converting list_objs to a list of dictionaries
                    list_dicts.append(obj.to_dictionary())
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation 'json_string'.
        If json_string is empty or None, returns an empty list.
        """
        if not json_string or len(json_string) == 0:
            return []
        return (loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a dummy instance of the class and updates its attributes
        based on the given dictionary.

        Args:
            cls (class): The class to create an instance of.
            **dictionary: A dictionary containing the attributes to update
                the new instance with.

        Returns:
            The new instance of the class with updated attributes.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            # Not a Rectangle, so should be Square
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances of the given class from a JSON file.
        The file used should be of the format <Class_name>.json

        Returns:
            list: A list of instances (empty if the file doesn't exist)
        """
        list_objs = []
        filename = f"{cls.__name__}.json"

        if not exists(filename):
            return list_objs

        with open(filename, mode="r", encoding="utf-8") as file:
            # Extract a list of dictionary representations from the file
            list_dicts = cls.from_json_string(file.read())
            # Creating actual instances from the dictionaries in the list
            for instance_dict in list_dicts:
                list_objs.append(cls.create(**instance_dict))

        return list_objs
