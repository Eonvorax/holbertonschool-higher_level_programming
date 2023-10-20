#!/usr/bin/python3
"""
This is the 12-pascal_triangle module

Technical interview preparation:
    - You are not allowed to google anything
    - Whiteboard first
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal's triangle of n rows.
    """
    rows = []

    if n <= 0:
        return rows

    # Creating n rows of Pascal's triangle, from the top down
    for i in range(0, n):
        # creating the current row, empty for now
        row = []

        for j in range(0, i + 1):
            # Depending on the index (first and last element or not ?)
            if j in (0, i):
                # First or last element of the row: defaults to 1
                row.append(1)
            else:
                # Using previous row to fill the middle of the current one
                row.append(rows[i - 1][j] + rows[i - 1][j - 1])
                # NOTE: This only happens after i > 2. Previous rows [1],[1,1]
                # were built, so no index error is possible

        # Adding completed row to the list
        rows.append(row)
    return rows
