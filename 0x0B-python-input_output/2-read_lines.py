#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    with open(filename, 'r') as file:
        line_number = 0
        for line in file:
            line_number += 1
        file.seek(0)
        if nb_lines >= line_number or nb_lines <= 0:
            print(file.read(), end="")
        else:
            i = 0
            while i < nb_lines:
                print(file.readline(), end="")
                i += 1
