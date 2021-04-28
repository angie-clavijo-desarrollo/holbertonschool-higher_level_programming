#!/usr/bin/python3
def remove_char_at(str, n):
    cop = ""
    iter = 0
    for char in str:
        if iter != n:
            cop += char
        iter = iter+1
    return cop
