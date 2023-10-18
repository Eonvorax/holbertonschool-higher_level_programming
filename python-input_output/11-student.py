#!/usr/bin/python3
"""
This is the 11-student module
"""


class Student():
    """
    A class representing a student.

    Attributes:
    - first_name (str): the first name of the student
    - last_name (str): the last name of the student
    - age (int): the age of the student
    """

    def __init__(self, first_name, last_name, age):
        """
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student object.

        Args:
        - attrs (list of str): a list of attribute names to include in
        the dictionary (defaults to None for no filter)

        Returns:
        - A dictionary containing the filtered attibutes.
        """
        if attrs is None:
            return self.__dict__

        # Alternative way: dictionary comprehension
        # return {attr: self.__dict__[attr]
        # for attr in attrs if attr in self.__dict__}

        filtered_attrs = {}
        for attr in attrs:
            if attr in self.__dict__:
                filtered_attrs[attr] = self.__dict__[attr]

        return filtered_attrs

    def reload_from_json(self, json):
        for key in json:
            self.__dict__[key] = json[key]
