#!/usr/bin/python3
"""
This script connects to a MySQL and retrieves and prints
the names of states that match the provided state_name.
"""
import sys
import MySQLdb


def filter_states_by_user_input(mysql_username, mysql_password, database_name,
                                state_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT name FROM states WHERE name='{}'\
        ORDER BY id ASC".format(state_name))

    # Fetch all rows and display the results
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":

    mysql_username, mysql_password, database_name, state_name =\
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    filter_states_by_user_input(mysql_username, mysql_password, database_name,
                                state_name)
