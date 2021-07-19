SELECT *
FROM "movie" as M JOIN ("movie_id" as I JOIN "tag" as T ON I.tag_id = T.tag_id) ON M.movie_id = I.movie_id
WHERE T.name = ?;