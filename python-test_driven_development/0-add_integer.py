#!/usr/bin/python3
"""
Adds two numbers and returns the result.
    a (int or float): The first number.
    b (int or float): The second number. Defaults to 98.
"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result.
    """
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b is None:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
