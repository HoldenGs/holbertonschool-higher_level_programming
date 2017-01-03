#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        num = i
        if i % 3 == 0:
            num = "Fizz"
        elif i % 5 == 0:
            num = "Buzz"
        if i % 5 == 0 and i % 3 == 0:
            num = "FizzBuzz"
        print("{}".format(num), end=" ")
