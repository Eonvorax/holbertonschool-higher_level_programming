#!/usr/bin/python3

"""
lists all states with a name starting with N (upper N) from the database
"""

import MySQLdb
import sys


def main():
    """
    Main function handling arguments, then requesting and printing the data
    """

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = database.cursor()

    cursor.execute("""
                   SELECT * FROM states
                   WHERE name LIKE BINARY 'N%'
                   """)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()


if __name__ == "__main__":
    main()
