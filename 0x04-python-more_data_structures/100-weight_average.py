#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    up = 0
    down  = 0
    for i in my_list:
        up += i[0] * i[1]
        down += i[1]
    return up / down

