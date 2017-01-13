#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    sum = 0
    for v in my_dict.values():
        if type(v) != int:
            sum += 1
    if sum == len(my_dict):
        return None
    v = list(my_dict.values())
    return list(my_dict.keys())[v.index(max(v))]
