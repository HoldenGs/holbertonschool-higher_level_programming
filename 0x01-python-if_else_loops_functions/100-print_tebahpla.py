#!/usr/bin/python3
for i in range(25, -1, -1):
    char = i + 97
    if (i % 2 == 0):
        char -= 32
    print("{:c}".format(char), end="")
