#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Making sure our tuples have enough elements
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    # Adding the values, now defaulting to 0 if there was no element at index
    new_tuple = (a[0] + b[0], a[1] + b[1])
    return new_tuple
