# SQL - More queries

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

# SQL - More queries

## Task 0: My privileges!
Write a script (`0-privileges.sql`) that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).

```bash
$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password:
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'
$ echo "CREATE USER 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p
Enter password:
$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p
Enter password:
$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password:
Grants for user_0d_1@localhost
GRANT SELECT, INSERT, UPDA..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`
GRANT APPLICATION_PASSWORD_ADMIN, AUDIT..., XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
```

## Task 1: Root user
Write a script (`1-create_user.sql`) that creates the MySQL server user `user_0d_1`.

- `user_0d_1` should have all privileges on your MySQL server.
- The `user_0d_1` password should be set to `user_0d_1_pwd`.
- If the user `user_0d_1` already exists, your script should not fail.

```bash
$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password:
$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password:
Grants for user_0d_1@localhost
GRANT SELECT, INSERT, ..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`
GRANT APPLICATION_PASSWORD_ADMIN, ..., XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
```

## Task 2: Read user
Write a script (`2-create_read_user.sql`) that creates the database `hbtn_0d_2` and the user `user_0d_2`.

- `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`.
- The `user_0d_2` password should be set to `user_0d_2_pwd`.
- If the database `hbtn_0d_2` already exists, your script should not fail.
- If the user `user_0d_2` already exists, your script should not fail.

```bash
$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
Enter password:
$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password:
Grants for user_0d_1@localhost
GRANT SELECT, ..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`
GRANT APPLICATION_PASSWORD_ADMIN, ..., XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`
Grants for user_0d_2@localhost
GRANT USAGE ON *.* TO `user_0d_2`@`localhost`
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`
```

## Task 3: Always a name
Write a script (`3-force_name.sql`) that creates the table `force_name` on your MySQL server.

Table `force_name` description:
- `id INT`
- `name VARCHAR(256)` can’t be null.

The database name will be passed as an argument of the `mysql` command.
If the table `force_name` already exists, your script should not fail.

```bash
$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
$ echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id  name
89  Best School
$ echo 'INSERT INTO force_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id  name
89  Best School
```

## Task 4: ID can't be null
Write a script (`4-never_empty.sql`) that creates the table `id_not_null` on your MySQL server.

Table `id_not_null` description:
- `id INT` with the default value `1`.
- `name VARCHAR(256)`.

The database name will be passed as an argument of the `mysql` command.
If the table `id_not_null` already exists, your script should not fail.

```bash
$ cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
$ echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id  name
89  Best School
$ echo 'INSERT INTO id_not_null (name) VALUES ("Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id  name
89  Best School
1   Best
```

## Task 5: Unique ID
Write a script (`5-unique_id.sql`) that creates the table `unique_id` on your MySQL server.

`unique_id` description:
- `id INT` with the default value `1` and must be unique.
- `name VARCHAR(256)`.

The database name will be passed as an argument of the `mysql` command.
If the table `unique_id` already exists, your script should not fail.

```bash
$ cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id  name
89  Best School
$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'unique_id.id'
$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id  name
89  Best School
```

## Task 6: States table
Write a script (`6-states.sql`) that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.

`states` description:
- `id INT` unique, auto-generated, can’t be null, and is a primary key.
- `name VARCHAR(256)` can’t be null.

If the database `hbtn_0d_usa` already exists, your script should not fail.
If the table `states` already exists, your script should not fail.

```bash
$ cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password:
$ echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  name
1   California
2   Arizona
3   Texas
```

## Task 7: Cities table
Write a script (`7-cities.sql`) that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.

`cities` description:
- `id INT` unique, auto-generated, can’t be null, and is a primary key.
- `state_id INT`, can’t be null, and must be a FOREIGN KEY that references to `id` of the `states` table.
- `name VARCHAR(256)` can’t be null.

If the database `hbtn_0d_usa` already exists, your script should not fail.
If the table `cities` already exists, your script should not fail.

```bash
$ cat 7-cities.sql | mysql -hlocalhost -uroot -p
Enter password:
$ echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  state_id    name
1   1   San Francisco
```

## Task 8: Cities of California
Write a script (`8-cities_of_california_subquery.sql`) that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

The `states` table contains only one record where `name = California` (but the `id` can be different, as per the example).
Results must be sorted in ascending order by `cities.id`.
You are not allowed to use the JOIN keyword.
The database name will be passed as an argument of the `mysql` command.

```bash
$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  name
1   California
2   Arizona
3   Texas
4   Utah
$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
$ cat 8-cities_of_california_sub

query.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  name
1   San Francisco
2   San Jose
```

## Task 9: Cities by States
Write a script (`9-cities_by_state_join.sql`) that lists all cities contained in the database `hbtn_0d_usa`.

Each record should display: `cities.id - cities.name - states.name`
Results must be sorted in ascending order by `cities.id`.
You can use only one SELECT statement.
The database name will be passed as an argument of the `mysql` command.

```bash
$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  name
1   California
2   Arizona
3   Texas
4   Utah
$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
$ cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  name    name
1   San Francisco   California
2   San Jose    California
4   Page    Arizona
6   Paris   Texas
7   Houston Texas
8   Dallas  Texas
```

## Task 10: Genre ID by show

Import the database dump from `hbtn_0d_tvshows` to your MySQL server.

Write a script (`10-genre_id_by_show.sql`) that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

Each record should display: `tv_shows.title - tv_show_genres.genre_id`
Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`.
You can use only one SELECT statement.
The database name will be passed as an argument of the `mysql` command.

```bash
$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
title   genre_id
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
```

## Task 11: Genre ID for all shows

Import the database dump of `hbtn_0d_tvshows` to your MySQL server.

Write a script (`11-genre_id_all_shows.sql`) that lists all shows contained in the database `hbtn_0d_tvshows`.

Each record should display: `tv_shows.title - tv_show_genres.genre_id`
Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`.
If a show doesn’t have a genre, display NULL.
You can use only one SELECT statement.
The database name will be passed as an argument of the `mysql` command.

```bash
$ cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
title   genre_id
Better Call Saul    NULL
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
Homeland    NULL
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
```

## Task 12: No genre

Import the database dump from `hbtn_0d_tvshows` to your MySQL server.

Write a script (`12-no_genre.sql`) that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

Each record should display: `tv_shows.title - tv_show_genres.genre_id`
Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`.
You can use only one SELECT statement.
The database name will be passed as an argument of the `mysql` command.

```bash
$ cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
title   genre_id
Better Call Saul    NULL
Homeland    NULL
```

## Task 13: Number of shows by genre

Import the database dump from `hbtn_0d_tvshows` to your MySQL server.

Write a script (`13-count_shows_by_genre.sql`) that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

Each record should display: `<TV Show genre> - <Number of shows linked to this genre>`
First column must be called `genre`
Second column must be called `number_of_shows`
Don’t display a genre that doesn’t have any shows linked.
Results must be sorted in descending order by the number of shows linked.
You can use only one SELECT statement.
The database name will be passed as an argument of the `mysql` command.

```bash
$ cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
genre   number_of_shows
Drama   5
Comedy  4
Mystery 2
Crime   2
Suspense    2
Thriller    2
Adventure   1
Fantasy 1
```

## Task 14: My genres

Import the database dump from `hbtn_0d_tvshows` to your MySQL server.

Write a script (`14-my_genres.sql`) that uses the `hbtn_0d_tvshows` database to list all genres of the show Dexter.

The `tv_shows` table contains only one record where `title = Dexter` (but the `id` can be different).
Each record should display: `tv_genres.name`
Results must be sorted in ascending order by the genre name.
You can use only one SELECT statement.
The database name will be passed as an argument of the `mysql` command.

```bash
$ cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
Comedy
Crime
Drama
Suspense
Thriller
```

## Task 15: Only Comedy

Import the database dump from `hbtn_0d_tvshows` to your MySQL server.

Write a script (`15-comedy_only.sql`) that lists all Comedy shows in the database `hbtn_0d_tvshows`.

The `tv_genres` table contains only one record where `name = Comedy` (but the `id` can be different).
Each record should display: `tv_shows.title`
Results must be sorted in ascending order by the show title.
You can use only one SELECT statement.
The database name will be passed as an argument of the `mysql` command.

```bash
$ cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
Better Call Saul
New Girl
Silicon Valley
The Big Bang Theory
```

## Task 16: List shows and genres

Import the database dump from `hbtn_0d_tvshows` to your MySQL server.

Write a script (`16-list_shows_and_genres.sql`) that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.

If a show doesn’t have a genre, display NULL in the genre column.
Each record should display: `tv_shows.title - tv_genres.name`
Results must be sorted in ascending order by the show title and genre name.
You can use only one SELECT statement.
The database name will be passed as an argument of the `mysql` command.

```bash
$ cat 16-list_shows_and_genres.sql | mysql -hlocalhost -uroot -p hbtn

_0d_tvshows
Enter password:
title   name
Better Call Saul    Comedy
Better Call Saul    Crime
Breaking Bad    Crime
Breaking Bad    Drama
Breaking Bad    Suspense
Breaking Bad    Thriller
Dexter  Comedy
Dexter  Crime
Dexter  Drama
Dexter  Suspense
Dexter  Thriller
Game of Thrones Drama
Game of Thrones Fantasy
Game of Thrones Mystery
Homeland    Drama
Homeland    Suspense
House   Drama
House   Medical
New Girl    Comedy
Silicon Valley  Comedy
The Big Bang Theory Comedy
The Last Man on Earth   Comedy
The Last Man on Earth   Drama
```

## Authors
This project was realized Christophe Ngan (@Sirothpech)
