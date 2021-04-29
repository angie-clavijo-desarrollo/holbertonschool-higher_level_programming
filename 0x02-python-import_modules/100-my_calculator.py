#!/usr/bin/python3
"""import functions of file calculator, * all"""
from calculator_1 import *
if __name__ == "__main__":
    a = 3
    b = 5
    if a != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif (add, sub, mul, div) == (add, sub, mul, div):
       print("{:d} + {:d} =" .format(a, b), add(a, b))
       print("{:d} - {:d} =" .format(a, b), sub(a, b))
       print("{:d} * {:d} =" .format(a, b), mul(a, b))
       print("{:d} / {:d} =" .format(a, b), div(a, b))
       exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)