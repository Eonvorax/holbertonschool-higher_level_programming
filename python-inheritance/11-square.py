#!/usr/bin/python3
"""
This is the module 11-square

This module contains the Square class, which is a subclass
of the Rectangle class.
"""

Rectangle = __import__('9-rectangle').Rectangle
"""
Using the Rectangle class
"""


class Square(Rectangle):
    """
    A class representing a square, which is a special type of rectangle.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square object with a given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square object.
        """
        return (f"[Square] {self.__size}/{self.__size}")

    def area(self):
        """
        Returns the area of the Square.
        """
        return (self.__size ** 2)
