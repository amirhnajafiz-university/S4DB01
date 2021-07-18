CREATE TABLE "movie_creator" (
	creator varchar(1024),
	movie_id int,
	PRIMARY KEY (creator, movie_id),
	FOREIGN KEY (movie_id) REFERENCES "movie" (movie_id)
);