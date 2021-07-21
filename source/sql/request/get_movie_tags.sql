SELECT M.movie_id, T.name
FROM "movie" as M JOIN ("movie_tag" as I JOIN "tag" as T ON I.tag_id = T.tag_id) ON M.movie_id = I.movie_id
WHERE M.movie_id = ?;