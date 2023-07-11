#!/usr/bin/python3
"""function read file and return string"""


def read_file(filename=""):
    """ Print the contents of a UTF8 text file to stdout"""
    with open(filename, "r", encoding="utf-8") as a file:
    print(file.read(), end="")
    
