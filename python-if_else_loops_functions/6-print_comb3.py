#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if (i == 8 and j == 9):
            print(i, j, sep="")
        elif (i != j):
            print(i, j, sep="", end=", ")
