CREATE TRIGGER update_wallet AFTER INSERT ON "user"
BEGIN 
    SELECT CASE
        WHEN(NEW.wallet < 0)
        THEN RAISE(ABORT, 'Your wallet amount in low.')
        END;
    END;
END;