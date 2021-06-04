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
    def __init__(self, size=0, position=(0, 0)):
        self.__position = position
        self.__size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if type(value) != tuple\
            or len(value) != 2\
            or type(value[1]) != int\
            or type(value[0]) != int\
            or value[0] < 0\
            or value[1] > 0:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        return(self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__position[1]):
                print('')
            for j in range(self.__size):
               print("{}{}".format(" " * self.__position[0], "#" * self.__size))


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
