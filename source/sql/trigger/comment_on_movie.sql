CREATE TRIGGER comment_on_movie AFTER INSERT ON "comment"
BEGIN 
    SELECT CASE
        WHEN(NEW.pro_username NOT IN (SELECT username FROM "watch" WHERE movie_id = NEW.movie_id) OR 
                                      NEW.pro_username NOT IN (SELECT username 
                                      FROM "special_user" as S JOIN "user" U ON S.username = U.username 
                                      WHERE S.pro_id = SOME (SELECT pro_id FROM "watch_special" as W WHERE W.movie_id = NEW.movie_id ) ))
        THEN RAISE(ABORT, 'Cannot comment on this movie. Not watched yet!')
        END;
    END;
END;