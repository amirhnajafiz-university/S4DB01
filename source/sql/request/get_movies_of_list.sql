SELECT *
FROM "movie" as M JOIN ("list" as L JOIN "movie_in_list" as I ON I.list_id = L.list_id) ON M.movie_id = I.movie_id
WHERE L.username = ?;