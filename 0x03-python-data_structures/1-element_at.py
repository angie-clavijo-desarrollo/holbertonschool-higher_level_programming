#!/usr/bin/python3
def element_at(my_list, idx):
    """if idx exist is range"""
    if idx in range(my_list[idx]):
        return(my_list[idx])
    else:
        return None
