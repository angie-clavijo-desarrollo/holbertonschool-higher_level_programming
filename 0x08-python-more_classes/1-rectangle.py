#!/usr/bin/python3
"""Class Rectangle
"""


class Rectangle():
    """
    Define Class Rectangle
    Import sys library for type error
    Gets and Setters for object width and heigth
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return(self._width)

    @width.setter
    def width(self, value):
        if type(width) is not int:
            print("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(width) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = value
