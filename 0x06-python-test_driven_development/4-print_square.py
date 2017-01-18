#!/usr/bin/python3
"""
4-print_square

1 function:
print_square
"""
def print_square(size):
    """
    print_square: print a square of hashes of size
    size: side length of square

    Exceptions
    TypeError: if size isn't an integer
    ValueError: if size is under zero
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    try:
        for i in range(size):
            print("#" * size)
        if size == 0:
            print()
    except:
        raise
