CREATE TRIGGER check_pro_date AFTER INSERT ON "watch_special"
BEGIN 
    SELECT CASE
        WHEN((SELECT expiredate FROM "special_user" WHERE pro_id = NEW.pro_id) <= DATETIME('now'))
        THEN RAISE(ABORT, 'Your wallet amount in low.')
        END;
    END;
END;