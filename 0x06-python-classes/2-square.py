#!/usr/bin/python3
class Square():
    """
    This is a class with name Square
    The args is size(int)
    Raises
    TypeError if is diferent to an integer
    ValueError if is lass than 0
    """
    def __init__(self, size=0):
        if type(size).__name__ != 'int':
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
