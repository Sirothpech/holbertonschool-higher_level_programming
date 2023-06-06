#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    result = []
    for row in matrix:
        new_row = []
        for element in row:
            squared = element ** 2
            new_row.append(squared)
        result.append(new_row)
    return result
