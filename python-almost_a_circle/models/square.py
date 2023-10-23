#!/usr/bin/python3
"""
This is the square module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a square, which is a special type of rectangle.
    It inherits from the Rectangle class and adds a size attribute.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square object.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The ID of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}")
