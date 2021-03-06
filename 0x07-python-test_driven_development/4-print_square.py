#!/usr/bin/python3
def print_square(size):
    if type(size) != int:
        raise TypeError('size must be an integer')
    if type(size) == int:
        for i in range(size):
            print("".join(["#" for i in range(size)]))
        return(size)
    if len(size) < 0:
        raise ValueError('size must be >= 0')
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
