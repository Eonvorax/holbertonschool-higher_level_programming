#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
    - matrix: a 2-dimensional array

    Returns:
    - A new matrix:
        - Same size as original matrix
        - Each value should be the square of the value of the input
    """
    # Also works in one line but looks digusting :
    # return list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
    return [[x * x for x in row] for row in matrix]
