CREATE TABLE "comment" (
	rate int DEFAULT 0,
	user_comment varchar(1024) DEFAULT NULL,
	username varchar(50),
	movie_id int,
	PRIMARY KEY (username, movie_id),
	FOREIGN KEY (username) REFERENCES "user" (username) ON DELETE CASCADE,
	FOREIGN KEY (movie_id) REFERENCES "movie" (movie_id) ON DELETE CASCADE,
	CHECK (rate IN (0, 1, 2, 3, 4, 5))
);