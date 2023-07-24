-- Script to create the table second_table in the database hbtn_0c_0 and add multiple rows
-- The query creates the table if it doesn't exist and inserts the specified records.

CREATE TABLE IF NOT EXISTS second_table (
  id INT,
  name VARCHAR(256),
  score INT
);

INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
