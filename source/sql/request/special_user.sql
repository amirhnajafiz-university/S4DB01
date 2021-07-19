SELECT pro_id
FROM "user" as U JOIN "special_user" as S ON U.username = S.username
WHERE U.username = ?;