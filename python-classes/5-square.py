#!/usr/bin/python3
"""Defines a square"""


class Square:
    """
    Defines a square by its size with validation, area calculation,
    and methods to retrieve size, set size, and print the square.

    Attributes:
        __size (int): Private attribute for square size
    """

    def __init__(self, size=0):
        """Initializes the Square instance with an optional size."""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
