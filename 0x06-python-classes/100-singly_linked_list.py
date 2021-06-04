#!/usr/bin/python3
"""Class Node
"""


class Node:
    def __init__(self, next_node):
        self.__next_node = next_node

    def data(self):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def next_node(self, value):
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

        def next_node(self):
            self.__next_node = self

        @property
        def next_node(self):
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            if nex_node:
                return
            else:
                raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    def __init__(self, head):
        self.__head = head

    def sorted_insert(self, value):
        self.value = value

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
