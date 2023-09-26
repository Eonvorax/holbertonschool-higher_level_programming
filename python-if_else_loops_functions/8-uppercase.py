#!/usr/bin/python3
def uppercase(str):
    for char in str:
        unicode = ord(char)
        if (unicode in range(97, 123)):
            unicode = unicode - 32
        print("{:c}".format(unicode), end="")
    print()
