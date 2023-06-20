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
