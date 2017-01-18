#!/usr/bin/python3
"""
5-text_indentation.py

1 function:
text_indentation
"""


def text_indentation(text):
    """
    text_indentation: print 2 newlines after every ?, ., and : in text
    text: the string to indent

    Exceptions
    TypeError: if text isn't a string
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    try:
        new = text
        chars = ['?', '.', ':']
        for c in chars:
            new = new.replace(c, c + '\n\n')
        new = new.replace('\n ', '\n')
        print(new, end="")
    except:
        raise
