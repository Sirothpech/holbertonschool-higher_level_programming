#!/usr/bin/python3
"""Write an empty class BaseGeometry"""


class BaseGeometry:
    """This class represents a BaseGeometry."""
    def __init__(self):
        """Init the BaseGeometry"""
        pass

    def area(self):
        """Calculate and return the area of BaseGeometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(name) is str:
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
        return value
