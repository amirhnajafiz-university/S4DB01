CREATE TABLE "watch" (
	username varchar(50),
	movie_id int,
	PRIMARY KEY (username, movie_id),
	FOREIGN KEY (username) REFERENCES "user" (username) ON DELETE CASCADE,
	FOREIGN KEY (movie_id) REFERENCES "movie" (movie_id) ON DELETE CASCADE
);