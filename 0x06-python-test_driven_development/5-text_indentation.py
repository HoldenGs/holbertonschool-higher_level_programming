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
    new = "".join(c if c not in '?.:' else c + "\n\n" for c in text)
    line_list = new.split('\n')
    new = ""
    for line in line_list:
        new += '\n' + (line.strip())
    new = new[1:]
    print(new, end="")
