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

    @proporety
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width (self, value):
        if type (value) != int:
            raise TypeError("value not a int")
        if value <= 0:
            raise ValueError("most be >= 0")
        self.__width = width

    @proporety
    def height (self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height (self, value):
        if type (value) != int:
            raise TypeError("value not a int")
        if value <= 0:
            raise ValueError("most be >0")
        self.__height = height

    @proporety
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type (value) != int:
            raise TypeError("x most be integer")
        if value < 0:
            raise ValueError("x most be >= 0")
        self.__x = x

    @proporety
    def y(self):
        """set/get cordinator of triangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type (value) != int:
            raise TypeError("y most be integer")
        if value < 0:
            raise ValueError("y most be >0")
        self.__y = y
