#!/usr/bin/python3
"""Class Rectangle
"""


class Rectangle:
    """
    Define Class Rectangle
    Import sys library for type error
    Gets and Setters for object width and heigth
    Method Area for know area of rectangle
    Method Perimeter for know perimeter of rectangle and if area and
        perimeter is 0 perimeter will be 0
    Function magic __str__ for printing rectanfle with ##
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return(self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            perimeter = 0
            return('')
        return(self.width + self.height) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return('')
        stri = ('')
        for inc in range(self.__height):
            for inc_two in range(self.__width):
                stri = stri + '#'
            if inc != self.__height - 1:
                stri = stri + '\n'
        return(stri)

    def __repr__(self):
        return(stri)
