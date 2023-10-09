#!/usr/bin/python3
"""
This module defines the Square class
"""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.

    Methods:
        area(): Returns the area of the square.
        my_print(): Prints the square using the '#' character.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If size is not an integer or position is
            not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (
            not isinstance(position, tuple) or len(position) != 2 or
            not isinstance(position[0], int) or not isinstance(
                position[1], int)
            or position[0] < 0 or position[1] < 0
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
        Calculate the area of the Square.

        Returns:
            The area of the Square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            The size of the Square.
        """
        return self.__size

    @property
    def position(self):
        """
        Getter method for the private instance attribute `position`.
        Returns:
            The value of the `position` attribute.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The new size of the Square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers representing the
            position of the square.

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.

        """
        if (
            not isinstance(value, tuple) or len(value) != 2 or
            not isinstance(value[0], int) or not isinstance(value[1], int)
            or value[0] < 0 or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints a square of a given size and position using the '#' character.

        If the size is 0, prints an empty line. If the position is not (0, 0),
        prints the specified number of spaces before printing the square.

        Args:
            self (Square): The square to print.

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return

        for line_count in range(0, self.__position[1]):
            print()

        for i in range(0, self.__size):
            for spaces_count in range(0, self.__position[0]):
                print(" ", end="")

            for j in range(0, self.__size):
                print("#", end="")
            print()
