#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Inisialisation for a new rectangle.

        Args:
            width (int): is the width for N_R
            height (int):is a height for N_R
            x (int): the coordinate for N_R
            y (int): the coordinate for N_R
            id (int): the identity for N_R
        raises:
            TypeError: raise if height or width not int.
            ValueError: raise if height or width <= 0.
            TypeError: raise if x or y not n int.
            ValueError: raise if x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("must be an integer")
        if value <= 0:
            raise ValueError(" width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get cordinator of triangle"""
        return self.y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be integer")
        if value < 0:
            raise ValueError("y most be >=0")
        self.__y = value

    def area(self):
        """Initialisation area for rectangle.

        Args:
            self.__width :the width for rectangle
            self.__height :the heigth for rectangle

            area == self.__height * self.__width
        """
        return self.__width * self.__height
