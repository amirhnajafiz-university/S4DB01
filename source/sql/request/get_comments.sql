SELECT * 
FROM "comment"
WHERE movie_id = ?
LIMIT 5
OFFSET ?;