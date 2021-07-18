CREATE TABLE "watch_special" (
	pro_id int,
	movie_id int,
	PRIMARY KEY (pro_id, movie_id),
	FOREIGN KEY (pro_id) REFERENCES "special_user" (pro_id),
	FOREIGN KEY (movie_id) REFERENCES "special_movie" (movie_id)
);