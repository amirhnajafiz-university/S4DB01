BEGIN TRANSACTION;

INSERT INTO "user" (username, password, name, email, phonenumber, nationalID, wallet, point)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?);

COMMIT;