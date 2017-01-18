#!/usr/bin/python3
"""
3-say_my_name

1 function:
say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: print out first_name and last_name
    first_name: string
    last_name: string

    exceptions:
    TypeError: if either input is not a string
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    try:
        print("{:s} {:s}".format(first_name, last_name))
    except:
        raise
