-- Script to list the number of records with the same score in the table second_table
-- The query uses the SELECT statement with the COUNT() function to count the number of records for each score.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
