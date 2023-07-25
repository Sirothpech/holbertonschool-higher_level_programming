-- Script to list all records with a valid name in the table second_table
-- The query retrieves all records where the name is not NULL or an empty string.
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
