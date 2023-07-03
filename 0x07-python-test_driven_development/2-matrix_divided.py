#!/usr/bin/python3


"""
Module for matrix division
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"

    # Input validation
    if not isinstance(matrix, list) or len(matrix) < 1:
        raise TypeError(error)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix[0], list):
        raise TypeError(error)

    len_matrix = len(matrix[0])
    new_list = []

    for count, row in enumerate(matrix):
        if not isinstance(row, list) or len(row) < 1:
            raise TypeError(error)

        if len(row) != len_matrix:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error)
            new_row.append(round(element / div, 2))

        new_list.append(new_row)

    return new_list
