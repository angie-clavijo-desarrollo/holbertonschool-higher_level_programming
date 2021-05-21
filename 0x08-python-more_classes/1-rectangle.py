#!/usr/bin/python3
"""Class Rectangle
"""


class Rectangle():
    """
    Define Class Rectangle
    Import sys library for type error
    Gets and Setters for object width and heigth
    """
    import sys

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return(self._width)

    @width.setter
    def width(self, value):
        if width != int:
            print("width must be an integer", file=sys.stderr)
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            return(value)

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if height != int:
            raise TypeError("height must be an integer", file=sys.stderr)
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            return(value)
