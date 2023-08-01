#!/usr/bin/python3
"""
Fetch and print all states matching the provided state_name from the database.
"""
import sys
import MySQLdb


def safe_filter(mysql_username, mysql_password, database_name, state_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    # Use parameterized query to avoid SQL injection
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC;"
    cursor.execute(query, (state_name,))

    # Fetch all rows and display the results
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":

    mysql_username, mysql_password, database_name, state_name =\
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    safe_filter(mysql_username, mysql_password, database_name, state_name)
