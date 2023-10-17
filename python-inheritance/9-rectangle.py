#!/usr/bin/python3
"""
This is the module 8-rectangle

This module contains the Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Using the BaseGeometry class
"""


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle

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
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the Rectangle object."""
        return (f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return (self.__height * self.__width)
