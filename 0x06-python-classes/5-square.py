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
        self.size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value).__name__ != 'int':
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return(self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
            return()
        for i in range(self.__size):
            print("".join(["#" for i in range(self.__size)]))

if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
