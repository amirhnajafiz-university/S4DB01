SELECT movie_id, movie_file, name, movie_year, description 
FROM "movie" as M JOIN "special_movie" as S ON M.movie_id = S.movie_id
WHERE M.movie_id = ?;