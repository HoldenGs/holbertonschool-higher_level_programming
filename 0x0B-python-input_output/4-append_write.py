#!/usr/bin/python3


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='UTF-8') as file:
        bytes = file.write(text)
        return bytes
