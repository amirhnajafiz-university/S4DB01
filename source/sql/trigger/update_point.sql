CREATE TRIGGER update_point AFTER UPDATE ON "user"
BEGIN 
    SELECT CASE
        WHEN(NEW.point < 0)
        THEN RAISE(ABORT, 'Your wallet amount in low.')
        END;
    END;
END;