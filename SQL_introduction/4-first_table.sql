-- Script to create the table first_table in the current database
-- The query creates the table with the specified columns if it doesn't exist.
CREATE TABLE IF NOT EXISTS first_table (
  id INT,
  name VARCHAR(256)
);
