#!/usr/bin/python3
"""created class that inherits of Base"""
from base import Base


class Rectangle(Base):

    """class constructor, instance attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """call super class, with id, call with __init__ ,  or class parent"""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """getter and setter for each instance attributes"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    """update class Rectangle, add public method, return area value"""
    def area(self):
        return self.width * self.height

    """
    update class Rectangle, add public method,
    print # for width and height
    """
    def display(self):
        if self.width == 0 or self.height:
            return ('')
        str = ('')
        for iter_one in range(self.height):
            for iter_two in range(self.width):
                str = str + '#'
            if iter_one != self.height - 1:
                str = str + '\n'
            return str


if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
