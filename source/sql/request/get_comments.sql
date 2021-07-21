SELECT movie_id, username, user_comment, rate
FROM "comment"
WHERE movie_id = ?
LIMIT 5
OFFSET ?;