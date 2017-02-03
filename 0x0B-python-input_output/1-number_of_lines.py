#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename, 'r') as file:
        line_number = 0
        for line in file:
            line_number += 1
        return line_number
