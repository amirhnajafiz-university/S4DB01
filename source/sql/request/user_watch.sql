SELECT *
FROM "watch" as W JOIN "movie" as M ON W.movie_id = M.movie_id
WHERE W.username = ?;