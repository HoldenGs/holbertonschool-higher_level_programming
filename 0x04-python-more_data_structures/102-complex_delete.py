#!/usr/bin/python3
def complex_delete(my_dict, value):
    delete_us = []
    for k, v in my_dict.items():
        if v == value:
            delete_us.append(k)
    for k in delete_us:
        del my_dict[k]
    return my_dict
