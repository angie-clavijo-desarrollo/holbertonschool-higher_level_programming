#!/usr/bin/python3
"""created class that inherits of Base"""
Base = __import__('base').Base


class Rectangle(Base):

    """class constructor, instance attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """call super class, with id, call with __init__ ,  or class parent"""
        super().__init__(id)
        """private instance atributes"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        """validations"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')

        """validations"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')

        """validations"""
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')

        """validations"""
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')


        """getter and setter for each instance attributes"""
        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, width):
            """validations"""
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
            """validations"""
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
            """validations"""
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
            """validations"""
            if type(y) is not int:
                raise TypeError('y must be an integer')
            if y < 0:
                raise ValueError('y must be >= 0')
            self.__y = y


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


