#!/usr/bin/python3

"""
Module listing all states from the database
"""

import MySQLdb
import sys


def main():
    """
    Main function handling arguments, then requesting and printing the data
    """
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    database.close()


if __name__ == "__main__":
    main()
