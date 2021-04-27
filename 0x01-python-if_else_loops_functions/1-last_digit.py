#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = ((number % 10)) #last digit#
 #follow last digit of number 
if last_digit > 5:
	 print("Last digit of, {:d} is {:d} and is greater than 5".format(number, (last_digit)))
elif last_digit == 0:
	print("Last digit of, {:d} is {:d} and is 0".format(number, (last_digit)))

if last_digit < 6 and number != 0:
	print("Last digit of, {:d} is {:d} and is less than 6 and not 0".format(number, (last_digit * -1)))

#number * -1
#if (number % 10) > 5:
#    print("Last digit of, {:d} is {:d} and is greater than 5".format(number, (number % 10)))
#elif (number % 10) < 6 and  (number * -1) != 0:
#   print("Last digit of, {:d} is {:d} and is less than 6 and not 0".format(number, (number % 10)))
#else: 
#    print("Last digit of, {:d} is {:d} and is 0".format(number, (number % 10)))
 