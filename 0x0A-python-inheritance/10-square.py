#!/usr/bin/python3
"""This function import  file 9 rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class square inheritance of rectangle
    that validate of size of square
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
