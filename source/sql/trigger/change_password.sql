CREATE TRIGGER comment_on_movie
ON "user"
AFTER INSERT, UPDATE
AS BEGIN
    IF (LEN(user.password) < 6)
    BEGIN
     RAISERROR('Password is too weak!', 10, 1)
     ROLLBACK
    END;
END;
