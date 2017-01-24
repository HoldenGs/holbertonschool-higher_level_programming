#!/usr/bin/python3
"""
4-square

1 class:
Square
"""
class Square:
    """
    Square: Square class, represents a physical square
    """
    def __init__(self, size=0):
        """
        __init__: Square initializer
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        size: private variable getter
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        size: private variable setter
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        area: area of instance variable size
        """
        return self.__size * self.__size
