#!/usr/bin/python3
"""
0-add_integer

1 Function:
add_integer
"""


def add_integer(a, b):
    """
    add_integer: adds two integers
    a: first integer
    b: second integer

    converts floats to ints; raises exceptions for non-number input
    """
    try:
        if isinstance(a, (int, float)) is False:
            raise TypeError("a must be an integer")
        if isinstance(b, (int, float)) is False:
            raise TypeError("b must be an integer")
        c = int(a) + int(b)
        return c
    except:
        raise
