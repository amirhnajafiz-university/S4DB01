SELECT M.movie_id, M.movie_file, M.name, M.movie_year, M.description
FROM "movie" as M JOIN ("list" as L JOIN "movie_in_list" as I ON I.list_id = L.list_id) ON M.movie_id = I.movie_id
WHERE L.list_id = ?;