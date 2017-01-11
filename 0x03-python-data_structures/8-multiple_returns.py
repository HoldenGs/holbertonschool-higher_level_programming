#!/usr/bin/python3
def multiple_returns(sentence):
    first_letter = sentence[0]
    if len(sentence) == 0:
        first_letter = None
    t = len(sentence), first_letter
    return t
