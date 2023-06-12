#!/usr/bin/python3
"""Write an empty class Square that defines a square:"""


class Square:
    """This class represents a square.
    Args:
        size: private attribute
    """
    __size = 0

    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        pass
