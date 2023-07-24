# SQL - Introduction

## Description

This project is about learning the basics of the Structured Query Language (SQL). SQL is a language used to interact with databases. You will use SQL to create, modify, delete, and display data in a database.

## Requirements

   - Allowed editors: `vi`, `vim`, `emacs`
   - All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
   - All your files should end with a new line
   - All your SQL queries should have a comment just before (i.e. syntax above)
   - All your files should start by a comment describing the task
   - All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
   - A `README.md` file, at the root of the folder of the project, is mandatory
   - The length of your files will be tested using `wc`

## Tasks 0-7:

Task Details

0. :Write a script that lists all databases of your MySQL server.

Output:

The output of the script should be a list of all the databases in your MySQL server, one per line.

Example:
```
Database
hbtn_0c_0
information_schema
mysql
performance_schema
sys
```
1. : List databases

The task 1 is to write a script that lists all the databases in your MySQL server.

2. : Create a database

The task 2 is to write a script that creates a database called hbtn_0c_0 in your MySQL server.

3. : Delete a database

The task 3 is to write a script that deletes the database hbtn_0c_0 from your MySQL server.

4. : List tables

The task 4 is to write a script that lists all the tables in the database hbtn_0c_0 of your MySQL server.

5. : Full description

The task 5 is to write a script that prints the full description of the table first_table of the database hbtn_0c_0 of your MySQL server.

6. : List all in table

The task 6 is to write a script that lists all the rows of the table first_table of the database hbtn_0c_0 of your MySQL server.

7. : First add

The task 7 is to write a script that inserts a new row in the table first_table of the database hbtn_0c_0 of your MySQL server. The new row will have the following values:

id = 89
name = Best School

## Tasks 8-16:

Count 89
Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command

9. Full creation

Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

second_table description:

id INT
name VARCHAR(256)
score INT
The database name will be passed as an argument to the mysql command

If the table second_table already exists, your script should not fail

You are not allowed to use the SELECT and SHOW statements

Your script should create these records:

id = 1, name = “John”, score = 10
id = 2, name = “Alex”, score = 3
id = 3, name = “Bob”, score = 14
id = 4, name = “George”, score = 8
10. List by best

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

Results should display both the score and the name (in this order)

Records should be ordered by score (top first)

The database name will be passed as an argument of the mysql command

11. Select the best

Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

Results should display both the score and the name (in this order)

Records should be ordered by score (top first)

The database name will be passed as an argument of the mysql command

12. Cheating is bad

Write a script that updates the score of Bob to 10 in the table second_table.

You are not allowed to use Bob’s id value, only the name field

The database name will be passed as an argument of the mysql command

13. Score too low

Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command

14. Average

Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

The result column name should be average

The database name will be passed as an argument of the mysql command

15. Number by score

Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

The result should display:

the score
the number of records for this score with the label number
The list should be sorted by the number of records (descending)

The database name will be passed as an argument to the mysql command

16. Say my name

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

Don’t list rows without a name value

Results should display the score and the name (in this order)

Records should be listed by descending score

The database name will be passed as an argument to the mysql command

In this example, new data have been added to the table second_table.

```
sirothpech@LAPTOP-NAVGPF15:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
18  Aria
12  Aria
10  John
10  Bob
sirothpech@LAPTOP-NAVGPF15:~/$
```

## Authors
This project was realized Christophe Ngan (@Sirothpech)
