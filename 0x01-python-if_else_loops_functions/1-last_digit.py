#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = -(-number % 10)
else:
    last = number % 10
if last > 5:
    print("Last digit of {:d}".format(number), end=" ")
    print("is {:d} and is greater than 5".format(last))
elif last < 6 and last != 0:
    print("Last digit of {:d}".format(number), end=" ")
    print("is {:d} and is less than 6 and not 0".format(last))
else:
    print("Last digit of {:d}", end=" ")
    print("is {:d} and is 0".format(last))
