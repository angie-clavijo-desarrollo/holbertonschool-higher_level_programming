#!/usr/bin/python3
"""Class Square
"""


class Square():
    """
    Class Square
    Args Size(int)
    Raise TypeError, if not is int
    Raise ValueError, if is lass than 0
    Instance Public for area
    Return size of area
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size).__name__ != 'int':
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return(self.__size * self.__size)
