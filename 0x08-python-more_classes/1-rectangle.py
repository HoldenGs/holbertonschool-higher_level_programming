#!/usr/bin/python3


class Rectangle:
    def __init__(self, width=0, height=0):
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
