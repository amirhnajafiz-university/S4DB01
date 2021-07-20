SELECT COUNT(*) 
FROM "comment" as C JOIN "movie" as M ON C.movie_id = M.movie_id
WHERE movie_id = ?;