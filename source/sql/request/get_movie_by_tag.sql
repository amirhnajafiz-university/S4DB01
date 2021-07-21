SELECT M.movie_id, M.movie_file, M.name, M.movie_year, M.description, T.name
FROM "movie" as M JOIN ("movie_tag" as I JOIN "tag" as T ON I.tag_id = T.tag_id) ON M.movie_id = I.movie_id
WHERE T.name = ? AND M.name LIKE ?
LIMIT 5
OFFSET ?;