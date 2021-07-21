SELECT movie_id, movie_file, name, movie_year, description
FROM "movie"
WHERE name LIKE ?
LIMIT 5
OFFSET ?;