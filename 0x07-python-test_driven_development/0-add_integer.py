#!/usr/bin/python3
"""
This is the module  0-add_integer.py
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
