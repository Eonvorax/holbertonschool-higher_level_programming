#!/usr/bin/python3
"""
This is the rectangle module
"""

from models.base import Base


class Rectangle(Base):
    """
    This class represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle's position.
        __y (int): The y-coordinate of the rectangle's position.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for the Rectangle class

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The ID of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}")

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width}

    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The value to set the width attribute to.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The value to set the height attribute to.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute.
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute.

        Args:
            value (int): The value to set the x attribute to.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute.
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute.

        Args:
            value (int): The value to set the y attribute to.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return (self.__height * self.__width)

    def display(self):
        """
        Prints the rectangle using the '#' character.
        The output is offset vertically by y and horizontally by x
        """
        for newline in range(0, self.__y):
            print()

        for row in range(0, self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle instance.
        **kwargs will be skipped if *args exists and is not empty

        Args:
            *args: Variable length argument list of attributes to update.
            **kwargs: Arbitrary keyword arguments to update attributes.
        """
        if not args or len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
