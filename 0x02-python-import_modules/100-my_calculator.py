#!/usr/bin/python3
"""import functions of file calculator, * all"""
from calculator_1 import *
if __name__ == "__main__":
    a = 3
    b = 5
    if a != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(1)
        exit(1)
    elif (add, sub, mul, div) == (add, sub, mul, div):
        if add == add:
            print("{:d} + {:d} =" .format(a, b), add(a, b))
            print(0)
        if sub == sub:
            print("{:d} - {:d} =" .format(a, b), sub(a, b))
            print(0)
        if mul == mul:
            print("{:d} * {:d} =" .format(a, b), mul(a, b))
            print(0)
        if div == div:
            print("{:d} / {:d} =" .format(a, b), div(a, b))
            print(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        print(1)
        exit(1)
