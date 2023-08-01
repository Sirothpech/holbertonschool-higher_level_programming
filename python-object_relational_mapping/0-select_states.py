#!/usr/bin/env python3
import sys
import MySQLdb

def get_all_states(mysql_username, mysql_password, database_name):
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

    mysql_username, mysql_password, database_name = sys.argv[1], sys.argv[2],\
        sys.argv[3]
    get_all_states(mysql_username, mysql_password, database_name)
