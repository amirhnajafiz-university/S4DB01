CREATE TRIGGER watch_special_movie
ON watch_special
AFTER INSERT
AS BEGIN
    WHEN (watch_special.pro_id not int (SELECT pro_id FROM special_user))
    BEGIN
     ROLLBACK
    END;
END;

// TODO: Fix this