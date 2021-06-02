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
        if (attrs is None):
            return(self.__dict__)

        attrs_all = {}

        for i in range(len(attrs)):
            if attrs[i] in self.__dict__:
                aux = {
                    attrs[i]: getattr(self, attrs[i])
                }
                attrs_all.update(aux)
        return attrs_all
