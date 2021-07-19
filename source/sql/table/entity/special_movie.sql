CREATE TABLE "special_movie" (
	special_id int,
	movie_id int NOT NULL,
	price int NOT NULL,
	PRIMARY KEY (special_id),
	FOREIGN KEY (movie_id) REFERENCES "movie" (movie_id) ON DELETE CASCADE
);