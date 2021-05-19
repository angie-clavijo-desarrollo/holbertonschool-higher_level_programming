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
    Property for get for value
    Value for setter
    Return area for square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def value(self):
        return(self.__value)

    @value.setter
    def value(self, size):
        if type(size).__name__ != 'int':
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._value = size

    def area(self):
        return(self.__size * self.__size)
