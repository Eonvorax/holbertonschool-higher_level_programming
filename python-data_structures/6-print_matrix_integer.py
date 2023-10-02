#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for number in line:
            print("{:d}".format(number), end="")
            if number != line[-1]:
                print(" ", end="")
        print()
