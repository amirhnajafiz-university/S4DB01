CREATE TRIGGER up_password_check AFTER UPDATE ON "user"
BEGIN 
    SELECT CASE
        WHEN(length(NEW.password) < 6)
        THEN RAISE(ABORT, 'Password is too short.')
        END;
    END;
END;
