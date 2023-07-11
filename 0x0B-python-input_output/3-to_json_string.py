#!/usr/bin/python3
"""
================================
Defines a string-to-JSON function.
================================
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    Args:
        my_obj: The object to be converted into JSON
    Returns:
        The JSON representation of the object (string)
    """
    return json.dumps(my_obj)
