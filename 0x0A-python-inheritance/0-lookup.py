#!/usr/bin/python3

""" this a function lookup """


def lookup(obj):
    """
        this a function that returns the list of available attributes
         and methods of an object.

    args:
        obj; the objets we search method for get attributes for.
    Return:
           list of attributes and methode.
    """
    return dir(obj)
