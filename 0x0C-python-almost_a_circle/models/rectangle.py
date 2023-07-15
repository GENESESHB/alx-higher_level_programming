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
