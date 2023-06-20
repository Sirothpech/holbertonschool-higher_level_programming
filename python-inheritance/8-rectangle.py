#!/usr/bin/python3
"""Write an empty class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """initialize the rectangle"""
        self._width = self.integer_validator("width", width)
        self._height = self.integer_validator("width", height)
