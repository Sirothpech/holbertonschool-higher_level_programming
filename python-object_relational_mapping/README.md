# Python - Object-relational mapping

This repository contains Python scripts and classes to interact with a MySQL database using Object-Relational Mapping (ORM) techniques. The scripts utilize the `MySQLdb` module to connect to a local MySQL server running on port 3306. The database used throughout these tasks is named `hbtn_0e_0_usa`.

## Task 0: Get all states

Script: `0-select_states.py`

This script lists all states from the database `hbtn_0e_0_usa` in ascending order by their `id` column.

Usage:
```bash
python 0-select_states.py <mysql_username> <mysql_password> <database_name>
```

## Task 1: Filter states

Script: `1-filter_states.py`

This script lists all states whose name starts with the letter 'N' (uppercase) from the database `hbtn_0e_0_usa`.

Usage:
```bash
python 1-filter_states.py <mysql_username> <mysql_password> <database_name>
```

## Task 2: Filter states by user input

Script: `2-my_filter_states.py`

This script takes a state name as an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where the name matches the argument.

Usage:
```bash
python 2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
```

## Task 3: SQL Injection...

Script: `3-my_safe_filter_states.py`

This script is similar to Task 2 but is safe from SQL injection attacks. It properly handles user input to prevent malicious SQL queries.

Usage:
```bash
python 3-my_safe_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
```

## Task 4: Cities by states

Script: `4-cities_by_state.py`

This script lists all cities from the database `hbtn_0e_4_usa` in ascending order by their `id` column.

Usage:
```bash
python 4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
```

## Task 5: All cities by state

Script: `5-filter_cities.py`

This script takes a state name as an argument and lists all cities of that state from the database `hbtn_0e_4_usa`.

Usage:
```bash
python 5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>
```

## Task 6: First state model

File: `model_state.py`

This Python file contains the class definition of a `State` and an instance of `Base` using SQLAlchemy. The `State` class represents a table in the database `hbtn_0e_6_usa` and has attributes `id` and `name`.

## Task 7: All states via SQLAlchemy

Script: `7-model_state_fetch_all.py`

This script lists all `State` objects from the database `hbtn_0e_6_usa` in ascending order by their `id` attribute.

Usage:
```bash
python 7-model_state_fetch_all.py <mysql_username> <mysql_password> <database_name>
```

## Task 8: First state

Script: `8-model_state_fetch_first.py`

This script prints the first `State` object from the database `hbtn_0e_6_usa` based on their `id` attribute.

Usage:
```bash
python 8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>
```

## Task 9: Contains 'a'

Script: `9-model_state_filter_a.py`

This script lists all `State` objects from the database `hbtn_0e_6_usa` that contain the letter 'a' in their name, in ascending order by their `id` attribute.

Usage:
```bash
python 9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>
```

## Task 10: Get a state

Script: `10-model_state_my_get.py`

This script prints the `id` of the `State` object with the given name from the database `hbtn_0e_6_usa`. If no state has the provided name, it displays "Not found".

Usage:
```bash
python 10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> <state_name>
```

## Task 11: Add a new state

Script: `11-model_state_insert.py`

This script adds the `State` object with the name "Louisiana" to the database `hbtn_0e_6_usa` and prints its newly generated `id`.

Usage:
```bash
python 11-model_state_insert.py <mysql_username> <mysql_password> <database_name>
```

## Task 12: Update a state

Script: `12-model_state_update_id_2.py`

This script changes the name of the `State` object with `id=2` in the database `hbtn_0e_6_usa` to "New Mexico".

Usage:
```bash
python 12-model_state_update_id_2.py <mysql_username> <mysql_password> <database_name>
```

## Task 13: Delete states

Script: `13-model_state_delete_a.py`

This script deletes all `State` objects from the database `hbtn_0e_6_usa` that contain the letter 'a' in their name.

Usage:
```bash
python 13-model_state_delete_a.py <mysql_username> <mysql_password> <database_name>
```

## Task 14: Cities in state

File: `model_city.py`

This Python file contains the class definition of a `City` that inherits from `Base` and represents a table in the database `hbtn_0e_14_usa`. The `City` class has attributes `id`, `name`, and `state_id`, where `state_id` is a foreign key to `states.id`.

Script: `14-model_city_fetch_by_state.py`

This script lists all `City` objects from the database `hbtn_0e_14_usa` in ascending order by their `id` attribute. It displays the results in the format `<state name>: (<city id>) <city name>`.

Usage:
```bash
python 14-model_city_fetch_by_state.py <mysql_username> <mysql_password> <database_name>
```

## Authors
This project was realized Christophe Ngan (@Sirothpech)
