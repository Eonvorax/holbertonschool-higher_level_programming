#!/usr/bin/python3
"""
This is the 7-add_item module
"""

import os
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

FILENAME = "add_item.json"


def main():
    """
    Adds all arguments to a Python list, and saves them to a JSON file.
    If the file already exists, the existing data is loaded and the new
    data is appended to it, then saved in the JSON file.

    Usage:
        ./7-add_item.py [item] ...
    """
    if os.path.exists(FILENAME):
        new_list = load_from_json_file(FILENAME)
    else:
        new_list = []
    new_list.extend(sys.argv[1:])
    save_to_json_file(new_list, FILENAME)


if __name__ == "__main__":
    main()
