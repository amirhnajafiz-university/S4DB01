CREATE TRIGGER comment_on_movie
ON comment
AFTER INSERT
AS BEGIN
    WHEN (comment.pro_username not int (SELECT username FROM watch WHERE movie_id = comment.movie_id))
    BEGIN
     ROLLBACK
    END;
END;