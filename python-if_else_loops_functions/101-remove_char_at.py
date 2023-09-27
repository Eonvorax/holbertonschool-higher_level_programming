#!/usr/bin/python3

def remove_char_at(str, n):
    # May be better than using a double slice or join()
    new_str = ""
    for i, char in enumerate(str):
        if (i != n):
            new_str += char
    return new_str
