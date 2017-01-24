#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if isinstance(position, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if isinstance(position, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position


    def area(self):
        return self.__size * self.__size

    def my_print(self):
        print("\n" * self.__position[1], end="")
        print("{}{}\n".format(" " * self.__position[0],
                                "#" * self.__size) * self.__size, end="")
        if self.__size == 0:
            print()
