#!/usr/bin/python3
"""
Divides all elements of a matrix.
    div: number divides the elements of matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    if not isinstance(matrix, (list)):
        raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    new_matrix = []
    for row in matrix:
        if not isinstance(row, (list)):
            raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
            new_row.append(round((element / div), 2))
        new_matrix.append(new_row)
    if len(row) != len(matrix[0]):
        raise TypeError("Each row of the matrix must have the same size")
    return new_matrix
