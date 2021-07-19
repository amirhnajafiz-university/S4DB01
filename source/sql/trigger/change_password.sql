CREATE TRIGGER comment_on_movie
ON user
AFTER UPDATE
AS BEGIN
    WHEN (LEN(user.password) < 6 )
    BEGIN
     ROLLBACK
    END;
END;

// TODO: Fix this