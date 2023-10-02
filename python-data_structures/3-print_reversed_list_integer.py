#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        # Decrementing by 1 from (len - 1) to -1 (not included)
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
