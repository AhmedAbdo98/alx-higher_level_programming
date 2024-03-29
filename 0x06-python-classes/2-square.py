#!/usr/bin/python3
"""square module."""
class square:
    """Defines a square."""
    def __init__(self, size):
        """constructor.
        Args:
        size: length of a side of a square.
        Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
