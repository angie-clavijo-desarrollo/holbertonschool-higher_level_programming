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

    def area(self):
        return(self.__size * self.__size)

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if type(value) != tuple \
                or len(value) != 2 \
                or type(value[0]) != int \
                or value[0] < 0 \
                or type(value[1]) != int \
                or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

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
