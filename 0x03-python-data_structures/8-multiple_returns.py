#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_letter = None
    else:
        first_letter = sentence[0]
    t = len(sentence), first_letter
    return t
