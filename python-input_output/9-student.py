#!/usr/bin/python3
"""
This is the 9-student module
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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of a Student instance.
        """
        return self.__dict__
