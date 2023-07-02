#!/usr/bin/python3


"""
this the models for add_integer.py
"""


def add_integer(a, b=98):
    """
    function that adds two integer
    """
 if not isinstance(a, (int, float))
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float))
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
