#!/usr/bin/python3
"""Class Student"""


class Student:
    """
    Def instance atrributes of class student
    Instances publics of attributes first_name, last_name, age
    self espicify  methods and atributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if(attrs is type(str)):
            return(self.last_name, self.first_name)
        else:
            return( self.age, self.first_name, self.last_name, )
        return(self.__dict__)