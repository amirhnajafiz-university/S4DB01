SELECT M.movie_id, M.movie_file, M.name, M.movie_year, M.description
FROM "watch" as W JOIN "movie" as M ON W.movie_id = M.movie_id
WHERE W.username = ?;