#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """
    Executes a function safely by catching any exceptions that may occur.

    Args:
        fct (function): The function to execute.
        *args: The arguments to pass to the function.

    Returns:
        The result of the function if it executes successfully,
        or None if an exception occurs.
    """
    try:
        # Returning function call on unpacked arguments tuple (see '*' syntax)
        return (fct(*args))
    except Exception as err_msg:
        # Met an exception, printing Exception error message to stderr
        sys.stderr.write("Exception: " + str(err_msg) + "\n")
        return None
