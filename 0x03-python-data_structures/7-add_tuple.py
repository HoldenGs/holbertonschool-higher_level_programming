#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta0 = ta1 = tb0 = tb1 = 0
    if len(tuple_a) >= 1:
        ta0 = tuple_a[0]
    if len(tuple_a) >= 2:
        ta1 = tuple_a[1]
    if len(tuple_b) >= 1:
        tb0 = tuple_b[0]
    if len(tuple_b) >= 2:
        tb1 = tuple_b[1]
    new_tuple = ta0 + tb0, tb1 + ta1
    return new_tuple
