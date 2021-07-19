CREATE TRIGGER watch_special_movie
ON "watch_special"
AFTER INSERT
AS BEGIN
    IF (NEW.pro_id NOT IN (SELECT pro_id FROM special_user))
    BEGIN
     RAISERROR('Not special user', 10, 1)
     ROLLBACK
    END;
END;
