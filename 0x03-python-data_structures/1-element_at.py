#!/usr/bin/python3
def element_at(my_list, idx):
    """if idx is negative"""
    if idx < 0:
        return None
    """if idx exist is range"""
    if idx in range (my_list[idx]):
        return(my_list[idx])
