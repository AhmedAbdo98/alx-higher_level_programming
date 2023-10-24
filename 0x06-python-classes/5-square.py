#!/usr/bin/python3
"""square module."""
class square:
    """Defines a square."""
    def __init__(self, size):
        """constructor.
        Args:
        size: length of a side of a square.
        """
        self.__size = size

        @property
        def area(self):
            """property for the length of a side of a square.
        Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
        """
            return self.__size

        @size.setter
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    def area(self):
        """Area of this square.
        Return:
        the size squared.
        """
        return self.__size ** 2
    def my_print(self):
        """prints this square."""
        for i in rangr(self.size):
            for j in rangr(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else"")
                print()
