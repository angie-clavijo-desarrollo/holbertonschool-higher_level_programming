#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in my_list:
        if my_list:
            return(max(my_list[:]))
        if my_list == 0 or my_list < 0:
            return None
