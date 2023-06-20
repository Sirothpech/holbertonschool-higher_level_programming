#!/usr/bin/python3
"""Write an empty class BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Write an class Square"""
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
