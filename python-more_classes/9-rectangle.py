#!/usr/bin/python3
"""
Write an empty class Rectangle that defines a rectangle:
Private instance attribute: width.
Private instance attribute: height.
"""


class Rectangle:
    """This class represents a  rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """initialize the rectangle"""
        rectangle_str = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_str
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += str(self.print_symbol)
            rectangle_str += "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """return the command to create the same rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delete the current Rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set a new value to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set a new value to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return the biggest Rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """return a new instance as a square"""
        return cls(size, size)
