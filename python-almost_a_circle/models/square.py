#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle:
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """initialize the square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding the __str__ method so that it returns"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
