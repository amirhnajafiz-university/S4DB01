SELECT M.movie_id, M.movie_file, M.name, M.movie_year, M.description, S.price 
FROM "movie" as M JOIN "special_movie" as S ON M.movie_id = S.movie_id
WHERE M.movie_id = ?;