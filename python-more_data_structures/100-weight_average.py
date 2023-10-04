#!/usr/bin/python3

def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return 0
    sum_values = 0
    sum_weights = 0
    for item in my_list:
        sum_values += item[0] * item[1]
        sum_weights += item[1]
    return (sum_values / sum_weights)
