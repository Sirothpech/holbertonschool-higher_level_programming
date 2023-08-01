#!/usr/bin/python3
"""
Filter and print cities in a specified state from the database.
"""
import sys
import MySQLdb


def filter_cities_by_state(mysql_username, mysql_password, database_name,
                           state_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    # Use parameterized query to avoid SQL injection
    query = "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities\
        JOIN states ON cities.state_id = states.id\
            WHERE states.name=%s ORDER BY cities.id ASC;"
    cursor.execute(query, (state_name,))

    # Fetch the row and display the results
    row = cursor.fetchone()
    if row[0]:
        print(row[0])
    else:
        print("")

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":

    mysql_username, mysql_password, database_name, state_name =\
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    filter_cities_by_state(mysql_username, mysql_password, database_name,
                           state_name)
