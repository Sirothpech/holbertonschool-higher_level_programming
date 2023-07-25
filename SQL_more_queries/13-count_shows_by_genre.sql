-- Script to list genres from the hbtn_0d_tvshows database and display the number of linked shows.
-- Columns displayed: <TV Show genre> - <Number of shows linked to this genre>.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
HAVING COUNT(tv_show_genres.genre_id) > 0
ORDER BY number_of_shows DESC;
