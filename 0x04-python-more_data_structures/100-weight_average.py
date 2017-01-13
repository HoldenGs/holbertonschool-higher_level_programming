#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = 0
    num = 0
    for t in my_list:
        sum += t[0] * t[1]
        num += t[1]
    average = sum / num
    return average
