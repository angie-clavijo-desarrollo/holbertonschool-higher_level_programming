#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) != int and type(a) != float or type(a) == None:
        raise TypeError('a must be a integer')

    if type(b) != int and type(b) != float or type(b) == None:
        raise TypeError('b must be a integer')

    return(int(a+b))