SELECT * 
FROM "movie" as M JOIN "special_movie" as S ON M.movie_id = S.movie_id
WHERE M.movie_id = ?;