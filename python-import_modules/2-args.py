#!/usr/bin/python3

from sys import argv


def list_args(argv):
    argc = len(argv)
    if argc == 2:
        print(f"{argc - 1} argument", end="")
    else:
        print(f"{argc - 1} arguments", end="")
    if argc == 1:
        print(".")
        return
    else:
        print(":")
    for i in range(1, argc):
        print(f"{i}: {argv[i]}")


if __name__ == "__main__":
    list_args(argv)
