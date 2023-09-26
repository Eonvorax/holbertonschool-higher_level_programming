#!/usr/bin/python3

from sys import argv


def sum_args(argv):
    argc = len(argv)
    args_sum = 0
    for i in range(1, argc):
        args_sum += int(argv[i])
    print(args_sum)


if __name__ == "__main__":
    sum_args(argv)
