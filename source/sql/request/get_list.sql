SELECT *
FROM "list" as L JOIN "user" as U ON L.username = U.username
WHERE L.username = ?;