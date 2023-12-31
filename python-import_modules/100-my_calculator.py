#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    operators = {"+": add,
                 "-": sub,
                 "*": mul,
                 "/": div}

    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    for i, op in enumerate(operators):
        if (argv[2] == op):
            print(f"{a} {argv[2]} {b} = {operators[op](a, b)}")
            exit(0)

    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
