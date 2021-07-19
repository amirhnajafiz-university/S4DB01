CREATE TRIGGER watch_special_movie AFTER INSERT ON "watch_special"
BEGIN
    SELECT CASE
        WHEN (NEW.pro_id NOT IN (SELECT pro_id FROM special_user))
        THEN RAISE(ABORT, 'Cannot watch this movie.')
        END;
    END;
END;
