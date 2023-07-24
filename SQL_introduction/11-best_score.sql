-- Script to list all records with score >= 10 in the table second_table in the database hbtn_0c_0
-- The query retrieves all records with score >= 10 from the second_table, ordering them by score in descending order.
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
