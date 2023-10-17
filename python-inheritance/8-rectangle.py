#!/usr/bin/python3

"""
This is the module 7-base_geometry.

This module contains the BaseGeometry class
"""


class BaseGeometry:
    """
    A basic class that represents a basic geometry shape.

    Methods:
        area(): Raises an exception
        integer_validator(name, value): Validates or not the given value
    """

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inherited from BaseGeometry

    Attributes:
    - __width (int): the width of the rectangle
    - __height (int): the height of the rectangle
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with the given width and height.
        (width and height are validated by integer_validator)

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
