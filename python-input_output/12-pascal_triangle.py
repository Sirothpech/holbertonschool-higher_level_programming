#!/usr/bin/python3
"""
Representing the Pascal triangle of n
"""


def pascal_triangle(n):
    """
    Representing the Pascal triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            previous_value = triangle[i-1][j-1]
            current_value = triangle[i-1][j]
            value = previous_value + current_value
            row.append(value)
        row.append(1)
        triangle.append(row)

    return triangle
