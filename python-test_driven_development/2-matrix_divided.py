#!/usr/bin/python3

"""
This is the 2-matrix_divided module

This module contains the matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
    - matrix (list of lists of integers/floats): matrix to be divided
    - div (int or float): divisor

    Returns:
    - new_matrix (list of lists): new matrix with all elements
        divided by the divisor
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (
            not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_matrix.append([round(x / div, 2) for x in row])

    return new_matrix
