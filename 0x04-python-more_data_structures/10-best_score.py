#!/usr/bin/python3
def best_score(my_dict):
     if my_dict is None:
          return None
     value = list(my_dict.values())
     key = list(my_dict.keys())
     return key[value.index(max(value))]
