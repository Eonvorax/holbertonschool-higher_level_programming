#!/usr/bin/python3

if __name__ == "__main__":
    for i in range(122, 96, -1):
        code = i
        if (i % 2) != 0:
            code = code - 32
        print('{:c}'.format(code), end='')
