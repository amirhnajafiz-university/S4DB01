BEGIN TRANSACTION;

UPDATE "user" SET point = point + ? WHERE username = ?;

COMMIT;