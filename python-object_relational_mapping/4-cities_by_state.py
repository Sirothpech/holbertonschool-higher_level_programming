#!/usr/bin/python3
"""
Fetch and print all cities along with their corresponding
states from the database.
"""
import sys
import MySQLdb


def cities_by_states(mysql_username, mysql_password, database_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    # Use parameterized query to avoid SQL injection
    query = "SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC;"
    cursor.execute(query)

    # Fetch all rows and display the results
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":

    mysql_username, mysql_password, database_name =\
        sys.argv[1], sys.argv[2], sys.argv[3]
    cities_by_states(mysql_username, mysql_password, database_name)
