#!/usr/bin/python3
"""
===========================
defines a json file_writing a function.
===========================
"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to txt file using json representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
