#!/usr/bin/python3
"""Module containing the Square class."""


class Square:
    """This class represents a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0).

        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: The position of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position value to set.

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
            ValueError: If the position values are not positive integers.

        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(type(coord) is int and coord >= 0 for coord in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character.

        If the size is 0, an empty line is printed.
        If the position[1] value is greater than 0, lines are not
        filled with spaces.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
