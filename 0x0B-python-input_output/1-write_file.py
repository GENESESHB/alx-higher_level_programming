#!/usr/bin/python3

"""
=================================
write_f(fname, txt) it s a function can
write the txt in ather file.
=================================
"""


def write_file(filename="", text=""):
     """Write a string to a UTF8 text file.

        Args:
            filename (str): The name of the file to write.
            text (str): The text to write to the file.
        Returns:
               The number of characters written.
     """
     with open(filename, "w", encoding="utf-8") as f:
         return f.write(text)
