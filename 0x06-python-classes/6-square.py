#!/usr/bin/python3 
"""square module."""
class square:
    """Defines a square."""
    def __init__(self, size=0, position=(0, 0):
        """constructor.
        Args:
        size: length of a side of a square.
        """
        self.size = size
        self.position = position

        @property
        def size(self):
            """property for the length of a side of a square.
        Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0. 
        """
            return (self.__size)

        @position.setter
        def position (value, tuple): or
        len(value) != 2 or
        not all(isinstance(num, int) for num in value) or
        not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of this square.
        Return:
        the size squared.
        """
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0
        print("")
        return
        
    [print("") for i in range(0, self.__position[1])]
    for i in range(0, self.__size):
        [print(" ", end="") for j in range(0, self.__position[0])]
        [print("#", end="") for k in range(0, self.__size)]
                print("")
