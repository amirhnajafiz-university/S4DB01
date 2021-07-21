CREATE TRIGGER comment_on_movie AFTER INSERT ON "comment"
BEGIN 
    SELECT CASE
        WHEN(NEW.username NOT IN (SELECT W.username FROM "watch" as W WHERE NEW.movie_id = W.movie_id)) AND (NEW.username NOT IN (SELECT U.username FROM "watch_special" as W JOIN "special_user" as U ON W.pro_id = U.pro_id WHERE NEW.movie_id = W.movie_id))
        THEN RAISE(ABORT, 'Cannot comment on this movie. Not watched yet!')
        END;
    END;
END;