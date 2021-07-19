BEGIN TRANSACTION;

// TODO: First decrease then set user to go pro

INSERT INTO "special_user" (pro_id, expiredate)
    VALUES(?, ?);

COMMIT;