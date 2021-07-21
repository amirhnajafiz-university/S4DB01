SELECT C.movie_id, C.creator
FROM "movie_creator" as C JOIN "movie" as M ON C.movie_id = M.movie_id
WHERE M.movie_id = ?;