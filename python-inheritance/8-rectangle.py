#!/usr/bin/python3
"""Write an empty class BaseGeometry"""


class BaseGeometry:
    """This class represents a BaseGeometry."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """initialize the rectangle"""
        self._width = self.integer_validator("width", width)
        self._height = self.integer_validator("width", height)
