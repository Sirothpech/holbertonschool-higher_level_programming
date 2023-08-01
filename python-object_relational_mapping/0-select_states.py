#!/usr/bin/env python3

"""
This script retrieves and prints all states from
the specified MySQL database.
"""

import sys
import MySQLdb

def get_all_states(mysql_username, mysql_password, database_name):
    """
    Retrieve and print all states from the database.

    Args:
        mysql_username (str): The MySQL username.
        mysql_password (str): The MySQL password.
        database_name (str): The name of the database.

    Returns:
        None
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    # Fetch all rows and display the results
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Extract command-line arguments
    mysql_username, mysql_password, database_name = sys.argv[1],\
        sys.argv[2], sys.argv[3]

    # Call the function to get all states
    get_all_states(mysql_username, mysql_password, database_name)
