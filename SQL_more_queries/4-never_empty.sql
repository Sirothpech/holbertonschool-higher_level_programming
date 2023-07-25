-- Script to create the table id_not_null on your MySQL server.
-- The table id_not_null has two columns: id (INT) with a default value of 1, and name (VARCHAR(256)).
-- If the table id_not_null already exists, the script will not fail.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
