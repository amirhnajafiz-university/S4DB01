SELECT M.movie_id, M.name, M.movie_year, M.description
FROM "watch_special" as W JOIN "movie" as M ON w.movie_id = M.movie_id
WHERE W.pro_id = ?;