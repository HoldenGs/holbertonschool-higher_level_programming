-- Print out tv show titles and genre ids
-- Natural join select
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
NATURAL JOIN tv_show_genres
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
