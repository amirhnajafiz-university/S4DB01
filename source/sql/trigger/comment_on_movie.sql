CREATE TRIGGER comment_on_movie
ON "comment"
AFTER INSERT, UPDATE
AS 
BEGIN
    DECLARE @count int 
    DECLARE @special_count int

    SELECT
        @count = count(*) 
    FROM "comment" as C 
    WHERE C.pro_username NOT IN (SELECT username FROM "watch" WHERE movie_id = C.movie_id)

    SELECT
        @special_count = count(*)
    FROM "comment" as C 
    WHERE C.pro_username NOT IN (   SELECT username 
                                    FROM "special_user" as S JOIN "user" U ON S.username = U.username 
                                    WHERE S.pro_id = (SELECT pro_id FROM "watch_special" as W WHERE W.movie_id = C.movie_id ) )

    IF (@count > 0 OR @special_count > 0)
    BEGIN 
     RAISERROR('Cannot comment on this movie. Not watched yet!', 10, 1)
     ROLLBACK
    END;

END;
