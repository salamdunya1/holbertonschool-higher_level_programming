#!/usr/bin/python3
"""Defines a square"""


class Square:
    """
    Defines a square by its size.

    Attributes:
        __size (int): Private instance attribute represent the size  square.
    """

    def __init__(self, size):
        """Initializes the Square instance with a given size."""
        self.__size = size
