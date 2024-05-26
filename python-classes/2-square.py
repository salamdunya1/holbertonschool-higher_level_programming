#!/usr/bin/python3
"""Defines a square"""


class Square:
    """
    Defines a square by its size with validation.

    Attributes:
        __size (int): Private size attribute.
   """

    def __init__(self, size=0):
        """Initializes the Square instance with an optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
