-- Script to list all the cities of California from the hbtn_0d_usa database.
-- The states table contains only one record where name = California (but the id can be different).
-- Results are sorted in ascending order by cities.id.

SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
