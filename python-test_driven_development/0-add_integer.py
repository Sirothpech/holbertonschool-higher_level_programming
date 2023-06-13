#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two numbers and returns the result.
    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.
    Returns:
        int: The sum of the two numbers.
    Raises:
        TypeError: If either `a` or `b` is not an integer or a float.
                   If either `a` or `b` is None.
    """
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)) or b is None:
        raise TypeError("b must be an integer or a float")

    a = int(a)
    b = int(b)

    return a + b
